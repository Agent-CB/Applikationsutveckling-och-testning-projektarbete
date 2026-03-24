# Test Report

## Project
PyQuiz

## Test Summary
The project was tested using automated unit tests and manual execution of the console application. The goal was to verify the core quiz flow, score handling, input validation, question retrieval, and question ordering.

## Test Execution
Automated test command:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests
```

## Latest Result
- Total tests executed: 17
- Passed: 17
- Failed: 0
- Result: PASS

## Covered Areas
- answer parsing
- question ordering
- question repository behavior
- quiz engine behavior
- score handling
- result formatting
- random service bounds

## Manual Verification
Manual startup command:

```powershell
.\.venv\Scripts\python.exe -m src.main
```

Observed behavior:
- the application starts in the console
- questions and answer options are shown
- user input is accepted
- correct and wrong answers are handled
- final score is shown

## Defects Found
- initial environment issues with Python setup were resolved by creating a local virtual environment
- GitHub Pages was not applicable because the project is a console application and not a website

## Conclusion
The tested implementation satisfies the currently implemented user stories for the console quiz application. No blocking defects remain in the tested functionality.
