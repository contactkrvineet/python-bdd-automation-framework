# Python BDD Automation Framework - Complete Setup Guide (Updated 2025)

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Project Setup](#project-setup)
3. [File Structure](#file-structure)
4. [Step-by-Step Implementation](#step-by-step-implementation)
5. [Running Tests](#running-tests)
6. [Generating Reports](#generating-reports)

---

## Prerequisites

### Required Software
- **Python 3.8+** - [Download](https://www.python.org/downloads/)
- **pip** (comes with Python)
- **Git** - [Download](https://git-scm.com/downloads)
- **Chrome Browser** (or Firefox)
- **IDE** - VS Code, PyCharm, or any Python IDE

### Verify Installation
```bash
python --version  # Should show 3.8 or higher
pip --version
git --version
```

---

## Project Setup

### Step 1: Create Project Directory
```bash
# Create project folder
mkdir python-bdd-automation-framework
cd python-bdd-automation-framework

# Initialize git
git init
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### Step 3: Create Project Structure
```bash
# Create main directories
mkdir -p features/api features/ui features/steps
mkdir -p pages api config/environments utilities reports/allure-results reports/behave-html
mkdir -p tests logs data

# Create __init__.py files to make them packages
touch features/__init__.py pages/__init__.py api/__init__.py utilities/__init__.py tests/__init__.py

# On Windows use: type nul > features/__init__.py (and repeat for others)
```

---

## File Structure

```
python-bdd-automation-framework/
│
├── features/                           # BDD feature files
│   ├── __init__.py
│   ├── api/                           # API feature files
│   │   └── user_api.feature
│   ├── ui/                            # UI feature files
│   │   └── login.feature
│   ├── steps/                         # Step definitions
│   │   ├── __init__.py
│   │   ├── api_steps.py
│   │   └── ui_steps.py
│   └── environment.py                 # Behave hooks
│
├── pages/                             # Page Object Model
│   ├── __init__.py
│   ├── base_page.py
│   └── login_page.py
│
├── api/                               # API clients
│   ├── __init__.py
│   └── base_api_client.py
│
├── config/                            # Configuration files
│   ├── config.py
│   └── environments/
│       ├── dev.yaml
│       ├── staging.yaml
│       └── prod.yaml
│
├── utilities/                         # Helper functions
│   ├── __init__.py
│   ├── logger.py
│   ├── screenshot_helper.py
│   └── data_generator.py
│
├── reports/                           # Test reports
│   ├── allure-results/
│   └── behave-html/
│
├── tests/                             # Non-BDD pytest tests (optional)
│   └── __init__.py
│
├── logs/                              # Execution logs
│
├── data/                              # Test data files
│   └── test_data.json
│
├── requirements.txt                   # Dependencies
├── behave.ini                         # Behave configuration
├── pytest.ini                         # Pytest configuration
├── .gitignore
├── README.md
└── run_tests.sh                       # Test execution script
```

---

## Step-by-Step Implementation

### Step 4: Create requirements.txt

Your updated `requirements.txt` is already provided with latest versions.

Install dependencies:
```bash
pip install -r requirements.txt
```

### Step 5: Install Allure (for Reports)

**Windows (using Scoop):**
```bash
scoop install allure
```

**Mac:**
```bash
brew install allure
```

**Linux:**
```bash
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update
sudo apt-get install allure
```

**Verify Allure installation:**
```bash
allure --version
```

---

### Step 6: Create Configuration Files

#### config/config.py
```python
import os
import yaml
from pathlib import Path

class Config:
    # Project paths
    BASE_DIR = Path(__file__).resolve().parent.parent
    CONFIG_DIR = BASE_DIR / 'config'
    REPORTS_DIR = BASE_DIR / 'reports'
    LOGS_DIR = BASE_DIR / 'logs'
    DATA_DIR = BASE_DIR / 'data'
    
    # Browser settings
    BROWSER = os.getenv('BROWSER', 'chrome')
    HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'
    
    # Timeout settings
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 20
    PAGE_LOAD_TIMEOUT = 30
    
    # Screenshot settings
    SCREENSHOT_ON_FAILURE = True
    
    # Environment
    ENV = os.getenv('ENV', 'dev')
    
    @classmethod
    def load_environment_config(cls):
        """Load environment-specific configuration"""
        env_file = cls.CONFIG_DIR / 'environments' / f'{cls.ENV}.yaml'
        if env_file.exists():
            with open(env_file, 'r') as f:
                return yaml.safe_load(f)
        return {}
    
    @classmethod
    def get_base_url(cls):
        env_config = cls.load_environment_config()
        return env_config.get('base_url', 'https://example.com')
    
    @classmethod
    def get_api_base_url(cls):
        env_config = cls.load_environment_config()
        return env_config.get('api_base_url', 'https://api.example.com')
```

#### config/environments/dev.yaml
```yaml
environment: dev
base_url: https://dev.example.com
api_base_url: https://api-dev.example.com
credentials:
  username: testuser@example.com
  password: TestPass123
database:
  host: localhost
  port: 5432
timeout:
  api: 30
  ui: 20
```

#### config/environments/staging.yaml
```yaml
environment: staging
base_url: https://staging.example.com
api_base_url: https://api-staging.example.com
credentials:
  username: testuser@example.com
  password: TestPass123
timeout:
  api: 30
  ui: 20
```

#### config/environments/prod.yaml
```yaml
environment: prod
base_url: https://www.example.com
api_base_url: https://api.example.com
credentials:
  username: produser@example.com
  password: ProdPass123
timeout:
  api: 30
  ui: 20
```

---

### Step 7: Create Utility Files

#### utilities/logger.py
```python
import logging
import colorlog
from pathlib import Path
from datetime import datetime

class Logger:
    @staticmethod
    def get_logger(name):
        """Create and configure logger with color support"""
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        
        # Avoid adding handlers multiple times
        if logger.handlers:
            return logger
        
        # Create logs directory if not exists
        log_dir = Path(__file__).resolve().parent.parent / 'logs'
        log_dir.mkdir(exist_ok=True)
        
        # File handler
        log_file = log_dir / f'test_execution_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        
        # Console handler with colors
        console_handler = colorlog.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Formatters
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        console_formatter = colorlog.ColoredFormatter(
            '%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red,bg_white',
            }
        )
        
        file_handler.setFormatter(file_formatter)
        console_handler.setFormatter(console_formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        return logger
```

#### utilities/screenshot_helper.py
```python
import os
from datetime import datetime
from pathlib import Path
import allure

class ScreenshotHelper:
    @staticmethod
    def take_screenshot(driver, name="screenshot"):
        """Take screenshot and attach to Allure report"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_dir = Path(__file__).resolve().parent.parent / 'reports' / 'screenshots'
        screenshot_dir.mkdir(parents=True, exist_ok=True)
        
        screenshot_name = f"{name}_{timestamp}.png"
        screenshot_path = screenshot_dir / screenshot_name
        
        driver.save_screenshot(str(screenshot_path))
        
        # Attach to Allure report
        allure.attach(
            driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=allure.attachment_type.PNG
        )
        
        return str(screenshot_path)
```

#### utilities/data_generator.py
```python
from faker import Faker

class DataGenerator:
    def __init__(self):
        self.fake = Faker()
    
    def generate_user_data(self):
        """Generate random user data"""
        return {
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name(),
            'email': self.fake.email(),
            'phone': self.fake.phone_number(),
            'address': self.fake.address(),
            'company': self.fake.company(),
            'job_title': self.fake.job()
        }
    
    def generate_email(self):
        return self.fake.email()
    
    def generate_password(self, length=12):
        return self.fake.password(length=length, special_chars=True, digits=True, upper_case=True, lower_case=True)
    
    def generate_name(self):
        return self.fake.name()
    
    def generate_address(self):
        return self.fake.address()
    
    def generate_phone(self):
        return self.fake.phone_number()
```

---

### Step 8: Create Base Page Object

#### pages/base_page.py
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from config.config import Config
from utilities.logger import Logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
        self.logger = Logger.get_logger(self.__class__.__name__)
    
    def navigate_to(self, url):
        """Navigate to URL"""
        self.logger.info(f"Navigating to: {url}")
        self.driver.get(url)
    
    def find_element(self, locator):
        """Find element with explicit wait"""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            self.logger.error(f"Element not found: {locator}")
            raise
    
    def find_elements(self, locator):
        """Find multiple elements"""
        try:
            elements = self.wait.until(EC.presence_of_all_elements_located(locator))
            return elements
        except TimeoutException:
            self.logger.error(f"Elements not found: {locator}")
            return []
    
    def click_element(self, locator):
        """Click element"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        self.logger.info(f"Clicked element: {locator}")
    
    def enter_text(self, locator, text):
        """Enter text into element"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        self.logger.info(f"Entered text '{text}' into: {locator}")
    
    def get_text(self, locator):
        """Get text from element"""
        element = self.find_element(locator)
        text = element.text
        self.logger.info(f"Retrieved text '{text}' from: {locator}")
        return text
    
    def is_element_visible(self, locator, timeout=10):
        """Check if element is visible"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def is_element_present(self, locator):
        """Check if element is present in DOM"""
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
    
    def wait_for_element_to_disappear(self, locator, timeout=10):
        """Wait for element to disappear"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def hover_over_element(self, locator):
        """Hover over element"""
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.logger.info(f"Hovered over element: {locator}")
    
    def get_current_url(self):
        """Get current URL"""
        return self.driver.current_url
    
    def get_page_title(self):
        """Get page title"""
        return self.driver.title
    
    def refresh_page(self):
        """Refresh current page"""
        self.driver.refresh()
        self.logger.info("Page refreshed")
    
    def switch_to_frame(self, frame_locator):
        """Switch to iframe"""
        frame = self.find_element(frame_locator)
        self.driver.switch_to.frame(frame)
        self.logger.info(f"Switched to frame: {frame_locator}")
    
    def switch_to_default_content(self):
        """Switch back to default content"""
        self.driver.switch_to.default_content()
        self.logger.info("Switched to default content")
```

#### pages/login_page.py
```python
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import Config

class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
    WELCOME_MESSAGE = (By.XPATH, "//h1[contains(text(), 'Welcome')]")
    LOGOUT_BUTTON = (By.ID, "logout")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{Config.get_base_url()}/login"
    
    def navigate_to_login(self):
        """Navigate to login page"""
        self.navigate_to(self.url)
    
    def enter_username(self, username):
        """Enter username"""
        self.enter_text(self.USERNAME_INPUT, username)
    
    def enter_password(self, password):
        """Enter password"""
        self.enter_text(self.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        """Click login button"""
        self.click_element(self.LOGIN_BUTTON)
    
    def login(self, username, password):
        """Complete login process"""
        self.logger.info(f"Logging in with username: {username}")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
    
    def get_error_message(self):
        """Get error message text"""
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_welcome_message_displayed(self):
        """Check if welcome message is displayed"""
        return self.is_element_visible(self.WELCOME_MESSAGE)
    
    def is_error_message_displayed(self):
        """Check if error message is displayed"""
        return self.is_element_visible(self.ERROR_MESSAGE, timeout=5)
    
    def logout(self):
        """Logout from application"""
        if self.is_element_visible(self.LOGOUT_BUTTON, timeout=5):
            self.click_element(self.LOGOUT_BUTTON)
            self.logger.info("Logged out successfully")
```

---

### Step 9: Create API Client

#### api/base_api_client.py
```python
import requests
import allure
import json
from utilities.logger import Logger
from config.config import Config

class BaseAPIClient:
    def __init__(self):
        self.base_url = Config.get_api_base_url()
        self.session = requests.Session()
        self.logger = Logger.get_logger(self.__class__.__name__)
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    
    def _log_request(self, method, url, **kwargs):
        """Log request details"""
        self.logger.info(f"{method} request to: {url}")
        if 'json' in kwargs:
            self.logger.debug(f"Request body: {json.dumps(kwargs['json'], indent=2)}")
        if 'params' in kwargs:
            self.logger.debug(f"Query params: {kwargs['params']}")
    
    def _log_response(self, response):
        """Log response details"""
        self.logger.info(f"Response status: {response.status_code}")
        try:
            self.logger.debug(f"Response body: {json.dumps(response.json(), indent=2)}")
        except:
            self.logger.debug(f"Response text: {response.text}")
    
    @allure.step("Send GET request to {endpoint}")
    def get(self, endpoint, params=None, headers=None):
        """Send GET request"""
        url = f"{self.base_url}{endpoint}"
        request_headers = {**self.headers, **(headers or {})}
        
        self._log_request("GET", url, params=params)
        response = self.session.get(url, params=params, headers=request_headers)
        self._log_response(response)
        
        # Attach to Allure
        allure.attach(
            f"URL: {url}\nMethod: GET\nParams: {params}",
            name="Request Details",
            attachment_type=allure.attachment_type.TEXT
        )
        
        return response
    
    @allure.step("Send POST request to {endpoint}")
    def post(self, endpoint, data=None, json=None, headers=None):
        """Send POST request"""
        url = f"{self.base_url}{endpoint}"
        request_headers = {**self.headers, **(headers or {})}
        
        self._log_request("POST", url, json=json, data=data)
        response = self.session.post(url, data=data, json=json, headers=request_headers)
        self._log_response(response)
        
        # Attach to Allure
        if json:
            allure.attach(
                f"Request Body:\n{json}",
                name="POST Request Body",
                attachment_type=allure.attachment_type.JSON
            )
        
        return response
    
    @allure.step("Send PUT request to {endpoint}")
    def put(self, endpoint, data=None, json=None, headers=None):
        """Send PUT request"""
        url = f"{self.base_url}{endpoint}"
        request_headers = {**self.headers, **(headers or {})}
        
        self._log_request("PUT", url, json=json, data=data)
        response = self.session.put(url, data=data, json=json, headers=request_headers)
        self._log_response(response)
        
        return response
    
    @allure.step("Send PATCH request to {endpoint}")
    def patch(self, endpoint, data=None, json=None, headers=None):
        """Send PATCH request"""
        url = f"{self.base_url}{endpoint}"
        request_headers = {**self.headers, **(headers or {})}
        
        self._log_request("PATCH", url, json=json, data=data)
        response = self.session.patch(url, data=data, json=json, headers=request_headers)
        self._log_response(response)
        
        return response
    
    @allure.step("Send DELETE request to {endpoint}")
    def delete(self, endpoint, headers=None):
        """Send DELETE request"""
        url = f"{self.base_url}{endpoint}"
        request_headers = {**self.headers, **(headers or {})}
        
        self._log_request("DELETE", url)
        response = self.session.delete(url, headers=request_headers)
        self._log_response(response)
        
        return response
    
    def set_auth_token(self, token):
        """Set authentication token"""
        self.headers['Authorization'] = f'Bearer {token}'
        self.logger.info("Authentication token set")
    
    def set_header(self, key, value):
        """Set custom header"""
        self.headers[key] = value
        self.logger.info(f"Header set: {key}={value}")
    
    def clear_headers(self):
        """Clear all custom headers"""
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.logger.info("Headers cleared")
```

---

### Step 10: Create Feature Files

#### features/ui/login.feature
```gherkin
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
    When I enter username "<username>"
    And I enter password "<password>"
    And I click the login button
    Then I should see an error message "<error_message>"

    Examples:
      | username              | password    | error_message           |
      | invalid@example.com   | TestPass123 | Invalid credentials     |
      | testuser@example.com  | short       | Invalid credentials     |
      | notanemail            | TestPass123 | Invalid email format    |
```

#### features/api/user_api.feature
```gherkin
Feature: User API Operations
  As an API client
  I want to perform CRUD operations on users
  So that I can manage user data

  @smoke @api @get
  Scenario: Get user details by ID
    Given I have a valid authentication token
    When I send a GET request to "/api/users/1"
    Then the response status code should be 200
    And the response should contain user details
    And the response should have field "id" with value "1"
    And the response should have field "email"

  @api @post @positive
  Scenario: Create a new user
    Given I have a valid authentication token
    And I have user data with:
      | first_name | John           |
      | last_name  | Doe            |
      | email      | john@test.com  |
    When I send a POST request to "/api/users"
    Then the response status code should be 201
    And the response should contain field "id"
    And the response should have field "email" with value "john@test.com"

  @api @put @positive
  Scenario: Update existing user
    Given I have a valid authentication token
    When I send a PUT request to "/api/users/1" with data:
      | first_name | Jane  |
      | last_name  | Smith |
    Then the response status code should be 200
    And the response should have field "first_name" with value "Jane"
    And the response should have field "last_name" with value "Smith"

  @api @delete @positive
  Scenario: Delete existing user
    Given I have a valid authentication token
    When I send a DELETE request to "/api/users/999"
    Then the response status code should be 204

  @api @delete @negative
  Scenario: Delete non-existent user
    Given I have a valid authentication token
    When I send a DELETE request to "/api/users/99999"
    Then the response status code should be 404

  @api @get @negative
  Scenario: Get user without authentication
    Given I do not have an authentication token
    When I send a GET request to "/api/users/1"
    Then the response status code should be 401
    And the response should have field "error" with value "Unauthorized"

  @regression @api
  Scenario: Get list of all users
    Given I have a valid authentication token
    When I send a GET request to "/api/users"
    Then the response status code should be 200
    And the response should be an array
    And the response array should not be empty
```

---

### Step 11: Create Step Definitions

#### features/steps/ui_steps.py
```python
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pages.login_page import LoginPage
from config.config import Config
from utilities.screenshot_helper import ScreenshotHelper
import allure

@given('I am on the login page')
def step_navigate_to_login(context):
    """Navigate to login page"""
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate_to_login()
    allure.attach(
        context.driver.get_screenshot_as_png(),
        name="Login Page Loaded",
        attachment_type=allure.attachment_type.PNG
    )

@when('I enter username "{username}"')
def step_enter_username(context, username):
    """Enter username"""
    context.login_page.enter_username(username)

@when('I enter password "{password}"')
def step_enter_password(context, password):
    """Enter password"""
    context.login_page.enter_password(password)

@when('I click the login button')
def step_click_login(context):
    """Click login button"""
    context.login_page.click_login_button()

@then('I should be redirected to the dashboard')
def step_check_dashboard_url(context):
    """Verify redirect to dashboard"""
    current_url = context.login_page.get_current_url()
    assert '/dashboard' in current_url, f"Expected '/dashboard' in URL, got: {current_url}"
    allure.attach(
        f"Current URL: {current_url}",
        name="Dashboard URL Verification",
        attachment_type=allure.attachment_type.TEXT
    )

@then('I should see the welcome message')
def step_check_welcome_message(context):
    """Verify welcome message is displayed"""
    assert context.login_page.is_welcome_message_displayed(), "Welcome message not displayed"

@then('I should see an error message "{message}"')
def step_check_error_message(context, message):
    """Verify error message"""
    assert context.login_page.is_error_message_displayed(), "Error message not displayed"
    error_text = context.login_page.get_error_message()
    assert message in error_text, f"Expected '{message}' in error, got: {error_text}"
    allure.attach(
        f"Error Message: {error_text}",
        name="Error Message",
        attachment_type=allure.attachment_type.TEXT
    )

@then('I should remain on the login page')
def step_check_login_page(context):
    """Verify still on login page"""
    current_url = context.login_page.get_current_url()
    assert '/login' in current_url, f"Expected '/login' in URL, got: {current_url}"
```

#### features/steps/api_steps.py
```python
from behave import given, when, then
import json
import allure
from api.base_api_client import BaseAPIClient

@given('I have a valid authentication token')
def step_set_auth_token(context):
    """Set valid authentication token"""
    context.api_client = BaseAPIClient()
    # In real scenario, get token from login API
    context.api_client.set_auth_token("mock_token_12345")

@given('I do not have an authentication token')
def step_no_auth_token(context):
    """Initialize API client without auth token"""
    context.api_client = BaseAPIClient()

@given('I have user data with')
def step_prepare_user_data(context):
    """Prepare user data from table"""
    context.user_data = {}
    for row in context.table:
        context.user_data[row['first_name']] = row['last_name']

@when('I send a GET request to "{endpoint}"')
def step_send_get_request(context, endpoint):
    """Send GET request"""
    context.response = context.api_client.get(endpoint)
    
    # Attach to