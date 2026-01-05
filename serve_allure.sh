#!/bin/bash
# serve_allure.sh - Start Allure report server

echo "Starting Allure report server..."
echo "This will automatically open the report in your browser."
echo "Press Ctrl+C to stop the server."
echo ""

allure serve reports/allure-results
