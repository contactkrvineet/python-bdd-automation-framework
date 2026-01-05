# File: `features/api/user_api.feature`
Feature: User API Operations
  As an API client
  I want to perform CRUD operations on users
  So that I can manage user data

  @smoke @api @get
  Scenario: Get list of users
    Given base api url is "https://api.vineetkr.com"
    And I have a valid authentication token
    When I send a GET request to "/api/users"
    Then the response status code should be 200
    And the response should be an array
    And the response array should not be empty
    And the response should contain field "email"
