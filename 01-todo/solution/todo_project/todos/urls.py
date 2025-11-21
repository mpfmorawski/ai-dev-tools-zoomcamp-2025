from django.urls import path

from . import views

app_name = "todos"

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("tasks/<int:pk>/toggle/", views.toggle_task, name="toggle_task"),
    path("tasks/<int:pk>/delete/", views.delete_task, name="delete_task"),
]
