Feature: Decorator

  Scenario: Create a new decorated function
    Given a new empty state
      And a dummy chain function
      And a mocked decorated chain function
     When I run the chain
     Then the mocked should have been called
