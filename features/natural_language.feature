Feature: Divide or Not 

    When dividing a number the divisor should not be zero,
    So we have to decide if we can make the division or not
    based on the divisor value.

    Scenario: Number is not Zero
        Given the number is ten
        When the divisor is two
        Then we complete the division

    Scenario: Number is Zero
        Given the number is ten
        When the divisor is zero
        Then we skip the division
