.PHONY: clean install test test-api test-ui report help

help:
	@echo "Available targets:"
	@echo "  make install    - Install dependencies"
	@echo "  make test-api   - Run API tests with @get tag"
	@echo "  make test-ui    - Run UI tests with @ui tag"
	@echo "  make test       - Run all tests"
	@echo "  make report     - Generate and open reports"
	@echo "  make clean      - Clean reports and cache"

clean:
	rm -rf reports __pycache__ .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

install:
	pip install --upgrade pip setuptools wheel
	pip install -r requirements.txt

test-api:
	@echo "Running API tests with @get tag..."
	@rm -rf reports/allure-results reports/allure-report reports/behave-html
	@mkdir -p reports/allure-results reports/behave-html
	venv/bin/behave \
		-f allure_behave.formatter:AllureFormatter -o reports/allure-results \
		-f behave_html_pretty_formatter:PrettyHTMLFormatter -o reports/behave-html/report.html \
		--tags=@get --no-skipped
	@$(MAKE) report

test-ui:
	@echo "Running UI tests with @ui tag..."
	@rm -rf reports/allure-results reports/allure-report reports/behave-html
	@mkdir -p reports/allure-results reports/behave-html
	venv/bin/behave \
		-f allure_behave.formatter:AllureFormatter -o reports/allure-results \
		-f behave_html_pretty_formatter:PrettyHTMLFormatter -o reports/behave-html/report.html \
		--tags=@ui --no-skipped
	@$(MAKE) report

test:
	@echo "Running all tests..."
	@rm -rf reports/allure-results reports/allure-report reports/behave-html
	@mkdir -p reports/allure-results reports/behave-html
	venv/bin/behave \
		-f allure_behave.formatter:AllureFormatter -o reports/allure-results \
		-f behave_html_pretty_formatter:PrettyHTMLFormatter -o reports/behave-html/report.html
	@$(MAKE) report

report:
	@echo "=========================================="
	@echo "Reports available:"
	@echo "  Behave HTML: reports/behave-html/report.html"
	@echo "  Allure: Use 'allure serve reports/allure-results'"
	@echo "=========================================="
	@open reports/behave-html/report.html || true
	@echo ""
	@echo "To view Allure report with proper server:"
	@echo "  allure serve reports/allure-results"
	@echo ""
