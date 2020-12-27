Feature: Step Parameters

  Scenario: Get the biggest number
    Given I have a list of 5,10,9,7,8
    When  I call max on them
    Then  It should be 10

  Scenario: Get the smallest number
    Given I have a list of 5,10,9,7,8
    When  I call min on them
    Then  It should be 5
