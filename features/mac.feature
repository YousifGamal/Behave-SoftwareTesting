Feature: testing mac algorithm

Scenario: 3 nodes and 2 colors
    Given this graph n = 3, c = 2:
        | n0  | n1 | n2|
        | 0   | 1  | 1 | 
        | 1   | 0  | 1 |
        | 1   | 1  | 0 |
    When coloring the map with mac algo
    Then mac solution is:
        | C   |
        | 0   |
        | 0   |
        | 0   |
    
Scenario: 3 nodes and 3 colors
    Given this graph n = 3, c = 3:
        | n0  | n1 | n2|
        | 0   | 1  | 1 | 
        | 1   | 0  | 1 |
        | 1   | 1  | 0 |
    When coloring the map with mac algo
    Then mac solution is:
        | C   |
        | 1   |
        | 2   |
        | 3   |
    
    
Scenario: 4 nodes and 3 colors
    Given this graph n = 4, c = 3:
        | n0  | n1 | n2| n3|
        | 0   | 1  | 1 | 0 |
        | 1   | 0  | 1 | 1 |
        | 1   | 1  | 0 | 1 |
        | 0   | 1  | 1 | 0 |
    When coloring the map with mac algo
    Then mac solution is:
        | C   |
        | 1   |
        | 2   |
        | 3   |
        | 1   |
        
Scenario: 6 nodes and 3 colors
    Given this graph n = 6, c = 3:
        | n0  | n1 | n2| n3| n4| n5|
        | 0   | 0  | 1 | 0 | 1 | 1 |
        | 0   | 0  | 1 | 0 | 1 | 0 |
        | 1   | 1  | 0 | 1 | 1 | 1 |
        | 0   | 0  | 1 | 0 | 0 | 1 |
        | 1   | 1  | 1 | 0 | 0 | 0 |
        | 1   | 0  | 1 | 1 | 0 | 0 |
    When coloring the map with mac algo
    Then mac solution is:
        | C   |
        | 1   |
        | 1   |
        | 2   |
        | 1   |
        | 3   |
        | 3   |
        
        