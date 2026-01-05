Feature: User Login Functionality
  As a user
  I want to log into the application
  So that I can access my account

  Background:
    Given I am on the login page

  @smoke @ui @positive
  Scenario: Successful login with valid credentials
    When I enter username "testuser@example.com"
    And I enter password "TestPass123"
    And I click the login button
    Then I should be redirected to the dashboard
    And I should see the welcome message

  @ui @negative
  Scenario: Login fails with invalid password
    When I enter username "testuser@example.com"
    And I enter password "wrongpassword"
    And I click the login button
    Then I should see an error message "Invalid credentials"
    And I should remain on the login page

  @ui @negative
  Scenario: Login fails with empty username
    When I enter username ""
    And I enter password "TestPass123"
    And I click the login button
    Then I should see an error message "Username is required"

  @ui @negative
  Scenario: Login fails with empty password
    When I enter username "testuser@example.com"
    And I enter password ""
    And I click the login button
    Then I should see an error message "Password is required"

  @ui @negative
  Scenario Outline: Login with various invalid credentials
    When I enter username ""
    And I enter password ""
    And I click the login button
    Then I should see an error message ""

    Examples:
      | username              | password    | error_message           |
      | invalid@example.com   | TestPass123 | Invalid credentials     |
      | testuser@example.com  | short       | Invalid credentials     |
      | notanemail            | TestPass123 | Invalid email format    |