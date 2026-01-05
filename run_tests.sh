#!/bin/bash
set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}=========================================="
echo "BDD Test Execution Script"
echo -e "==========================================${NC}"

# Clean previous reports
echo -e "\n${YELLOW}Cleaning previous reports...${NC}"
rm -rf reports/allure-results reports/allure-report reports/behave-html

# Create directories
mkdir -p reports/allure-results reports/allure-report reports/behave-html

# Run Behave with BOTH formatters
echo -e "\n${YELLOW}Running Behave tests with @get tag...${NC}"
venv/bin/behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results \
       -f behave_html_pretty_formatter:PrettyHTMLFormatter -o reports/behave-html/report.html \
       -t @get --no-skipped

echo -e "\n${GREEN}=========================================="
echo "Reports Generated:"
echo "  Behave HTML: reports/behave-html/report.html"
echo -e "==========================================${NC}"

# Open Behave HTML report
echo -e "\n${YELLOW}Opening Behave HTML report...${NC}"
open reports/behave-html/report.html

echo -e "\n${YELLOW}To view Allure report (with proper server):${NC}"
echo -e "${GREEN}  allure serve reports/allure-results${NC}"

echo -e "\n${GREEN}Done!${NC}"
