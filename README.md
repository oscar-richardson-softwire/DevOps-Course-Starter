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

### CosmosDB database

The app uses a CosmosDB database to store to-do items and their statuses. The app interfaces with this database using [PyMongo](https://pymongo.readthedocs.io/en/stable/tutorial.html).

In order to use the app, you will need to do the following:
1. Follow [`these instructions`](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) to install the Azure CLI on your machine if you don't have it installed already
2. Open up a new terminal window and run:

```bash
$ az login
```

Which will launch a browser window to allow you to log in to your Azure account

3. Make a note of the name of the resource group that you wish to create the Web App under (creating a new resource group if necessary). You can see the names of your resource groups by navigating to the [`Azure portal`](https://portal.azure.com/#home) -> [`Resource groups`](https://portal.azure.com/#browse/resourcegroups)
4. Create a new CosmosDB account by running:

```bash
$ az cosmosdb create --name <cosmos_account_name> --resource-group <resource_group_name> --kind MongoDB --capabilities EnableServerless --server-version 4.2
```

5. Create a new MongoDB database under that account by running:

```bash
$ az cosmosdb mongodb database create --account-name <cosmos_account_name> --name <database_name> --resource-group <resource_group_name>
```

Note: it can take a few minutes for your CosmosDB instance to spin up

6. Retrieve your CosmosDB connection by running:

```bash
$ az cosmosdb keys list -n <cosmos_account_name> -g <resource_group_name> --type connection-strings
```

and copying the value of `"connectionString"` for the connection string with description `"Primary MongoDB Connection String"`. Set this as the value for `COSMOS_DB_CONNECTION_STRING` in your `.env` file

7. Set the value for `DB_NAME` in your `.env` file to a name of your choice (when the app tries to connect to this database it will be created if it does not already exist)

## Running the app locally

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

## Running the app in Docker

It is also possible to run the app inside a Docker container, allowing you to run the app inside a dedicated, reproducible environment that is isolated from your local machine.

### Running the app in a production container

To run the app in a production container (which uses Gunicorn, a true production-ready server), first run the following command to build a production image:
```bash
$ docker build --target production -t todo-app:prod .
```

This creates a production image with the name `'todo-app'` and the tag `'prod'`.

Once you have a production image, you can run a production container from it by running:
```bash
$ docker run --env-file .env -p 5000:8000 -it todo-app:prod
```

Now visit [`http://localhost:8000/`](http://localhost:8000/) in your web browser to view the app.

The `--env-file` flag loads the `.env` file into the container.

The `-p` (or `--publish`) flag makes the container's port 8000 (where the app is running) available on your local machine's port 5000.

The `-it` (or `--interactive` + `--tty`) starts an interactive terminal when starting the container, allowing you to (for instance) use `Ctrl/Cmd + C` to exit the container.

### Running the app in a development container

To run the app in a development container (which uses Flask's development server with `FLASK_DEBUG` set to `true` to allow hot reloading of code changes), first run the following command to build a development image:
```bash
$ docker build --target development -t todo-app:dev .
```

This creates a development image with the name `'todo-app'` and the tag `'dev'`.

Once you have a development image, you can run a development container from it by running:
```bash
$ docker run --env-file .env -p 5000:5000 --mount "type=bind,source=$(pwd)/todo_app,target=/opt/todoapp/todo_app" -it todo-app:dev
```

Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

The `--env-file` flag loads the `.env` file into the container.

The `-p` (or `--publish`) flag makes the container's port 5000 (where the app is running) available on your local machine's port 5000. This allows hot reloading of code changes without the need to rebuild the image.

The `--mount` flag makes the `/todo_app` directory on your local machine available at `/opt/todoapp/todo_app` inside the container via a bind mount.

The `-it` (or `--interactive` + `--tty`) starts an interactive terminal when starting the container, allowing you to (for instance) use `Ctrl/Cmd + C` to exit the container.

## Testing

### Directory structure

Unit tests live in the same directory as the code that they test (e.g., `test_view_model.py` is in the same directory as `ViewModel.py`).

Integration tests live in the `test_integration.py` file in the top level of the `todo_app` directory.

### Terminal

#### Run all unit and integration tests

From the project root (`DevOps-Course-Starter`), run the following from your preferred shell:

```shell
$ poetry run pytest
```

#### Run a single unit/integration test file

From the project root (`DevOps-Course-Starter`), run the following from your preferred shell:

```shell
$ poetry run pytest todo_app/<rest_of_path_to_test_file>
```

E.g.,

```shell
$ poetry run pytest todo_app/data/classes/test_view_model.py
```

#### Run a single unit/integration test

From the project root (`DevOps-Course-Starter`), run the following from your preferred shell:

```shell
$ poetry run pytest todo_app/<rest_of_path_to_test_file>::<name_of_test_function>
```

E.g.,

```shell
$ poetry run pytest todo_app/data/classes/test_view_model.py::test_view_model_done_items_property_returns_items_with_status_done
```

### Docker

#### Setup

From the project root (`DevOps-Course-Starter`), run the following from your preferred shell:

```shell
$ docker build --target test --tag <name_you_want_to_give_to_test_image> .
```

#### Run all unit and integration tests

From the project root (`DevOps-Course-Starter`), run the following from your preferred shell:

```shell
$ docker run --env-file .env.test <name_you_gave_to_test_image_during_setup> 
```

#### Run a single unit/integration test file

From the project root (`DevOps-Course-Starter`), run the following from your preferred shell:

```shell
$ docker run --env-file .env.test <name_you_gave_to_test_image_during_setup> todo_app/<rest_of_path_to_test_file>
```

E.g.,

```shell
$ docker run --env-file .env.test test-image todo_app/data/classes/test_view_model.py
```

#### Run a single unit/integration test

From the project root (`DevOps-Course-Starter`), run the following from your preferred shell:

```shell
$ docker run --env-file .env.test <name_you_gave_to_test_image_during_setup> todo_app/<rest_of_path_to_test_file>::<name_of_test_function>
```

E.g.,

```shell
$ docker run --env-file .env.test test-image todo_app/data/classes/test_view_model.py::test_view_model_done_items_property_returns_items_with_status_done
```

Note: the above commands work because anything after the image name gets appended to the `ENTRYPOINT` in the `Dockerfile` (i.e., `poetry run pytest`).

### VSCode GUI

#### Setup

Select the 'Testing' tab from the 'Activity Bar', select 'Configure Python Tests', choose 'pytest', then choose '`todo_app`' as the folder containing the tests.

#### Run all unit and integration tests

Select the 'Testing' tab from the 'Activity Bar', then select the play button icon, 'Run Tests' in the middle of the top bar on the tab.

#### Run all unit/integration tests in a directory or file, or run a single unit/integration test

Select the 'Testing' tab from the 'Activity Bar', use the dropdown 'Explorer'-style menu to locate the directory/file/test, then hover over its name and click the play button icon, 'Run Test'.

## Infrastructure

### Provision a VM from an Ansible Control Node

From the project root (`DevOps-Course-Starter`), run the following from your preferred shell:

```shell
$ ansible-playbook provision-vm.yml -i provision-vm-inventory
```

When prompted, enter the CosmosDB connection string and DB name from your `.env` file. Note that your input for these fields is hidden.

## Manual deployment

This section documents manually deploying the app to Azure as a Web App that pulls a container image from the Docker Hub registry.

### Pushing a container image to the Docker Hub registry

Note: The latest production image (at the time of writing) is already pushed to `oscarrichardson/todo-app:prod` on Docker Hub.

To store a container image on the Docker Hub registry, first run the following command to log in to Docker Hub locally:

```bash
$ docker login
```

Once you have logged in, build an image that you want to push by running:

```bash
$ docker build --target <name_of_build_phase> -t <docker_hub_user_name>/todo-app:<tag> .
```

Finally, push the image to Docker Hub by running:

```bash
$ docker push <docker_hub_user_name>/todo-app:<tag>
```

This creates an image with the name `'todo-app'` under your user namespace on Docker Hub (trying to push just `todo-app:<tag>` will error because you won't have permission for the global namespace!).

### Deploying the container image to Azure Web App

1. Follow [`these instructions`](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) to install the Azure CLI on your machine if you don't have it installed already
2. Open up a new terminal window and run:

```bash
$ az login
```

Which will launch a browser window to allow you to log in to your Azure account

3. Make a note of the name of the resource group that you wish to create the Web App under (creating a new resource group if necessary). You can see the names of your resource groups by navigating to the [`Azure portal`](https://portal.azure.com/#home) -> [`Resource groups`](https://portal.azure.com/#browse/resourcegroups)
4. Create an App Service Plan by running:

```bash
$ az appservice plan create --resource-group <resource_group_name> -n <name_for_appservice_plan_of_your_choice> --sku B1 --is-linux
```

5. Create the Web App by running:

```bash
$ az webapp create --resource-group <resource_group_name> --plan <appservice_plan_name> --name <name_for_webapp_of_your_choice> --deployment-container-image-name docker.io/<docker_hub_user_name>/todo-app:<tag>
```

Note: The `<name_for_webapp_of_your_choice>` needs to be unique across all Azure Web Apps and will determine the URL of your deployed app: `https://<name_for_webapp_of_your_choice>.azurewebsites.net`

6. Add the environment variables from your `.env` file by navigating to the [`Azure portal`](https://portal.azure.com/#home) -> `App Services`, then selecting your Web App and navigating to `Settings` -> `Environment variables`. The environment variables can then be added one by one as key-value pairs. Make sure you click 'Apply' at the bottom of the page after adding all of the environment variables.

Note: as well as all of the variables from your `.env` file, you will also need to add `WEBSITES_PORT` will a value of `8000`. This is because, by default, Azure App Services assume that the app is listening on either port `80` or `8080`, when in fact (in the production image) the app listens on port `8000` (see the `Dockerfile`).

7. See your live site at `https://<webapp_name>.azurewebsites.net/`!

### Using the webhook URL to manually update the container

Azure exposes a webhook URL; `POST` requests to this endpoint cause the app to restart, pulling the latest version of the container image from the configured registry.

1. Find your webhook URL by navigating to the [`Azure portal`](https://portal.azure.com/#home) -> `App Services`, then selecting your Web App and navigating to `Deployment` -> `Deployment Center`. If it says `"REDACTED"` for the webhook URL, you may need to enable basic authentication for the App Service's FTP and SCM sites by running:

```bash
$ az resource update --resource-group <resource_group_name> --name ftp --namespace Microsoft.Web --resource-type basicPublishingCredentialsPolicies --parent sites/<webapp_name>  --set properties.allow=true

$ az resource update --resource-group <resource_group_name> --name scm --namespace Microsoft.Web --resource-type basicPublishingCredentialsPolicies --parent sites/<webapp_name>  --set properties.allow=true
```

2. Open a Linux/Mac shell (or Git Bash on Windows) and run:

```bash
$ curl -v -X POST '<webhook_url>'
```

Note: You must wrap the `<webhook_url>` in single quotes in the terminal as double quotes will treat `$` as a special character.

The response should include a link to a log-stream showing the re-pulling of the image and the restarting of the app.

Note: If this `POST` request returns a `401` error response, you may need to enable basic authentication for the App Service's FTP and SCM sites (if you haven't already); see the instructions in step 1 above.
