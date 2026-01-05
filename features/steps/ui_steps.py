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