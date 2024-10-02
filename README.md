# DevOps technical assessment

The goal of this technical assessment is to develop a containerized Python application that can be deployed as an AWS Lambda function, a REST API or a CLI possibly in non-AWS environment. The assessment covers several points:
- Code organisation between source, test, Continuous Integration (CI)...
- Development of a Python program to call a `process` function though the invokation of AWS Lambda function, a REST API or the execution of a CLI in the terminal.
- Configuration of a Continuous Integration pipeline using Github Actions to automate application testing and packaging.

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

## 🎯 Organize the code of the Python application

Throughout the assessment, you are responsible for organizing your code directories clearly and explicitly (source and test files, CI/CD workflow...).

## 🎯 Develop the application

The Python source directory is `lambda_app`.
Fill the lambda entry point `lambda_handler` to process the string message received as input and sent back the processed message.
The `events` directory contains sample event files that can be received by the lambda function.
You are also responsible for developing the corresponding unit tests.

## 🎯 Check coding rules and test the application

Coding rules are checked with `ruff` (coding rules are set in `pyproject.toml`).
Unit testing is run by `pytest` and code coverage with `pytest-cov`.

```bash
ruff check .
pytest --cov-report term-missing --cov=lambda_app python/test/dir
```

You are responsible for developing a Python code having the highest possible test coverage score and having the lowest possible coding rules errors/warnings.

## 🎯 Set up the CI/CD

Design a CI/CD workflow using Github actions to automatically:
- check coding rules with ruff
- test and measure test coverage with pytest and pytest-cov
- build the Docker image of the lambda function
- invoke the lambda function locally using the SAM CLI and check its response as integration test. 

You are responsible for providing a working CI/CD with 'success' status on the final commit.

## 🎯 Build the application
Fill the `Dockerfile` to package your lambda function using the base image `public.ecr.aws/lambda/python:3.12`.

Write a bash command to build the image from the `Dockerfile`.

```bash
...
```

## 🎯 Invoke the application locally


### With SAM CLI

The [SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) can be used to build a container image compatible with the AWS Lambda service. The SAM CLI can also invoke locally the lambda function. The SAM CLI is a Python dependency of the project and therefore installed by the dependency manager Poetry.

Write a small bash script to invoke wtih `sam` the lambda function locally with the event files of `events`. 

```bash
...
```

### With Docker as a CLI

Using the Docker image, write a small bash script to run the CLI locally with an input message `hello`.

```bash
...
```

### With curl

Using the Docker image, write a small bash script to invoke the lambda function locally using `curl`.

```bash
...
```

