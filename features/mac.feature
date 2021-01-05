Feature: testing mac algorithm

Scenario: Test removeConflicting function
    Given 2 nodes and 1 colors:
    """
        No solution will exist because
        there is only one color
        for two connected nodes
    """
    When removing the conflicting colors
    Then No solution exist
    
Scenario: Test arcConsistency function
    Given 2 nodes and 2 colors but the second has only one available color
    When applying arc consistency
    Then node 1 has only one available color
    
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
        
        