# Test Cases

## TC1 - Display Question Text
**Related User Story:** US1  
**Precondition:** Quiz contains at least one question  
**Steps:**
1. Start the quiz
2. Observe console output

**Expected Result:**
- The question text is displayed

## TC2 - Display Answer Options
**Related User Story:** US1  
**Precondition:** Quiz contains at least one question with options  
**Steps:**
1. Start the quiz
2. Observe the answer options shown in the console

**Expected Result:**
- Answer options are displayed with indexes

## TC3 - Accept Valid Numeric Input
**Related User Story:** US2  
**Precondition:** A question is shown  
**Steps:**
1. Enter a valid option number

**Expected Result:**
- The input is parsed into a valid answer index

## TC4 - Determine Correct or Wrong Answer
**Related User Story:** US2  
**Precondition:** A question is shown  
**Steps:**
1. Enter an answer
2. Let the quiz evaluate it

**Expected Result:**
- The system determines whether the answer is correct or wrong

## TC5 - Increase Score After Correct Answer
**Related User Story:** US3  
**Precondition:** Score is zero  
**Steps:**
1. Answer a question correctly

**Expected Result:**
- Score increases by one

## TC6 - Do Not Increase Score After Wrong Answer
**Related User Story:** US3  
**Precondition:** Score is zero  
**Steps:**
1. Answer a question incorrectly

**Expected Result:**
- Score remains unchanged

## TC7 - Retrieve Questions From Repository
**Related User Story:** US4  
**Precondition:** Repository is initialized  
**Steps:**
1. Call `get_questions()`

**Expected Result:**
- A non-empty list of questions is returned

## TC8 - Shuffle Question Order
**Related User Story:** US5  
**Precondition:** Repository contains multiple questions  
**Steps:**
1. Order questions through `QuestionOrderService`

**Expected Result:**
- Questions are returned in a valid ordered list

## TC9 - Keep Same Question Set After Shuffle
**Related User Story:** US5  
**Precondition:** Repository contains multiple questions  
**Steps:**
1. Order questions through `QuestionOrderService`
2. Compare input and output question sets

**Expected Result:**
- No questions are lost or duplicated

## TC10 - Show Final Score
**Related User Story:** US6  
**Precondition:** Quiz is completed  
**Steps:**
1. Finish the quiz

**Expected Result:**
- Final score is displayed in the console

## TC11 - Handle Non-Numeric Input
**Related User Story:** US7  
**Precondition:** A question is shown  
**Steps:**
1. Enter invalid text such as `abc`

**Expected Result:**
- An invalid input message is shown
- The program continues

## TC12 - Handle Out-of-Range Input
**Related User Story:** US7  
**Precondition:** A question is shown  
**Steps:**
1. Enter a number outside the valid range

**Expected Result:**
- The input is rejected
- The program continues without crashing
