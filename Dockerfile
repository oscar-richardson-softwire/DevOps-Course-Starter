FROM python:3.12.3 as base
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH=$PATH:/root/.local/bin/
COPY pyproject.toml poetry.toml /opt/todoapp/
WORKDIR /opt/todoapp/
RUN poetry install
COPY todo_app /opt/todoapp/todo_app

FROM base as production
RUN poetry add gunicorn
EXPOSE 8000
ENTRYPOINT poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"

FROM base as development
ENV FLASK_DEBUG=true
EXPOSE 5000
ENTRYPOINT poetry run flask run --host=0.0.0.0

FROM base as test
ENTRYPOINT poetry run pytest
