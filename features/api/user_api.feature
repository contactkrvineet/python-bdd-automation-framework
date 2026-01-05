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

  @smoke @api @post
  Scenario: Create a new user
    Given base api url is "https://api.vineetkr.com"
    And I have a valid authentication token
    When I send a POST request to "/api/users" with body
      """
      {
        "name": "Vineet Kr Test",
        "email": "vineet.test.{timestamp}@gmail.com",
        "age": 9
      }
      """
    Then the response status code should be 201
    And the response field "success" should be true
    And the response should contain field "data"
    And the response data should contain field "name"
    And the response data should contain field "email"

  @smoke @api @post @delete
  Scenario: Create and delete a user
    Given base api url is "https://api.vineetkr.com"
    And I have a valid authentication token
    When I send a POST request to "/api/users" with body
      """
      {
        "name": "Temp User",
        "email": "temp.user.{timestamp}@vineetkr.com",
        "age": 25
      }
      """
    Then the response status code should be 201
    And the response field "success" should be true
    And capture response data field "_id" as "user_id"
    When I send a DELETE request to "/api/users/{user_id}"
    Then the response status code should be 200
    And the response field "success" should be true
