# python-bdd-automation-framework
A robust, scalable test automation framework built with Python, Behave (BDD), Selenium, and Requests for comprehensive UI and API testing with beautiful HTML reports.

🎯 Overview
This framework offers a comprehensive solution for behavior-driven testing of web applications and RESTful APIs. Designed with clean architecture principles and following BDD best practices, it enables teams to write human-readable test scenarios that serve as living documentation.
✨ Key Features

BDD with Behave: Write tests in Gherkin syntax (Given/When/Then) for better collaboration between technical and non-technical team members
Dual Testing Support:

UI automation with Selenium WebDriver
API testing with the Requests library


Multiple Report Formats:

Allure Reports (modern, interactive HTML dashboards)
Behave HTML reports (simple, quick reference)


Page Object Model: Clean separation of test logic and page elements
Parallel Execution: Run tests in parallel for faster feedback
Cross-Browser Support: Execute tests on Chrome, Firefox, Edge, Safari
Configuration Management: Environment-specific configs (dev, staging, prod)
Logging & Screenshots: Automatic capture on test failures
CI/CD Ready: Easily integrate with Jenkins, GitHub Actions, GitLab CI, etc.

🛠️ Tech Stack
ComponentTechnologyLanguagePython 3.8+BDD FrameworkBehaveTest Runnerpytest (optional)UI AutomationSelenium WebDriverAPI TestingRequestsReportingAllure, Behave HTMLBrowser Managementwebdriver-managerData GenerationFakerParallel Executionpytest-xdist / behave parallel
