# Quick Start Guide

## Prerequisites

- Python 3.10 installed
- Allure command-line tool (`brew install allure` on macOS)

## Setup

### 1. Create and Activate Virtual Environment

```bash
python3.10 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
pip install behave-html-pretty-formatter
```

## Running Tests

### Using Makefile (Recommended)

```bash
# Run API tests with @get tag
make test-api

# Run UI tests with @ui tag
make test-ui

# Run all tests
make test

# Clean reports and cache
make clean
```

### Using Shell Script

```bash
# Make executable (first time only)
chmod +x run_tests.sh

# Run tests
./run_tests.sh
```

### Manual Command

```bash
# Clean old reports
rm -rf reports/allure-results reports/allure-report reports/behave-html

# Create directories
mkdir -p reports/allure-results reports/behave-html

# Run Behave with both formatters
venv/bin/behave \
  -f allure_behave.formatter:AllureFormatter -o reports/allure-results \
  -f behave_html_pretty_formatter:PrettyHTMLFormatter -o reports/behave-html/report.html \
  -t @get --no-skipped

# Generate Allure HTML report
allure generate reports/allure-results -o reports/allure-report --clean

# Open reports
open reports/allure-report/index.html
open reports/behave-html/report.html
```

## Reports

After running tests, you'll find two reports:

1. **Allure Report**: `reports/allure-report/index.html`

   - Interactive, detailed test execution report
   - Includes screenshots, logs, and step-by-step execution

2. **Behave HTML Report**: `reports/behave-html/report.html`
   - Clean, simple HTML report
   - Shows scenarios, steps, and execution status

## Tag Usage

- `@get` - API GET request tests
- `@api` - All API tests
- `@ui` - UI tests
- `@smoke` - Smoke tests
- `@regression` - Regression tests

### Running Specific Tags

```bash
# Run only API tests
venv/bin/behave -t @api

# Run smoke tests
venv/bin/behave -t @smoke

# Run multiple tags (AND)
venv/bin/behave -t @api -t @get

# Run multiple tags (OR)
venv/bin/behave -t @api,@ui
```

## Troubleshooting

### Issue: Reports not generated

**Solution**: Always use `venv/bin/behave` (not just `behave`) to ensure you're using the virtual environment's Behave installation with all required packages.

### Issue: Allure report keeps loading

**Solution**:

1. Ensure Allure results were generated: `ls -la reports/allure-results`
2. Regenerate the report: `allure generate reports/allure-results -o reports/allure-report --clean`
3. Clear browser cache and reload

### Issue: behave-html-formatter not found

**Solution**: We use `behave-html-pretty-formatter` which is more stable:

```bash
pip install behave-html-pretty-formatter
```

## Environment Configuration

Tests use environment-specific configs in `config/environments/`:

- `dev.yaml` - Development environment
- `staging.yaml` - Staging environment
- `prod.yaml` - Production environment

Set environment via:

```bash
ENV=staging venv/bin/behave -t @api
```

## Continuous Integration

For CI/CD pipelines:

```bash
#!/bin/bash
set -e

# Setup
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install behave-html-pretty-formatter

# Clean and run
rm -rf reports
mkdir -p reports/allure-results reports/behave-html

# Execute tests
venv/bin/behave \
  -f allure_behave.formatter:AllureFormatter -o reports/allure-results \
  -f behave_html_pretty_formatter:PrettyHTMLFormatter -o reports/behave-html/report.html \
  --tags=@smoke --no-skipped

# Generate Allure report
allure generate reports/allure-results -o reports/allure-report --clean

# Archive reports
tar -czf reports.tar.gz reports/
```

## Support

For issues, check:

1. Virtual environment is activated: `which python` should show `venv/bin/python`
2. All dependencies installed: `pip list | grep behave`
3. Allure CLI installed: `allure --version`
4. Reports directories exist: `ls -la reports/`
