# PyQuiz

PyQuiz is a console-based quiz application built in Python as part of the GIK36R software testing project. The project focuses on modular design, dependency injection, unit testing, mocking, GitHub workflow, and testing documentation.

## Project Structure

- `src/` contains the application source code
- `tests/` contains unit tests
- `docs/` contains project documentation and the GitHub Pages content

## Main Features

- multiple-choice quiz questions
- score handling
- randomized question order
- invalid input handling
- console-based user interface

## Requirements

- Python 3.13 or compatible Python 3 version
- PowerShell or another terminal

## Setup

Create and use a virtual environment if needed:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## Run the Application

From the `pyquiz` folder:

```powershell
.\.venv\Scripts\python.exe -m src.main
```

## Run the Tests

From the `pyquiz` folder:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests
```

## Documentation

Project documentation is available in the `docs/` folder, including:

- project charter
- user stories
- test strategy
- test plan
- test cases
- test report
- coverage report
- complexity report
- lessons learned

## GitHub Pages

The repository includes a simple GitHub Pages site built from the `docs/` folder. It is used as a lightweight project overview and documentation entry point. The application itself is still a console program, not a web application.

## Course

Course: GIK36R  
Project type: Software Testing Project
