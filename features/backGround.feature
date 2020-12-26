@wip
Feature: background

Background: Same numbers for two Scenarios
  Given A = 2 and B = 2
@add
Scenario: Add two numbers
  When A + B
  Then result is 4
@divide
Scenario: divide two numbers 
  When A / B
  Then result is 1



