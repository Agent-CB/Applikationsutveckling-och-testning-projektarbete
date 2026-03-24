# User Stories

## User Story 1 - Show Question
As a player, I want to see a question with multiple answer options so that I can play the quiz.

### Acceptance Criteria
- A question is displayed in the console
- Multiple answer options are displayed
- Only one option is correct

## User Story 2 - Select Answer
As a player, I want to choose one of the available options so that the game can determine whether my answer is correct.

### Acceptance Criteria
- The player can enter an answer
- The input is validated
- The system determines whether the answer is correct or incorrect

## User Story 3 - Score Handling
As a player, I want the game to keep track of my score so that I can see how well I performed.

### Acceptance Criteria
- The score increases when the answer is correct
- The score does not increase when the answer is wrong
- The final score is displayed at the end

## User Story 4 - Retrieve Questions
As a system, I want to retrieve questions from a repository so that the quiz can use them during gameplay.

### Acceptance Criteria
- The repository returns a list of questions
- The repository works independently of the UI
- The repository can be mocked in tests

## User Story 5 - Randomize Question Order
As a player, I want the questions to appear in varying order so that the quiz feels less repetitive.

### Acceptance Criteria
- Question order can be shuffled
- The same question is not shown twice in the same round
- The random behavior can be isolated in tests

## User Story 6 - Show Result
As a player, I want to see my result at the end so that I know how many points I got.

### Acceptance Criteria
- The final score is displayed
- The result is shown in the console

## User Story 7 - Handle Invalid Input
As a system, I want to handle invalid input so that the program does not crash.

### Acceptance Criteria
- Invalid input produces an error message
- The program continues to the next question
- Invalid input does not give points

## Traceability Matrix

| User Story | Test Cases | Modules |
|---|---|---|
| US1 - Show Question | TC1, TC2 | `QuizEngine`, `ConsoleUI`, `ResultFormatter` |
| US2 - Select Answer | TC3, TC4 | `AnswerParser`, `QuizEngine` |
| US3 - Score Handling | TC5, TC6 | `ScoreService`, `QuizEngine` |
| US4 - Retrieve Questions | TC7 | `QuestionRepository`, `Question` |
| US5 - Randomize Question Order | TC8, TC9 | `QuestionOrderService`, `RandomService` |
| US6 - Show Result | TC10 | `QuizEngine`, `ResultFormatter`, `ConsoleUI` |
| US7 - Handle Invalid Input | TC11, TC12 | `AnswerParser`, `QuizEngine` |
