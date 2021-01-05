Feature: Test for Check_Solution() function

  Scenario Outline: check if colors satisfies graph <graphs> constraints
    Given graph nodes colors is <colors> and adjacency matrix is <graphs>
    When I check for solution
    Then It returns <result>

    Examples: Check_Solution
        | colors    | graphs                                   | result    |
        | 0,1,2     | 0, 1, 1 - 1, 0, 1 - 1, 1, 0              | True      |
        | 2, 2, 0, 1     | 0, 0, 1, 1 - 0, 0, 1, 1 - 1, 1, 0, 1 - 1, 1, 1, 0              | True      |
        | 1     | 0              | True     |
  
