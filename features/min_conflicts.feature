Feature: Test for Min_Conflicts() function

  Scenario Outline: check if Min_Conflicts function find soluton for this graph <graphs>
    Given graph nodes colors is <colors> and adjacency matrix is <graphs>
    When I call Min_Conflicts with k <k>
    Then It returns <result>

    Examples: Factorial
        | colors         | graphs                       |k            | result    |
        | 0,1,2          | 0, 1, 1 - 1, 0, 1 - 1, 1, 0  |3             | True      |
        | 0,1,1          | 0, 1, 1 - 1, 0, 1 - 1, 1, 0  |2             | False      |
        | 2, 2, 1, 1     | 0, 0, 1, 1 - 0, 0, 1, 1 - 1, 1, 0, 1 - 1, 1, 1, 0  |3              | True      |
        | 1     | 0      |3        | True     |
  
