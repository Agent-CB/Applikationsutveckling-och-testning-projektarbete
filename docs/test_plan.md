# Test Plan

## Project
PyQuiz

## Test Items
- source modules in `src/`
- unit tests in `tests/`
- manual execution through `python -m src.main`

## Features To Be Tested
- question retrieval
- question correctness check
- score increase and reset
- answer parsing and invalid input handling
- randomized question ordering
- result formatting
- quiz execution flow

## Features Not To Be Tested
- graphical interface behavior
- persistent storage
- network communication

## Test Environment
- Windows
- PowerShell
- Python virtual environment in `.venv`
- local execution in the `pyquiz` project folder

## Test Responsibilities
- Rasim: project structure, GitHub, main startup flow
- Ahmad: requirements and traceability
- group: unit tests, execution, review, and reporting

## Schedule
1. implement core quiz modules
2. write unit tests for isolated modules
3. write tests for quiz flow with mocks
4. run manual functional checks
5. document results

## Pass Criteria
- unit tests pass
- quiz starts successfully from the terminal
- main requirements in the user stories are satisfied

## Suspension Criteria
Testing is paused if:
- the Python environment is unavailable
- the application cannot start
- major import or structure errors block execution

## Resumption Criteria
Testing resumes when:
- environment issues are solved
- application startup works again
- blocking code errors are fixed
