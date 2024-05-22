FROM python:3.12.3
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH=$PATH:/root/.local/bin/
COPY pyproject.toml poetry.toml /opt/todoapp/
WORKDIR /opt/todoapp/
RUN poetry install
RUN poetry add gunicorn
COPY todo_app /opt/todoapp/todo_app
EXPOSE 8000
ENTRYPOINT poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"
