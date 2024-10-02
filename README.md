# DevOps technical assessment

The goal of this technical assessment is to develop a containerized Python application that can be deployed as an AWS Lambda function, a REST API or a CLI possibly in non-AWS. The assessment covers several points:
- Code organisation between source, test, Continuous Integration (CI)...
- Development of a Python program to call a `process` function though the invokation of AWS Lambda function, the call to a REST API or the execution of a CLI in the terminal.
- Configuration of a Continuous Integration pipeline using Github Actions to automate application testing and packaging.

## Create a repository from this template

Recommended configuration:
- Windows 10/11 machine with [Windows Subsystem for Linux](https://learn.microsoft.com/fr-fr/windows/wsl/install) (WSL) feature enabled.
- VSCode editor installed on Windows and running on WSL (aka the 'local' machine in the following).
- Git installed on WSL.

The development environment can be reproduced with the [Devcontainer](https://code.visualstudio.com/docs/devcontainers/containers) feature of VSCode based on the `.devcontainer/devcontainer.json` file of the repo.

The project uses [Poetry](https://python-poetry.org/) as dependency manager and the dependencies are declared in `pyproject.toml`.

1. Follow [Creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) to create your own repository.
2. Clone the newly created repository on the WSL local machine.
3. `poetry install` create a virtual environment and install the Python packages
4. `poetry shell` activate the virtual environment in the terminal 

## Organize the code of the Python application

The Python source directory is `lambda_app`.
The `aws_lambda_events` contains a sample event file that can be received by the lambda function.

Throughout the assessment, you are responsible for organizing your code directories clearly and explicitly (test files, CI/CD workflow...)


## Check coding rules and test the application

Coding rules are checked with `ruff` (coding rules are set in `pyproject.toml`).
Unit testing is run by `pytest` and code coverage with `pytest-cov`.

```bash
ruff check .
pytest --cov-report term-missing --cov=lambda_app python/test/dir
```

You are responsible for developing a code having the highest possible test coverage score and having the lowest possible coding rules errors/warnings.

## Set up the CI/CD

Design a CI/CD workflow using Github actions to automatically:
- check coding rules with ruff
- test and measure test coverage with pytest and pytest-cov
- build the Docker image of the lambda function
- invoke the lambda function locally and check its response. 

You are responsible for providing a working CI/CD with 'sucess' status on the final commit?

## Build the application

## Invoke the application

### With SAM CLI locally

### With curl or AWS CLI

### With Docker as a CLI

Write a bash command using `docker run` to run the CLI with an input message `hello`.