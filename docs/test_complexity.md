# Code Complexity Analysis

## Overview
This documentation describes the code complexity analysis for the project using the Lizard tool.

## Lizard Tool
Lizard is a static code analysis tool that measures code complexity metrics across multiple programming languages. It analyzes:

- **Cyclomatic Complexity**: Measures the number of independent paths through code
- **Lines of Code (LOC)**: Counts the physical lines of code
- **Function Length**: Tracks the number of lines per function
- **Parameter Count**: Identifies functions with excessive parameters

## Analysis Target
- **Source Directory**: `src/`
- **Tool**: Lizard static analysis

## Metrics Interpretation

### Cyclomatic Complexity
- **1-5**: Low complexity (good)
- **6-10**: Moderate complexity (acceptable)
- **11+**: High complexity (consider refactoring)

## Results
Run `lizard src` from the project root to generate complexity metrics for all source files.
 lizard src
================================================
  NLOC    CCN   token  PARAM  length  location  
------------------------------------------------
       8      3     33      3      10 parse@2-11@src/answer_parser.py
       2      1     11      2       2 show_text@2-3@src/console_ui.py
       2      1      9      1       2 read_input@5-6@src/console_ui.py
       2      1     12      2       2 __init__@2-3@src/question_order_service.py
       9      2     67      2      11 order_questions@5-15@src/question_order_service.py
       4      1     26      4       4 __init__@2-5@src/question.py
       2      1     13      2       2 is_correct@7-8@src/question.py
      10      1     54      1      10 get_questions@5-14@src/question_repository.py
       2      1     18      2       2 next@5-6@src/random_service.py
      17      1     62      0      18 main@21-38@src/main.py
       2      1     10      1       2 __init__@2-3@src/score_service.py
       2      1     10      1       2 add_point@5-6@src/score_service.py
       2      1      9      1       2 get_score@8-9@src/score_service.py
       2      1     10      1       2 reset@11-12@src/score_service.py
      15      1     48      7      15 __init__@2-16@src/quiz_engine.py
      22      5    189      1      27 start@18-44@src/quiz_engine.py
       2      1     11      2       2 question_text@2-3@src/result_formatter.py
       2      1     12      3       2 option_text@5-6@src/result_formatter.py
       2      1      7      1       2 invalid_input@8-9@src/result_formatter.py
       2      1      7      1       2 correct_answer@11-12@src/result_formatter.py
       2      1      7      1       2 wrong_answer@14-15@src/result_formatter.py
       2      1     10      2       2 final_score@17-18@src/result_formatter.py
11 file analyzed.
==============================================================
NLOC    Avg.NLOC  AvgCCN  Avg.token  function_cnt    file
--------------------------------------------------------------
      9       8.0     3.0       33.0         1     src/answer_parser.py
      5       2.0     1.0       10.0         2     src/console_ui.py
     12       5.5     1.5       39.5         2     src/question_order_service.py
      7       3.0     1.0       19.5         2     src/question.py
      0       0.0     0.0        0.0         0     src/__init__.py
     12      10.0     1.0       54.0         1     src/question_repository.py
      4       2.0     1.0       18.0         1     src/random_service.py
     37      17.0     1.0       62.0         1     src/main.py
      9       2.0     1.0        9.8         4     src/score_service.py
     38      18.5     3.0      118.5         2     src/quiz_engine.py
     13       2.0     1.0        9.0         6     src/result_formatter.py

===============================================================================================================
No thresholds exceeded (cyclomatic_complexity > 15 or length > 1000 or nloc > 1000000 or parameter_count > 100)
==========================================================================================
Total nloc   Avg.NLOC  AvgCCN  Avg.token   Fun Cnt  Warning cnt   Fun Rt   nloc Rt
------------------------------------------------------------------------------------------
       146       5.2     1.3       28.9       22            0      0.00    0.00