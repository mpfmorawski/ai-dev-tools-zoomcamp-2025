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

## Question 4. TODO Logic

### Question

Let's now ask AI to implement the logic for the TODO app. Where do we put it?

- `views.py`
- `urls.py`
- `admin.py`
- `tests.py`

### Answer
The TODO app logic is implemented in `views.py`.

## Question 5. Templates

### Question

Next step is creating the templates. You will need at least two: the base one and the home one. Let's call them `base.html` and `home.html`.

Where do you need to register the directory with the templates? 

- `INSTALLED_APPS` in project's `settings.py`
- `TEMPLATES['DIRS']` in project's `settings.py`
- `TEMPLATES['APP_DIRS']` in project's `settings.py`
- In the app's `urls.py`

### Answer

You register the project-level templates directory in `TEMPLATES['DIRS']` inside the project's `settings.py`.

## Question 6. Tests

### Question

Now let's ask AI to cover our functionality with tests.

- Ask it which scenarios we should cover
- Make sure they make sense
- Let it implement it and run them 

Probably it will require a few iterations to make sure that tests pass and evertyhing is working. 

What's the command you use for running tests in the terminal? 

- `pytest`
- `python manage.py test`
- `python -m django run_tests`
- `django-admin test`

### Answer

`python manage.py test`
