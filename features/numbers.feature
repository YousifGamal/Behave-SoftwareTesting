Feature: Numbers Calculator
Scenario: Add two numbers
  Given A and B
  When add A and B
  Then result is A+B 
  
  
Scenario: Subtract two numbers
    Given A and B:
    """
        Given two integer number A and B, 
        Test the subtract function on them 
        and compare the expected output
        with the actual output
    """
    When subtract A and B
    Then result is A-B

Scenario: Merge two lists in ascending order
    Given A and B lists:
        | a  | b  |
        | 0  | 1  |
        | 2  | 3  |
        | 4  | 5  |
    When Merge A, B with working function
    Then we get list C sorted:
        | C   |
        | 0   |
        | 1   |
        | 2   |
        | 3   |
        | 4   |
        | 5   |
        
    Given A and B lists:
        | a  | b  |
        | 0  | 1  |
        | 2  | 3  |
        | 4  | 5  |
    When Merge A, B with wrong function
    Then we get list C sorted:
        | C   |
        | 0   |
        | 1   |
        | 2   |
        | 3   |
        | 4   |
        | 5   |
        
Scenario: Get total sum of two integer lists' elements
    Given A and B lists:
        | a  | b  |
        | 0  | 1  |
        | 2  | 3  |
        | 4  | 5  |
    When Sum elements in A and B
    Then total sum is 15
    
    Given A and B lists:
        | a  | b  |
        | 0  | 1  |
        | 2  | 3  |
        | 4  | 5  |
    When Sum elements in A and B
    Then total sum is 11
    
Scenario: Get minimum number in two lists
    Given A and B lists:
        | a  | b  |
        | 0  | 1  |
        | 2  | 3  |
        | 4  | 5  |
    When Merge A, B with working function
    And Get the minimum number
    Then minimum number is 0
    
    
    Given A and B lists:
        | a  | b  |
        | 0  | 1  |
        | 2  | 3  |
        | 4  | 5  |
    When Merge A and B then get the minimum number
    Then minimum number is 0
