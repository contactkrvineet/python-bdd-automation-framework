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