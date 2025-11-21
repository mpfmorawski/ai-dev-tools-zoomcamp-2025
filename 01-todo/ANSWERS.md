## Question 1: Install Django

### Question:

We want to install Django. Ask AI to help you with that.

What's the command you used for that?

There could be multiple ways to do it. Put the one that AI suggested in the homework form.

### Answer

Initial command to install Django propsed by Codex:
```bash
cd /home/mpfmorawski/learning/ai-dev-tools-zoomcamp-2025/ && python -m pip install Django
```

Final command to install Django (after adding information that I typically use `uv`):
```bash
cd 01-todo/codex && uv init
cd 01-todo/codex && uv add django
```

## Question 2: Project and App

### Question

Now we need to create a project and an app for that.

Follow the instructions from AI to do it. At some point, you will need to include the app you created in the project.

What's the file you need to edit for that?

- `settings.py`
- `manage.py`
- `urls.py`
- `wsgi.py`

### Answer

The file to edit is `settings.py`.

## Question 3: Django Models

### Question

Let's now proceed to creating models - the mapping from python objects to a relational database.

For the TODO app, which models do we need? Implement them.

What's the next step you need to take?

- Run the application
- Add the models to the admin panel
- Run migrations
- Create a makefile

### Answer

The `Task` model is implemented in `codex/todo_project/todos/models.py` with fields:
- `title` (CharField)
- `notes` (TextField, optional)
- `completed` (BooleanField)
- `created_at` (DateTimeField, auto_now_add=True)
- `updated_at` (DateTimeField, auto_now=True)

Next step: **Run migrations** — create and apply the migrations with:

```bash
cd 01-todo/codex
python manage.py makemigrations
python manage.py migrate
```
