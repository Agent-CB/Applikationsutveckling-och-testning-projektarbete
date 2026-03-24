# Test Strategy

## Purpose
The purpose of this strategy is to describe how the PyQuiz project is tested and which methods, tools, and priorities are used.

## Test Objectives
- verify that the quiz application behaves correctly from start to finish
- verify that score handling works as expected
- verify that invalid input is handled safely
- verify that question retrieval and question ordering work correctly
- verify isolated behavior of modules by using mocking where suitable

## Test Levels
- Unit testing is the primary test level in this project
- Manual functional testing is used to confirm that the console application can be run from the terminal

## Test Types
- functional testing
- input validation testing
- dependency-isolated testing with mocks
- basic integration through manual execution of the main program

## In Scope
- `Question`
- `QuestionRepository`
- `AnswerParser`
- `ScoreService`
- `RandomService`
- `QuestionOrderService`
- `ResultFormatter`
- `QuizEngine`
- `main.py` manual startup verification

## Out of Scope
- performance testing
- security testing
- database testing (not applicable, as the application does not use a database)

## Test Approach
- use `unittest` as the unit testing framework
- use `unittest.mock` to isolate dependencies
- run tests locally in the Python virtual environment using `python -m unittest discover`
- manually run the application from the terminal to verify the console flow

## Entry Criteria
- source code is committed locally
- virtual environment is available
- project dependencies are available

## Exit Criteria
- all planned unit tests pass
- no blocking defects remain in the tested functionality
- documentation and implementation are verified to be aligned through code review

## Tools
- Python 3
- `unittest`
- `unittest.mock`
- GitHub

## Risks
- documentation may describe behavior not implemented in code
- random behavior can make tests unstable if not isolated; mitigate by using mocks for randomness in tests
- console-based behavior must be validated carefully
