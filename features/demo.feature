
  Feature: Login feature
    Scenario: Default login scenario
      Given open website
      And enter user id
      And enter password
      When click on submit button
      Then verify the user dashboard


    Scenario: Login with different credential
      Given open website
