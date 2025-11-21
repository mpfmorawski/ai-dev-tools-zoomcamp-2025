from django.contrib.messages.test import MessagesTestMixin
from django.test import TestCase
from django.urls import reverse
from .models import Task


class TaskModelTest(TestCase):
    def test_task_str(self):
        task = Task.objects.create(title="Test Task")
        self.assertEqual(str(task), "Test Task")


class TaskViewTest(TestCase, MessagesTestMixin):
    def test_task_list_get_empty(self):
        response = self.client.get(reverse("todos:task_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No tasks yet")
        self.assertEqual(list(response.context["tasks"]), [])

    def test_task_list_get_with_tasks(self):
        Task.objects.create(title="Task 1")
        Task.objects.create(title="Task 2")
        response = self.client.get(reverse("todos:task_list"))
        self.assertEqual(response.status_code, 200)
        tasks = list(response.context["tasks"])
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].title, "Task 2")
        self.assertEqual(tasks[1].title, "Task 1")

    def test_create_task_valid(self):
        data = {"title": "New Task", "notes": "Some notes"}
        response = self.client.post(reverse("todos:task_list"), data=data)
        self.assertEqual(response.status_code, 302)  # redirect
        self.assertEqual(Task.objects.count(), 1)
        task = Task.objects.first()
        self.assertEqual(task.title, "New Task")
        self.assertEqual(task.notes, "Some notes")
        self.assertFalse(task.completed)

    def test_create_task_invalid(self):
        data = {"title": "", "notes": "notes"}
        response = self.client.post(reverse("todos:task_list"), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.count(), 0)

    def test_toggle_task(self):
        task = Task.objects.create(title="Task", completed=False)
        response = self.client.post(reverse("todos:toggle_task", args=[task.pk]))
        self.assertEqual(response.status_code, 302)
        task.refresh_from_db()
        self.assertTrue(task.completed)

    def test_delete_task(self):
        task = Task.objects.create(title="Task")
        response = self.client.post(reverse("todos:delete_task", args=[task.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)

    def test_toggle_task_back_to_incomplete(self):
        task = Task.objects.create(title="Task", completed=True)
        response = self.client.post(reverse("todos:toggle_task", args=[task.pk]))
        self.assertEqual(response.status_code, 302)
        task.refresh_from_db()
        self.assertFalse(task.completed)

    def test_create_task_success_message(self):
        data = {"title": "New Task"}
        response = self.client.post(reverse("todos:task_list"), data=data, follow=True)
        self.assertRedirects(response, reverse("todos:task_list"))
        self.assertContains(response, "Task added.")

    def test_create_task_invalid_error_message(self):
        data = {"title": ""}
        response = self.client.post(reverse("todos:task_list"), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please fix the issues below.")

    def test_delete_task_info_message(self):
        task = Task.objects.create(title="Task")
        response = self.client.post(
            reverse("todos:delete_task", args=[task.pk]), follow=True
        )
        self.assertRedirects(response, reverse("todos:task_list"))
        self.assertContains(response, "Task removed.")

    def test_create_task_without_notes(self):
        data = {"title": "Task without notes"}
        response = self.client.post(reverse("todos:task_list"), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)
        task = Task.objects.first()
        self.assertEqual(task.title, "Task without notes")
        self.assertEqual(task.notes, "")

    def test_toggle_task_404_invalid_pk(self):
        response = self.client.post(reverse("todos:toggle_task", args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_delete_task_404_invalid_pk(self):
        response = self.client.post(reverse("todos:delete_task", args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_toggle_task_method_not_allowed(self):
        task = Task.objects.create(title="Task")
        response = self.client.get(reverse("todos:toggle_task", args=[task.pk]))
        self.assertEqual(response.status_code, 405)

    def test_delete_task_method_not_allowed(self):
        task = Task.objects.create(title="Task")
        response = self.client.get(reverse("todos:delete_task", args=[task.pk]))
        self.assertEqual(response.status_code, 405)

    def test_task_defaults(self):
        task = Task.objects.create(title="Test")
        self.assertFalse(task.completed)
        self.assertIsNotNone(task.created_at)
        self.assertIsNotNone(task.updated_at)

    def test_task_ordering_explicit(self):
        Task.objects.create(title="First")
        t2 = Task.objects.create(title="Second")
        tasks = list(Task.objects.all())
        self.assertEqual(tasks[0], t2)
