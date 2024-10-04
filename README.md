# DevOps technical assessment

The goal of this technical assessment is to package a small Python function as an AWS Lambda. The assessment covers several points:
- Development of the AWS Lambda entrypoint in Python to be invoked as AWS Lambda function or via an HTTP request.
- Automatic deployment of the function in a local Kubernetes cluster.
- Configuration of a Continuous Integration workflows using Github Actions to automate testing, packaging and deployment.
- Code organization between source, test, Continuous Integration (CI) workflows, Kubernetes manifest files...

## Create a repository from this template

Recommended configuration:
- Windows 10/11 machine with [Windows Subsystem for Linux](https://learn.microsoft.com/fr-fr/windows/wsl/install) (WSL) feature enabled.
- VSCode editor installed on Windows and running on WSL (aka the 'local' machine in the following).
- Git and Docker installed on WSL.

The development environment can be reproduced with the [Devcontainer](https://code.visualstudio.com/docs/devcontainers/containers) feature of VSCode based on `.devcontainer/devcontainer.json`.

The project uses [Poetry](https://python-poetry.org/) as Python dependency manager and the dependencies are declared in `pyproject.toml`.

1. Follow [Creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) to create your own repository.
2. Clone the newly created repository on the WSL local machine.
3. `poetry install` create a virtual environment and install the Python packages
4. `poetry shell` activate the virtual environment in the terminal 

## 🎯 Organize the code

You are responsible for organizing your code directories clearly and explicitly (source and test files, CI/CD workflow...).

## 🎯 Set up the CI/CD

Throughout the assessment, design step by step a CI/CD workflow using Github actions to automatically:
- build the Docker image of the lambda function
- check coding rules with ruff
- test and measure test coverage with pytest and pytest-cov
- invoke the lambda function locally using the SAM CLI and check its response as integration test. 
- ...

## 🎯 Develop the Lambda function entrypoint

The Python source directory is `lambda_app`.
Fill the lambda entry point `lambda_handler` to process the string message received as input and sent back the processed message.
The `events` directory contains sample event files that can be received by the lambda function.
You are also responsible for developing the corresponding unit tests.

## 🎯 Check coding rules and test the Lambda function

Coding rules are checked with `ruff` (coding rules are set in `pyproject.toml`).
Unit testing is run by `pytest` and code coverage with `pytest-cov`.

```bash
ruff check .
pytest --cov-report term-missing --cov=lambda_app python/test/dir
```

You are responsible for developing a Python code having the highest possible test coverage score and having the lowest possible coding rules errors/warnings.

## 🎯 Build the application
Fill the `Dockerfile` to package your lambda function using the base image `public.ecr.aws/lambda/python:3.12`.

Write a bash command to build the image from the `Dockerfile`.

```bash
...
```

## 🎯 Invoke the application locally


### With SAM CLI

The [SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) can be used to build a container image compatible with the AWS Lambda service. The SAM CLI can also invoke locally the lambda function. The SAM CLI is a Python dependency of the project and therefore installed by the dependency manager Poetry.

Write a small bash script to invoke with `sam` the lambda function locally with the event files of `events`. 

```bash
...
```

### With curl

Using the Docker image, write a small bash script to invoke the lambda function locally using `curl` with the event files of `events`.

```bash
...
```

## 🎯 Deploy your application in a local Kubernetes cluster

Set up a local Kubernetes cluster using [k3d](https://k3d.io/v5.7.4/) (k3d and kubectl CLI are already installed by the devcontainer configuration).

Deploy you lambda application in the cluster.

Write a small bash script to invoke the lambda function deployed in the cluster using `curl` with the event files of `events`.
```bash
...
```

Propose a solution to automate the cluster provisioning locally and the deployment of the lambda application.