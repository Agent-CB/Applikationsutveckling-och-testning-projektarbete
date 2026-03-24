# Lessons Learned

## What Went Well
- the project structure became clearer after separating `src/` and `tests/`
- dependency injection made the quiz engine easier to test
- small modules such as `AnswerParser` and `ResultFormatter` improved testability
- unit tests helped verify behavior quickly after changes

## Challenges
- Python environment setup caused delays before testing could run
- Git safe-directory issues appeared because the repository was initialized in a sandboxed environment
- GitHub Pages created confusion because the project is a console app, not a web application

## What We Learned
- how to structure a small Python project for testing
- how to use `unittest` and `unittest.mock`
- how to isolate dependencies in tests
- how to connect user stories to test cases and modules
- how to use GitHub for commits, branches, and pull requests

## What We Would Improve Next Time
- create the documentation earlier in the project
- use pull requests from the beginning
- add coverage and complexity reporting
- expand the application with file-based question loading or richer result reporting
