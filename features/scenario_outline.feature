Feature: Scenario Outline

  Scenario Outline: Get Factorial for <number>
    Given number <number>
    When I calculate Factorial
    Then It should be <result>

    Examples: Factorial
        | number         | result |
        | 0              | 1      |
        | 2              | 2      |
        | 3              | 6      |
        | 4              | 24     |
        | 5              | 120    |
        | 6              | 720    |
        | 7              | 5040   |
