Feature: testing back tracking
Background: Same numbers for two Scenarios
Given colors to use
|colors|
|R     |
|G     |
|B     |
@complete
Scenario: testing complete assignment true case
Given nodes assigned values
|assignemt|
|R        |
|R        |
When check is it complete
Then complete assignmet = True
@complete
Scenario: testing complete assignment true case 2
Given nodes assigned values
|assignemt|
|B        |
|G        |
When check is it complete
Then complete assignmet = True
@complete
Scenario: testing complete assignment false case
Given nodes assigned values
|assignemt|
|R        |
|-1       |
When check is it complete
Then complete assignmet = False
@complete
Scenario: testing complete assignment false case 2
Given nodes assigned values
|assignemt|
|-1       |
|G        |
When check is it complete
Then complete assignmet = False

@consistent
Scenario: testing consistent assignemt true case
Given var = 0, and n = 3
|assignemt||n0|n1|n2|
|R        ||-1|2 |1 |
|R        ||-1|-1|-1|
|R        ||-1|-1|-1|
When check is consistent assignemt
Then consistent assignment = True
@consistent
Scenario: testing consistent assignemt true case 2
Given var = 0, and n = 3
|assignemt||n0|n1|n2|
|R        ||1 |2 |1 |
|G        ||-1|0 |-1|
|G        ||-1|-1|-1|
When check is consistent assignemt
Then consistent assignment = True
@consistent
Scenario: testing consistent assignemt false case 
Given var = 1, and n = 3
|assignemt||n0|n1|n2|
|R        ||1 |2 |1 |
|G        ||-1|0 |-1|
|G        ||-1|-1|-1|
When check is consistent assignemt
Then consistent assignment = False
@consistent
Scenario: testing consistent assignemt false case 2
Given var = 2, and n = 3
|assignemt||n0|n1|n2|
|R        ||1 |2 |1 |
|G        ||-1|0 |-1|
|G        ||-1|-1|-1|
When check is consistent assignemt
Then consistent assignment = False

@back
Scenario: testing backTracking
Given the following graph n = 6
|n0|n1|n2|n3|n4|n5|
|1 |2 |1 |2 |3 |0 |
|5 |0 |3 |4 |5 |1 |
|-1|5 |5 |5 |-1|2 |
|-1|-1|-1|-1|-1|3 |
|-1|-1|-1|-1|-1|4 |
When solve using backtracking
Then the solution is
|result|
|R     |
|G     |
|R     |
|G     |
|R     |
|B     |

@back
Scenario: testing backTracking 2
Given the following graph n = 4
|n0|n1|n2|n3|
|1 |2 |1 |2 |
|-1|0 |3 |1 |
|-1|3 |-1|-1|
When solve using backtracking
Then the solution is
|result|
|R     |
|G     |
|R     |
|B     |

