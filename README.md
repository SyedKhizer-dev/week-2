# Python Calculator — CI Pipeline

## Overview

A simple Python calculator that supports addition, subtraction, and multiplication of positive integers. The project includes unit tests, Docker-based test execution, and continuous integration using GitHub Actions.

## Tech Stack

- Python 3.13
- Unit testing with `unittest`
- Docker
- Git and GitHub
- GitHub Actions

## Project Structure

```text
week-2/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app/
│   ├── __init__.py
│   └── calculator.py
├── tests/
│   ├── __init__.py
│   └── test_calculator.py
├── .gitignore
├── Dockerfile
└── README.md
```

## Run Locally

Ensure Python 3.13 or a compatible Python 3 version is installed.

Run the unit tests:

```bash
python -m unittest discover -s tests -v
```

## Run Tests Using Docker

Build the Docker image:

```bash
docker build -t calculator-app:test .
```

Run the tests inside the container:

```bash
docker run --rm calculator-app:test
```

## Continuous Integration

The GitHub Actions workflow in `.github/workflows/ci.yml` automatically:

1. Checks out the repository.
2. Builds the Docker image.
3. Runs the unit tests inside the Docker container.

The workflow runs on pushes to the `main` branch and can also be triggered manually.

## Expected Result

The unit tests should pass successfully. If a build or test fails, GitHub Actions reports the workflow failure.

## Scope

This version covers the Python calculator, unit testing, Docker, and CI. AWS deployment and infrastructure configuration are excluded from the current submission scope.