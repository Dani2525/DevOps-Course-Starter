FROM python:3.8 as base
RUN pip install poetry
WORKDIR /app/
COPY poetry.lock pyproject.toml /app/
RUN poetry install --no-dev
COPY ./todo_app /app/todo_app
FROM base as development
ENV FLASK_ENV=development
ENTRYPOINT ["poetry", "run", "flask", "run", "--host", "0.0.0.0"]
FROM base as production
ENTRYPOINT ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:5000", "todo_app.app:create_app()"]
ENV FLASK_ENV=production