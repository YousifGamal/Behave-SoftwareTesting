Feature: Float Addition Failed
Scenario:
  Given Int A = 5, B = 2
  When A plus B
  Then result = 7

Scenario:
  Given Int A = 5.5, B = 2.5
  When A plus B
  Then result = 8