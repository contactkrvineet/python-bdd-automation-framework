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