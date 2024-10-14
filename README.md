# DevOps technical assessment

The goal of this technical assessment is to package a small Python function as an AWS Lambda and to deploy it in a local Kubernetes cluster. The assessment covers several points:
- Development of the AWS Lambda entrypoint in Python to be invoked as an AWS Lambda function or via an HTTP request.
- Automatic deployment of the function in a local Kubernetes cluster with application monitoring.
- Configuration of a Continuous Integration workflows using Github Actions to automate testing, packaging and deployment.
- Code organization between source, test, Continuous Integration (CI) workflows, Kubernetes manifest files...

There is no good answer to this technical assessment. Your are free to use any tool to build your solution.

## Create a repository from this template

Recommended configuration:
- Windows 10/11 machine with [Windows Subsystem for Linux](https://learn.microsoft.com/fr-fr/windows/wsl/install) (WSL) feature enabled.
- VSCode editor installed on Windows and running on WSL (aka the 'local' machine in the following).
- Git installed on WSL.
- Docker installed on WSL. We strongly advise to not use the Windows version of Docker.

The development environment can be reproduced with the [Devcontainer](https://code.visualstudio.com/docs/devcontainers/containers) feature of VSCode based on `.devcontainer/devcontainer.json`.

The project uses [Poetry](https://python-poetry.org/) as Python dependency manager and the dependencies are declared in `pyproject.toml`.

1. Follow [Creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) to create your own repository.
2. Clone the newly created repository on the WSL local machine.
3. `VSCode > Dev Containers: Open in container` to initialize automatically the development environement with Python, Docker in Docker...

## 🎯 Organize the code

You are responsible for organizing your code directories clearly and explicitly (source and test files, CI/CD workflow...).

## 🎯 Set up the CI/CD

Throughout the assessment, design step by step a CI/CD workflow using Github actions to automatically:
- build the Docker image of the lambda function
- check coding rules with ruff (already included in the base workflow)
- test and measure test coverage with pytest and pytest-cov  (already included in the base workflow)
- invoke the lambda function locally using `curl` and check its response as integration test. 
- provision the local Kubernetes cluster and deploy the lambda function when the code is updated
- ...

The CI/CD is initialized with a minimal workflow implementing the check of coding rules and the test of the lambda function.

## 🎯 Develop the Lambda function entrypoint

The Python source directory is `lambda_app`.
Fill the lambda entry point `lambda_handler` to process the string message received as input and sent back the processed message.
The `events` directory contains sample event files that can be received by the lambda function.
You are also responsible for developing the corresponding unit tests (we advise to use `pytest`).

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

## 🎯 Check the local invokation of the application

### With curl

Using the Docker image and the small bash script below, check the lambda function can be invoked locally using `curl` with the event files of `events`.

```bash
docker run -p 3001:8080 ${DOCKER_IMAGE}:latest

curl -d @events/event.json  http://localhost:3001/2015-03-31/functions/function/invocations
```

Propose a solution to automate the check of the response of `curl` in the CI.

## 🎯 Deploy your application in a local Kubernetes cluster

Set up a local Kubernetes cluster using [k3d](https://k3d.io/v5.7.4/) (k3d and kubectl CLI are already installed by the devcontainer configuration).

Deploy you lambda application in the cluster.

**Hints**
1. you can create a local Kubernetes cluster with the following command:
```
k3d cluster create ${CLUSTER} \
    --registry-create ${CLUSTER}:${CLUSTER_REGISTRY_PORT} \ # Create a Docker registry inside the cluster
    -p 5432:5432@loadbalancer # Expose a port outside the cluster (e.g. the Lambda port)
```

2. you can push a Docker image from WSL to the internal cluster registry:
```
docker tag ${DOCKER_IMAGE} localhost:${CLUSTER_REGISTRY_PORT}/${DOCKER_IMAGE} && docker push localhost:${CLUSTER_REGISTRY_PORT}/${DOCKER_IMAGE}
```

Write a small bash script to invoke the lambda function deployed in the cluster using `curl` with the event files of `events`.
```bash
...
```

## 🎯 Automate Kubernetes cluster deployment and code update

Propose a solution to automate the cluster provisioning locally and the deployment of the lambda application when the code is updated.

## 🎯 Monitor your application

Propose a solution to monitor the deployed lambda application: logs and execution metrics. Include this as part of the automatic deployment.
