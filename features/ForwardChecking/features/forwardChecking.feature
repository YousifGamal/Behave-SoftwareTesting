Feature: Forward Checking
   
Scenario: Test Forward Checking
    Given the following graph with N = 5:
        | N0 | N1 | N2 | N3 | N4 | N5 |
        | 0 | 1  | 1 | 0 | 0 | 0 |
        | 1 | 0  | 0 | 1 | 1 | 0 |
        | 1 | 0  | 0 | 0 | 0 | 1 |
	    | 0 | 1  | 0 | 0 | 1 | 1 |
	    | 0 | 1  | 0 | 1 | 0 | 1 |
        | 0 | 0  | 1 | 1 | 1 | 0 |
    When Test the graph with the forward checking
    Then we check that the colors assigned to each node:
        | Colors |
        | 0 |
        | 1 |
        | 2 |
        | 0 |
        | 2 |
        | 1 |
