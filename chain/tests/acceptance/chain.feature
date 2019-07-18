Feature: Chain

  Scenario: Common Usage
    Given a new empty state
      And a decorated chain function without output
      And a decorated chain function with output
     When I run the chain
     Then the first result must have the desired output

  Scenario: Run a chain
    Given a new empty state
      And a dummy chain function
      And a random number of static chains
     When I run the chain
     Then the first result context must be my initial state

  Scenario: Direct function call
    Given a decorated chain function with output
     When I run the first function on the chain directly
     Then the direct call result must match the output

  Scenario: Get the output from a chain
    Given a new empty state
      And a dummy chain function
      And a random number of static chains
      And a new chain with mocked function
      And add a return value to the mocked function
     When I run the chain
     Then the first result must have the desired output

  Scenario: Run an odd chain
    Given a new empty state
      And an odd random number of static chains
     When I run the chain
     Then the first result context must be my initial state

  Scenario: Run a single function chain
    Given a new empty state
      And a single static chain
     When I run the chain
     Then the first result context must be my initial state

  Scenario: Passing args to next function
    Given a new empty state
      And a new chain with mocked function
      And add an arg return value to the mocked function
      And a new chain with mocked function
     When I run the chain
     Then the mocked function should have been called with correct data

  Scenario: Reversed chain
    Given a new empty state
      And a dummy chain function
      And a random number of static chains
      And a new chain with mocked function
      And a new chain returning random autoincremented data
     When I run the chain
      And I reverse the chain
      And I reset the state
      And I add a counter on the current state
      And I run the chain
     Then the context should not persist data
