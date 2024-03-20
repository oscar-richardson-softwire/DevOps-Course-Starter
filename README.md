# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

You can check poetry is installed by running `poetry --version` from a terminal.

**Please note that after installing poetry you may need to restart VSCode and any terminals you are running before poetry will be recognised.**

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

## Environment variables

You'll need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

### Trello REST API

The app uses Trello to store to-do items (in the form of cards on a Trello board). The app interfaces with Trello using the [Trello REST API](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/).

In order to use the app, you will need to do the following:
1. Create or sign into a [Trello account](https://trello.com/signup)
2. Create a Trello [Power-Up](https://trello.com/power-ups/admin) (you'll need to associate this Power-Up to a workspace, so you may need to create a workspace if you don't already have one)
3. After creating a Power-Up, generate a new API key
4. Set the value for `TRELLO_API_KEY` in your `.env` file to be this new API key 
5. Generate an API token by clicking on the link on the page displaying your new API key
6. Set the value for `TRELLO_API_TOKEN` in your `.env` file to be this API token 
7. Create a new Trello board (in the workspace associated to this Power-Up) to store the to-do cards
8. Make a `GET` request to `https://api.trello.com/1/members/me/boards?key=<yourApiKey>&token=<yourApiToken>`
(e.g., using a browser, curl, or a tool such as Postman or the Thunder Client Extension for VS Code)
9. Find the `id` property of this newly created board in the response and set the value for `TRELLO_BOARD_ID`
in your `.env` file to be this `id`
10. Make a `GET` request to `https://api.trello.com/1/boards/<yourBoardId>/lists?key=<yourApiKey>&token=<yourApiToken>`
11. Find the `id` property of the list with the `name` `'To Do'` in the response and set the value for `TRELLO_TO_DO_COLUMN_LIST_ID` to be this `id`
12. Find the `id` property of the list with the `name` `'Done'` in the response and set the value for `TRELLO_DONE_COLUMN_LIST_ID` to be this `id`

## Running the App

Once the all dependencies have been installed and the necessary environment variables have been set, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app 'todo_app/app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 113-666-066
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Testing

### Terminal

#### Run all unit tests

From the project root (`DevOps-Course-Starter`), run the following from your preferred shell:

```shell
$ pytest
```

#### Run a single unit test file

From the project root (`DevOps-Course-Starter`), run the following from your preferred shell:

```shell
$ pytest todo_app/<rest of path to test file>
```

E.g.,

```shell
$ pytest todo_app/data/classes/test_view_model.py
```

#### Run a single unit test

From the project root (`DevOps-Course-Starter`), run the following from your preferred shell:

```shell
$ pytest todo_app/<rest of path to test file>::<name of test function>
```

E.g.,

```shell
$ pytest todo_app/data/classes/test_view_model.py::test_view_model_done_items_property_returns_items_with_status_done
```

### VSCode GUI

#### Setup

Select the 'Testing' tab from the 'Activity Bar', select 'Configure Python Tests', choose 'pytest', then choose '`todo_app`' as the folder containing the tests.

#### Run all unit tests

Select the 'Testing' tab from the 'Activity Bar', then select the play button icon, 'Run Tests' in the middle of the top bar on the tab.

#### Run all unit tests in a directory or file, or run a single unit test

Select the 'Testing' tab from the 'Activity Bar', use the dropdown 'Explorer'-style menu to locate the directory/file/test, then hover over its name and click the play button icon, 'Run Test'.
