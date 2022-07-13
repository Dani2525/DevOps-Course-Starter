FROM python:3.8 as base
RUN pip install poetry
WORKDIR /app/
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false --local && poetry install
COPY ./todo_app /app/todo_app
FROM base as development
ENV FLASK_ENV=development
ENTRYPOINT ["poetry", "run", "flask", "run", "--host", "0.0.0.0"]
FROM base as test
ENV FLASK_ENV=test
ENTRYPOINT ["poetry", "run", "pytest"]
FROM base as production
CMD poetry run gunicorn "todo_app.app:create_app()" --bind 0.0.0.0:$PORT
ENV FLASK_ENV=production