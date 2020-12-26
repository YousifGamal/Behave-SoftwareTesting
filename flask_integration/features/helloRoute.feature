Feature: testing the hello route "endpoint"

    Scenario: should return right welcome message
	    Given we have assinged name variable with muhammad
        When we run the hello endpoint 
        Then it will return hello muhammad