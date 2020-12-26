Feature: testing the sqrt route "endpoint"
    
    Scenario: should return right square root
	    Given we have assinged number variable with 9.0
        When we run the sqrt endpoint 
        Then it will return 3.0
    