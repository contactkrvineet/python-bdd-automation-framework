# GitHub Actions CI/CD Setup Guide

This guide explains how to set up and use the GitHub Actions CI/CD pipeline for automated testing.

## Table of Contents

1. [Overview](#overview)
2. [Setup Instructions](#setup-instructions)
3. [Workflow Features](#workflow-features)
4. [How to Use](#how-to-use)
5. [Viewing Results](#viewing-results)
6. [Customization](#customization)

---

## Overview

The GitHub Actions workflow automatically:

- ✅ Runs on every push to `main` or `develop` branches
- ✅ Runs on every pull request to `main` or `develop`
- ✅ Can be manually triggered with custom tags and environment
- ✅ Executes BDD tests using Behave
- ✅ Generates Allure and Behave HTML reports
- ✅ Uploads reports as downloadable artifacts
- ✅ Publishes Allure report to GitHub Pages (optional)
- ✅ Provides test execution summary

---

## Setup Instructions

### 1. Push Code to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit with BDD framework and CI/CD"

# Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Push to GitHub
git push -u origin main
```

### 2. Enable GitHub Actions

GitHub Actions is enabled by default for public repositories. For private repositories:

1. Go to repository **Settings**
2. Click **Actions** > **General**
3. Under "Actions permissions", select **Allow all actions and reusable workflows**
4. Click **Save**

### 3. Enable GitHub Pages (for Publishing Both Reports)

To publish Allure and Behave reports automatically:

1. Go to repository **Settings**
2. Click **Pages** (in left sidebar)
3. Under "Source", select **GitHub Actions**
4. Click **Save**

After the next successful test run, your reports will be available at:

```
https://YOUR_USERNAME.github.io/YOUR_REPO/
```

This landing page will provide links to both:

- **Allure Report**: `https://YOUR_USERNAME.github.io/YOUR_REPO/allure-report/`
- **Behave Report**: `https://YOUR_USERNAME.github.io/YOUR_REPO/behave-report/report.html`

---

## Workflow Features

### Automatic Triggers

The workflow runs automatically when:

1. **Push to main or develop branch**

   - Runs tests with `@smoke` tag by default
   - Tests against `dev` environment

2. **Pull Request to main or develop**
   - Validates changes before merging
   - Runs smoke tests to ensure quality

### Manual Trigger

You can manually run the workflow with custom parameters:

1. Go to repository → **Actions** tab
2. Select "**BDD Tests**" workflow
3. Click **Run workflow** button
4. Choose options:
   - **Branch**: Select branch to run from
   - **Tags**: Enter Behave tags (e.g., `@api`, `@smoke`, `@regression`)
   - **Environment**: Select environment (`dev`, `staging`, `prod`)
5. Click **Run workflow**

### Workflow Steps

```yaml
1. Checkout code
2. Setup Python 3.10
3. Install dependencies
4. Install Chrome browser
5. Install Allure
6. Run Behave tests
7. Generate Allure report
8. Upload reports as artifacts
9. Publish to GitHub Pages (if on main branch)
10. Display test summary
```

---

## How to Use

### Running Different Test Suites

#### 1. Smoke Tests (Default)

```yaml
Tags: @smoke
Environment: dev
```

Runs automatically on every push/PR.

#### 2. API Tests Only

Manually trigger with:

```
Tags: @api
Environment: staging
```

#### 3. Full Regression Suite

Manually trigger with:

```
Tags: @regression
Environment: staging
```

#### 4. Specific Feature

Manually trigger with:

```
Tags: @get
Environment: prod
```

### Testing Multiple Environments

The workflow supports three environments:

- **dev** - Development environment (default)
- **staging** - Pre-production environment
- **prod** - Production environment (use with caution!)

Environment configuration is loaded from `config/environments/{env}.yaml`

### Combining Tags

Use Behave tag syntax:

```
# AND condition (must have both tags)
@api -t @smoke

# OR condition (can have either tag)
@api,@ui

# Exclude tags
@api -t ~@wip
```

---

## Viewing Results

### 1. Test Summary

After workflow completes:

1. Go to **Actions** tab
2. Click on the workflow run
3. View **Summary** section
4. See test execution details:
   - Environment used
   - Tags executed
   - Python version
   - Available reports

### 2. Download Reports

In the workflow run page:

1. Scroll to **Artifacts** section
2. Download any of:
   - `behave-html-report` - Simple HTML report
   - `allure-results` - Raw Allure test results
   - `allure-report` - Complete Allure HTML report
   - `test-logs` - Execution logs

### 3. View Reports Online (GitHub Pages)

If GitHub Pages is enabled, visit the main dashboard:

1. Go to `https://YOUR_USERNAME.github.io/YOUR_REPO/`
2. You'll see a landing page with links to both reports:
   - **📊 Allure Report** - Interactive test analytics and history
   - **📝 Behave Report** - BDD scenario execution details
3. Reports update automatically after each successful run on `main` branch

You can also access reports directly:

- Allure: `https://YOUR_USERNAME.github.io/YOUR_REPO/allure-report/`
- Behave: `https://YOUR_USERNAME.github.io/YOUR_REPO/behave-report/report.html`

### 4. Check Test Status

- ✅ **Green checkmark** - All tests passed
- ❌ **Red X** - Some tests failed
- 🟡 **Yellow dot** - Tests are running
- ⚪ **Gray circle** - Tests skipped/cancelled

---

## Customization

### Change Default Tags

Edit `.github/workflows/tests.yml`:

```yaml
default: "@smoke" # Change to @regression, @api, etc.
```

### Add More Environments

1. Create new environment file: `config/environments/qa.yaml`
2. Add to workflow choices:

```yaml
options:
  - dev
  - staging
  - qa # New environment
  - prod
```

### Run on Different Branches

Edit trigger section:

```yaml
on:
  push:
    branches: [main, develop, feature/*] # Add more branches
```

### Change Python Version

Edit strategy matrix:

```yaml
strategy:
  matrix:
    python-version: ["3.10", "3.11"] # Test multiple versions
```

### Add Slack/Email Notifications

Add notification step at the end:

```yaml
- name: Send notification
  if: always()
  uses: 8398a7/action-slack@v3
  with:
    status: ${{ job.status }}
    webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

### Schedule Nightly Runs

Add schedule trigger:

```yaml
on:
  schedule:
    - cron: "0 2 * * *" # Run daily at 2 AM UTC
```

---

## Troubleshooting

### Tests Failing in CI but Passing Locally

**Causes**:

- Different Python version
- Missing dependencies
- Headless browser issues (UI tests)
- Environment configuration

**Solutions**:

```bash
# Test locally with same conditions as CI
HEADLESS=true venv/bin/behave -t @ui

# Check Python version matches
python --version  # Should be 3.10

# Ensure all dependencies installed
pip install -r requirements.txt
pip install behave-html-pretty-formatter
```

### GitHub Pages Not Updating

**Check**:

1. Workflow ran successfully on `main` branch
2. GitHub Pages is enabled in settings
3. Deployment job completed successfully
4. Clear browser cache and refresh

### Artifacts Not Uploading

**Ensure**:

1. Reports directory exists
2. Tests actually ran (check logs)
3. Artifact upload step didn't fail

### Secrets for Production

For production tests requiring credentials:

1. Go to **Settings** > **Secrets and variables** > **Actions**
2. Click **New repository secret**
3. Add secrets:

   - `PROD_USERNAME`
   - `PROD_PASSWORD`
   - `API_KEY`

4. Use in workflow:

```yaml
env:
  USERNAME: ${{ secrets.PROD_USERNAME }}
  PASSWORD: ${{ secrets.PROD_PASSWORD }}
```

---

## Best Practices

1. **Use Smoke Tests for Quick Feedback**

   - Run `@smoke` on every PR
   - Full regression on nightly schedule

2. **Test Against Staging First**

   - Don't run tests against production automatically
   - Require manual approval for prod tests

3. **Keep Test Execution Fast**

   - CI tests should complete in < 10 minutes
   - Use `@smoke` for speed
   - Run `@regression` on schedule

4. **Monitor Test Results**

   - Set up notifications for failures
   - Review Allure reports weekly
   - Track test trends over time

5. **Maintain Green Builds**
   - Fix failing tests immediately
   - Don't merge PRs with failing tests
   - Use `@wip` tag for tests under development

---

## Example Workflow Runs

### Example 1: PR Validation

```yaml
Trigger: Pull Request to main
Tags: @smoke
Environment: dev
Result: ✅ 15 scenarios passed, 0 failed
```

### Example 2: Nightly Regression

```yaml
Trigger: Scheduled (cron)
Tags: @regression
Environment: staging
Result: ✅ 87 scenarios passed, 2 failed
```

### Example 3: Manual API Test

```yaml
Trigger: Manual (workflow_dispatch)
Tags: @api @get
Environment: prod
Result: ✅ 8 scenarios passed, 0 failed
```

---

## Support

For CI/CD issues:

- 📖 [GitHub Actions Documentation](https://docs.github.com/en/actions)
- 🐛 Check workflow logs in Actions tab
- 💬 Open an issue in the repository
