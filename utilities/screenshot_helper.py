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