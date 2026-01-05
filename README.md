# Python BDD Automation Framework

[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/)
[![Behave](https://img.shields.io/badge/behave-1.3.3-green.svg)](https://behave.readthedocs.io/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A comprehensive BDD (Behavior-Driven Development) automation framework using Python, Behave, Selenium, and Allure for API and UI testing with automated CI/CD pipelines and live reporting.

## 📋 Table of Contents

1. [Framework Overview](#framework-overview)
2. [How the Framework Works](#how-the-framework-works)
3. [Framework Structure](#framework-structure)
4. [Quick Start](#quick-start)
5. [Running Tests](#running-tests)
6. [What is Makefile?](#what-is-makefile)
7. [Viewing Reports](#viewing-reports)
8. [Live Reports on GitHub Pages](#live-reports-on-github-pages)
9. [GitHub Actions CI/CD](#github-actions-cicd)
10. [Configuration](#configuration)
11. [Best Practices](#best-practices)

---

## Framework Overview

This framework provides:

- ✅ **BDD Testing** with Gherkin syntax for readable test scenarios
- ✅ **API Testing** with requests library and custom API client
- ✅ **UI Testing** with Selenium WebDriver and Page Object Model
- ✅ **Dual Reporting** - Allure (interactive) and Behave HTML (simple)
- ✅ **Multi-Environment** support (dev, staging, prod)
- ✅ **CI/CD Ready** with GitHub Actions integration
- ✅ **Tag-based Execution** for flexible test organization
- ✅ **Live Reports** published automatically to GitHub Pages
- ✅ **Makefile Support** for simplified test execution

---

## How the Framework Works

### 🎯 Core Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                    1. Write Feature Files                       │
│            (Human-readable Gherkin scenarios)                   │
│         features/api/user_api.feature                          │
│         features/ui/login.feature                              │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│              2. Implement Step Definitions                      │
│         (Python code that executes the steps)                   │
│         features/steps/api_steps.py                            │
│         features/steps/ui_steps.py                             │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│             3. Run Tests (Multiple Options)                     │
│    • Makefile: make test-api, make test-ui, make test         │
│    • Behave CLI: behave -t @smoke                              │
│    • GitHub Actions: Automated CI/CD                           │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│           4. Generate Reports (Automatic)                       │
│    • Allure Report: Interactive HTML with charts               │
│    • Behave Report: Simple HTML summary                        │
│    • Logs: Detailed execution logs                             │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│              5. View Results                                    │
│    Local:                                                       │
│    • allure serve reports/allure-results                       │
│    • open reports/behave-html/report.html                      │
│                                                                 │
│    CI/CD (GitHub Pages):                                       │
│    • https://username.github.io/repo-name/                     │
│      ├─ Allure Report                                          │
│      └─ Behave Report                                          │
└─────────────────────────────────────────────────────────────────┘
```

### 🔄 Test Execution Flow

1. **Behave reads feature files** from `features/` directory
2. **Matches steps** with step definitions in `features/steps/`
3. **Executes scenarios** using:
   - Page Objects for UI tests (`pages/`)
   - API clients for API tests (`api/`)
   - Configuration from `config/environments/`
4. **Generates test results** in real-time:
   - Allure JSON results → `reports/allure-results/`
   - Behave HTML → `reports/behave-html/`
5. **Hooks** in `features/environment.py` handle:
   - Browser setup/teardown
   - Screenshots on failure
   - Logging configuration

### 🏗️ Architecture Layers

```
┌─────────────────────────────────────────────────────────────────┐
│                     Feature Files (Gherkin)                     │
│                  Business-readable test cases                   │
└─────────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────────┐
│                    Step Definitions Layer                       │
│              Translates Gherkin to Python code                  │
└─────────────────────────────────────────────────────────────────┘
                              │
         ┌────────────────────┴────────────────────┐
         │                                         │
┌────────────────────┐                  ┌──────────────────────┐
│   Page Objects     │                  │    API Clients       │
│   (UI Tests)       │                  │   (API Tests)        │
│  • login_page.py   │                  │ • base_api_client.py │
│  • base_page.py    │                  │                      │
└────────────────────┘                  └──────────────────────┘
         │                                         │
         └────────────────────┬────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────────┐
│                    Utilities & Helpers                          │
│     • Logger • Screenshot Helper • Data Generator               │
└─────────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────────┐
│                   Configuration Layer                           │
│       Environment-specific settings (dev/staging/prod)          │
└─────────────────────────────────────────────────────────────────┘
```

---

## Framework Structure

```
python-bdd-automation-framework/
│
├── .github/
│   └── workflows/
│       └── tests.yml              # CI/CD pipeline - auto-runs tests & publishes reports
│
├── features/                      # BDD feature files and step definitions
│   ├── api/                       # API feature files (Gherkin)
│   │   └── user_api.feature       # User API test scenarios
│   ├── ui/                        # UI feature files (Gherkin)
│   │   └── login.feature          # Login UI test scenarios
│   ├── steps/                     # Step definitions (glue code)
│   │   ├── api_steps.py           # Implements API test steps
│   │   └── ui_steps.py            # Implements UI test steps
│   └── environment.py             # Behave hooks (setup/teardown)
│
├── pages/                         # Page Object Model (UI automation)
│   ├── base_page.py               # Base page with common methods
│   └── login_page.py              # Login page object with locators & methods
│
├── api/                           # API clients
│   └── base_api_client.py         # Reusable HTTP client with logging & Allure integration
│
├── config/                        # Configuration management
│   ├── config.py                  # Configuration loader class
│   └── environments/              # Environment-specific configs
│       ├── dev.yaml               # Development environment settings
│       ├── staging.yaml           # Staging environment settings
│       └── prod.yaml              # Production environment settings
│
├── utilities/                     # Helper utilities
│   ├── logger.py                  # Colored console logging
│   ├── screenshot_helper.py       # Screenshot capture on test failures
│   └── data_generator.py         # Fake test data generator (Faker)
│
├── reports/                       # Test reports (auto-generated)
│   ├── allure-results/            # Allure test results (JSON)
│   ├── allure-report/             # Allure HTML report (generated)
│   └── behave-html/               # Behave HTML report
│       └── report.html            # Simple test execution report
│
├── logs/                          # Execution logs (timestamped)
│
├── data/                          # Test data files (JSON, CSV, etc.)
│
├── tests/                         # Additional pytest tests (optional)
│
├── requirements.txt               # Python dependencies
├── Makefile                       # Quick commands for test execution (make test-api, etc.)
├── run_tests.sh                   # Shell script for running tests
├── serve_allure.sh                # Script to serve Allure reports locally
├── QUICK_START.md                 # Quick start guide
├── GITHUB_ACTIONS.md             # GitHub Actions CI/CD guide
├── REPORTS_PUBLISHING_GUIDE.md   # Guide for publishing reports to GitHub Pages
└── README.md                      # This file
```

### 📁 Directory Structure Explained

#### **Features Layer** (`features/`)

- **Purpose**: Contains business-readable test scenarios
- **Structure Maintained**:
  - Separate folders for API and UI tests
  - Steps organized by test type (api_steps.py, ui_steps.py)
  - Centralized hooks in environment.py
- **Best Practice**: One feature file per feature/module

#### **Page Objects** (`pages/`)

- **Purpose**: Encapsulates UI elements and interactions
- **Structure Maintained**:
  - base_page.py - Common methods (click, type, wait)
  - Specific page classes inherit from base_page
  - Locators defined as class variables
- **Benefits**: Code reusability, easier maintenance

#### **API Layer** (`api/`)

- **Purpose**: Reusable HTTP clients for API testing
- **Structure Maintained**:
  - base_api_client.py handles all HTTP methods
  - Automatic logging and Allure attachment
  - Consistent error handling

#### **Configuration** (`config/`)

- **Purpose**: Manage environment-specific settings
- **Structure Maintained**:
  - YAML files for each environment
  - Single config.py loads the appropriate environment
  - Easy to add new environments

#### **Reports** (`reports/`)

- **Auto-generated**: Created automatically during test execution
- **Contains**: Both Allure and Behave reports
- **Lifecycle**: Cleaned before each test run, archived in CI/CD

---

## Quick Start

### Prerequisites

- **Python 3.10** - [Download](https://www.python.org/downloads/)
- **Allure** - `brew install allure` (macOS) or [Download](https://github.com/allure-framework/allure2/releases)
- **Git** - [Download](https://git-scm.com/downloads)
- **Chrome Browser** (for UI tests)

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd python-bdd-automation-framework

# Create virtual environment with Python 3.10
python3.10 -m venv venv

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows

# Install dependencies
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
pip install behave-html-pretty-formatter

# Verify installation
# Verify installation
venv/bin/behave --version
allure --version
```

---

## Running Tests

The framework provides multiple ways to execute tests, from simple Makefile commands to advanced Behave CLI options.

### Method 1: Using Makefile (⭐ Recommended)

Makefile provides the simplest way to run tests with pre-configured commands.

```bash
# Run API tests
make test-api

# Run UI tests
make test-ui

# Run all tests
make test

# Clean reports and cache
make clean

# Install dependencies
make install

# View available commands
make help
```

**What happens when you run `make test-api`:**

1. Cleans old reports (`rm -rf reports/`)
2. Creates fresh report directories
3. Executes Behave with `@api` tag
4. Generates both Allure and Behave reports
5. Opens Behave report in browser
6. Launches Allure server automatically

### Method 2: Using Behave CLI Directly

For more control over test execution:

```bash
# Basic syntax
venv/bin/behave [options] [tags] [features]

# Run specific tag
venv/bin/behave \
  -f allure_behave.formatter:AllureFormatter -o reports/allure-results \
  -f behave_html_pretty_formatter:PrettyHTMLFormatter -o reports/behave-html/report.html \
  -t @api --no-skipped

# Run all tests
venv/bin/behave \
  -f allure_behave.formatter:AllureFormatter -o reports/allure-results \
  -f behave_html_pretty_formatter:PrettyHTMLFormatter -o reports/behave-html/report.html

# Run specific feature file
venv/bin/behave features/api/user_api.feature

# Run with dry-run (validate steps without execution)
venv/bin/behave --dry-run -t @api
```

### Method 3: Using Shell Script

```bash
# Run tests with automatic report generation
./run_tests.sh
```

### Available Tags

Organize and filter tests using tags:

| Tag           | Description            | Example Command                     |
| ------------- | ---------------------- | ----------------------------------- |
| `@api`        | All API tests          | `make test-api` or `behave -t @api` |
| `@ui`         | All UI tests           | `make test-ui` or `behave -t @ui`   |
| `@get`        | API GET request tests  | `behave -t @get`                    |
| `@post`       | API POST request tests | `behave -t @post`                   |
| `@smoke`      | Smoke tests            | `behave -t @smoke`                  |
| `@regression` | Regression tests       | `behave -t @regression`             |

### Tag Combinations

```bash
# Multiple tags (AND) - must have both tags
venv/bin/behave -t @api -t @smoke

# Multiple tags (OR) - can have either tag
venv/bin/behave -t @api,@ui

# Exclude specific tags
venv/bin/behave -t ~@ui              # Run all except UI tests
venv/bin/behave -t @api -t ~@wip     # Run API tests except work-in-progress
```

### Environment Selection

Run tests against different environments:

```bash
# Default (dev environment)
make test-api

# Staging environment
ENV=staging venv/bin/behave -t @api

# Production environment (use with caution!)
ENV=prod venv/bin/behave -t @smoke

# With Makefile
ENV=staging make test-api
```

### Advanced Execution Options

```bash
# Parallel execution (requires behave-parallel)
venv/bin/behave -t @api --processes 4

# Generate JUnit XML (for CI/CD)
venv/bin/behave -t @api --junit

# Verbose output
venv/bin/behave -t @api -v

# Show all step definitions
venv/bin/behave --steps-catalog

# Format output
venv/bin/behave -t @api --format plain     # Plain text
venv/bin/behave -t @api --format json      # JSON output
```

---

## What is Makefile?

### 📚 Definition

A **Makefile** is a special file that contains a set of directives (called "targets") used by the `make` build automation tool. It simplifies complex commands into short, memorable aliases.

### 🎯 Purpose in This Framework

Instead of typing long commands like:

```bash
rm -rf reports/allure-results reports/allure-report reports/behave-html
mkdir -p reports/allure-results reports/behave-html
venv/bin/behave \
  -f allure_behave.formatter:AllureFormatter -o reports/allure-results \
  -f behave_html_pretty_formatter:PrettyHTMLFormatter -o reports/behave-html/report.html \
  --tags=@api --no-skipped
allure serve reports/allure-results
```

You simply type:

```bash
make test-api
```

### 🔧 How It Works

1. **Targets**: Each command in Makefile is called a "target"

   ```makefile
   test-api:           # Target name
       @echo "Running API tests..."    # Command 1
       venv/bin/behave -t @api         # Command 2
   ```

2. **Execution**: When you run `make test-api`, it executes all commands under that target

3. **Dependencies**: Targets can depend on other targets
   ```makefile
   test: clean install    # Run 'clean' and 'install' first
       behave             # Then run tests
   ```

### 📋 Available Makefile Commands

```bash
# View all available commands with descriptions
make help
```

Output:

```
Available targets:
  make install    - Install dependencies
  make test-api   - Run API tests with @api tag
  make test-ui    - Run UI tests with @ui tag
  make test       - Run all tests
  make report     - Generate and open reports
  make clean      - Clean reports and cache
```

### ✨ Benefits of Using Makefile

| Benefit              | Description                                |
| -------------------- | ------------------------------------------ |
| **Simplicity**       | Short, easy-to-remember commands           |
| **Consistency**      | Same commands work across all environments |
| **Automation**       | Combines multiple steps into one command   |
| **Documentation**    | Self-documenting (run `make help`)         |
| **Error Prevention** | Pre-configured with correct options        |

### 💡 Makefile vs Behave Direct Command

| Aspect                | Makefile (`make test-api`) | Behave CLI (`behave -t @api`)   |
| --------------------- | -------------------------- | ------------------------------- |
| **Ease of Use**       | ✅ Very simple             | ⚠️ Requires remembering options |
| **Report Generation** | ✅ Automatic               | ❌ Manual                       |
| **Report Opening**    | ✅ Automatic               | ❌ Manual                       |
| **Directory Cleanup** | ✅ Automatic               | ❌ Manual                       |
| **Flexibility**       | ⚠️ Pre-configured          | ✅ Full control                 |
| **Best For**          | Daily testing              | Custom scenarios                |

### 📖 When to Use What

- **Use Makefile**:

  - Daily development testing
  - Quick smoke tests
  - Standardized test execution
  - Team collaboration (everyone uses same commands)

- **Use Behave CLI**:
  - Custom tag combinations
  - Testing specific feature files
  - Debugging individual scenarios
  - Advanced Behave options

---

## Viewing Reports

The framework generates two types of reports, each serving different purposes.

### 1. Behave HTML Report (Simple & Quick)

A lightweight, static HTML report that opens directly in your browser.

**How to View:**

```bash
# After running tests, open the report
open reports/behave-html/report.html          # macOS
xdg-open reports/behave-html/report.html      # Linux
start reports/behave-html/report.html         # Windows

# Or use Makefile (auto-opens after test execution)
make test-api
```

**Features:**

- ✅ Clean, simple interface
- ✅ Scenario execution status (Pass/Fail)
- ✅ Step-by-step details
- ✅ Execution time
- ✅ Screenshots (for UI test failures)
- ✅ No server required - just open the file

**Best For:**

- Quick glance at test results
- Sharing with team (single HTML file)
- Offline viewing

---

### 2. Allure Report (Interactive & Detailed)

A feature-rich, interactive HTML report that requires a local server.

**How to View:**

```bash
# Option 1: Using Allure CLI (Recommended)
allure serve reports/allure-results
# This opens a local server at http://localhost:RANDOM_PORT

# Option 2: Using helper script
./serve_allure.sh

# Option 3: Generate static HTML (for sharing)
allure generate reports/allure-results -o reports/allure-report --clean
open reports/allure-report/index.html

# Option 4: Using Makefile (auto-launches server)
make test-api
# After test completion, Allure server starts automatically
```

**Why Use Allure Serve?**

Allure reports use JavaScript that requires a proper HTTP server:

- ❌ Direct file opening (`file://`) causes CORS errors
- ✅ `allure serve` starts a local server automatically
- ✅ Auto-refreshes when new results are added
- ✅ Port is randomly assigned to avoid conflicts
- ✅ Press `Ctrl+C` to stop the server

**Features:**

- ✅ **All Behave HTML features PLUS:**
- ✅ Test history and trends across multiple runs
- ✅ Detailed request/response for API tests
- ✅ Screenshots and video attachments
- ✅ Timeline visualization
- ✅ Retry information
- ✅ Categorized failures
- ✅ Behavior graphs and charts
- ✅ Environment details
- ✅ Custom parameters and labels

**Report Sections:**

| Section        | Description                                          |
| -------------- | ---------------------------------------------------- |
| **Overview**   | Dashboard with pie charts, graphs, execution summary |
| **Behaviors**  | Tests organized by features and stories              |
| **Suites**     | Test suites and their scenarios                      |
| **Graphs**     | Visual representation of test results                |
| **Timeline**   | Time-based execution view                            |
| **Categories** | Failure categorization                               |
| **Packages**   | Tests grouped by package structure                   |

**Best For:**

- Detailed test analysis
- Historical trend tracking
- Debugging failures
- Stakeholder presentations
- CI/CD integration

---

### 📊 Report Comparison

| Feature           | Behave HTML           | Allure Report           |
| ----------------- | --------------------- | ----------------------- |
| **Setup**         | None - just open file | Requires local server   |
| **File Size**     | Small (KB)            | Larger (MB with assets) |
| **Interactivity** | Basic                 | Advanced                |
| **Test History**  | ❌ No                 | ✅ Yes                  |
| **API Details**   | ❌ No                 | ✅ Request/Response     |
| **Charts**        | ❌ No                 | ✅ Extensive            |
| **Sharing**       | ✅ Single file        | ⚠️ Folder structure     |
| **Offline**       | ✅ Yes                | ✅ Yes (generated)      |
| **Best Use**      | Quick checks          | Deep analysis           |

---

## Live Reports on GitHub Pages

When tests run via GitHub Actions on the `main` branch, both reports are automatically published to GitHub Pages!

### 🌐 Setup GitHub Pages

**One-time setup:**

1. Go to your GitHub repository
2. Navigate to **Settings** → **Pages**
3. Under "Source", select **GitHub Actions**
4. Click **Save**

That's it! No additional configuration needed.

### 📍 Accessing Live Reports

After the next successful test run on `main` branch:

**Main Dashboard:**

```
https://YOUR_USERNAME.github.io/YOUR_REPO/
```

This landing page provides a beautiful dashboard with links to both reports:

```
┌────────────────────────────────────────────────┐
│         🧪 Test Reports Dashboard              │
│    Latest test execution reports from CI/CD    │
├────────────────────────────────────────────────┤
│                                                │
│  📊 Allure Report                             │
│  Comprehensive test execution report with      │
│  detailed analytics, graphs, and test history. │
│                                                │
│  [View Allure Report →]                       │
│                                                │
├────────────────────────────────────────────────┤
│                                                │
│  📝 Behave HTML Report                        │
│  BDD-style test execution report showing       │
│  scenarios, steps, and feature details.        │
│                                                │
│  [View Behave Report →]                       │
│                                                │
└────────────────────────────────────────────────┘
```

**Direct URLs:**

- **Allure Report**: `https://YOUR_USERNAME.github.io/YOUR_REPO/allure-report/`
- **Behave Report**: `https://YOUR_USERNAME.github.io/YOUR_REPO/behave-report/report.html`

### 🔄 How It Works

```
1. You push code to `main` branch
                ↓
2. GitHub Actions triggers workflow
                ↓
3. Tests execute automatically
                ↓
4. Reports generated (Allure + Behave)
                ↓
5. Both reports uploaded as artifacts
                ↓
6. Deploy job publishes to GitHub Pages
                ↓
7. Reports available at public URL (within 1-2 minutes)
```

### ⏱️ Update Frequency

- **Trigger**: Automatic on every push to `main` branch
- **Duration**: Reports typically available within 5-10 minutes
- **Retention**: Latest test run always visible
- **History**: Allure shows trends across multiple runs

### 🎯 Benefits of Live Reports

| Benefit                 | Description                          |
| ----------------------- | ------------------------------------ |
| **Always Accessible**   | View from anywhere, no local setup   |
| **Team Collaboration**  | Share single URL with entire team    |
| **Stakeholder Access**  | Non-technical users can view results |
| **Historical Tracking** | Allure maintains test trends         |
| **No Maintenance**      | Auto-updates with each test run      |
| **Professional**        | Clean, branded landing page          |

### 🔗 Sharing Reports

Share the main dashboard URL with:

- QA team members
- Developers
- Product managers
- Stakeholders

Example message:

```
Latest test results are available at:
https://yourusername.github.io/yourrepo/

✅ All smoke tests passed
📊 Allure Report for detailed analysis
📝 Behave Report for BDD scenarios
```

### 📦 Artifact Reports (Fallback)

If GitHub Pages is not enabled, reports are still available as downloadable artifacts:

1. Go to **Actions** tab in your repository
2. Click on the latest workflow run
3. Scroll to **Artifacts** section
4. Download:
   - `allure-report` (ZIP file)
   - `behave-html-report` (single HTML file)
   - `test-logs` (execution logs)

**Note**: Artifacts are available for 30 days (configurable in workflow).

---

## GitHub Actions CI/CD

Automated testing pipeline that runs tests and publishes reports to GitHub Pages.

### 🚀 Setup (One-Time)

**1. Push Code to GitHub:**

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

**2. Enable GitHub Actions:**

GitHub Actions is enabled by default. Workflow automatically runs when you push code.

**3. Enable GitHub Pages (for Live Reports):**

1. Go to repository **Settings** → **Pages**
2. Under "Source", select **GitHub Actions**
3. Click **Save**

Done! Your reports will now be published automatically.

### ⚙️ Workflow Features

#### Automatic Triggers

The workflow (`[.github/workflows/tests.yml](.github/workflows/tests.yml)`) runs automatically when:

1. **Push to `main` or `develop` branch**

   - Runs tests with `@smoke` tag
   - Tests against `dev` environment
   - Publishes reports to GitHub Pages (main branch only)

2. **Pull Request to `main` or `develop`**
   - Validates changes before merging
   - Runs smoke tests to ensure quality
   - Reports available as artifacts (not published)

#### Manual Trigger

You can manually run tests with custom parameters:

1. Go to your repository on GitHub
2. Click **Actions** tab
3. Select "**BDD Tests**" workflow
4. Click **Run workflow** button
5. Choose your options:
   - **Branch**: Which branch to run from
   - **Tags**: Behave tags (e.g., `@api`, `@smoke`, `@regression`)
   - **Environment**: Target environment (`dev`, `staging`, `prod`)
6. Click **Run workflow**

**Example Scenarios:**

| Scenario               | Tags     | Environment |
| ---------------------- | -------- | ----------- |
| Quick validation       | `@smoke` | `dev`       |
| Full API regression    | `@api`   | `staging`   |
| Production smoke check | `@smoke` | `prod`      |
| UI tests only          | `@ui`    | `dev`       |

### 📋 Workflow Steps

```yaml
1. ✅ Checkout code from repository
2. ✅ Setup Python 3.10 with pip cache
3. ✅ Install dependencies (behave, selenium, allure, etc.)
4. ✅ Install Chrome browser (for UI tests)
5. ✅ Install Allure command-line tool
6. ✅ Create report directories
7. ✅ Run Behave tests with specified tags
8. ✅ Generate Allure HTML report
9. ✅ Upload Behave HTML report as artifact
10. ✅ Upload Allure results as artifact
11. ✅ Upload Allure report as artifact
12. ✅ Upload test logs as artifact
13. ✅ Create landing page with links to both reports
14. ✅ Deploy both reports to GitHub Pages (main branch only)
15. ✅ Display test summary in workflow
```

### 📊 Viewing CI/CD Results

#### Test Summary

After workflow completes:

1. Go to **Actions** tab
2. Click on the workflow run
3. View **Summary** section with:
   - ✅ Test execution details
   - ✅ Environment used
   - ✅ Tags executed
   - ✅ Python version
   - ✅ Links to artifacts

#### Download Artifacts

In the workflow run page, scroll to **Artifacts** section:

| Artifact             | Contents                         | Size    |
| -------------------- | -------------------------------- | ------- |
| `behave-html-report` | Simple HTML report (single file) | ~100 KB |
| `allure-report`      | Complete Allure HTML report      | ~2-5 MB |
| `allure-results`     | Raw JSON results                 | ~500 KB |
| `test-logs`          | Execution logs                   | ~50 KB  |

**Retention**: Artifacts are kept for 30 days.

#### GitHub Pages Reports

If Pages is enabled, visit:

```
https://YOUR_USERNAME.github.io/YOUR_REPO/
```

Reports are published automatically after successful runs on `main` branch.

### 🔔 Test Status Indicators

In GitHub:

- ✅ **Green checkmark** - All tests passed
- ❌ **Red X** - Some tests failed
- 🟡 **Yellow dot** - Tests are running
- ⚪ **Gray circle** - Tests skipped/cancelled

On your repository's main page, you'll see the status badge.

### 🎨 Customization Options

#### Change Default Tags

Edit [.github/workflows/tests.yml](.github/workflows/tests.yml):

```yaml
workflow_dispatch:
  inputs:
    tags:
      default: "@regression" # Change from @smoke
```

#### Add More Environments

1. Create new config: `config/environments/qa.yaml`
2. Update workflow options:

```yaml
environment:
  type: choice
  options:
    - dev
    - staging
    - qa # New environment
    - prod
```

#### Run on More Branches

```yaml
on:
  push:
    branches: [main, develop, feature/*, release/*]
```

#### Schedule Nightly Runs

```yaml
on:
  schedule:
    - cron: "0 2 * * *" # Daily at 2 AM UTC
```

#### Add Slack Notifications

```yaml
- name: Notify Slack
  if: always()
  uses: 8398a7/action-slack@v3
  with:
    status: ${{ job.status }}
    webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

### 📈 Best Practices

1. **Use Tags Wisely**

   - `@smoke` for quick validation
   - `@regression` for comprehensive testing
   - `@critical` for must-pass scenarios

2. **Environment Strategy**

   - `dev` for feature branches
   - `staging` for release candidates
   - `prod` for smoke tests only

3. **Branch Protection**

   - Require status checks before merge
   - Run smoke tests on PRs
   - Full regression on main branch

4. **Monitor Failures**
   - Check Allure trends regularly
   - Review failure categories
   - Fix flaky tests immediately

### 🔗 Workflow File Location

View or edit the workflow:

- [.github/workflows/tests.yml](.github/workflows/tests.yml)

Detailed documentation:

- [GITHUB_ACTIONS.md](GITHUB_ACTIONS.md)
- [REPORTS_PUBLISHING_GUIDE.md](REPORTS_PUBLISHING_GUIDE.md)

---

## Configuration

### Environment Configuration

Edit files in `config/environments/` to customize per environment:

```yaml
# config/environments/dev.yaml
environment: dev
base_url: https://dev.example.com
api_base_url: https://api-dev.example.com
credentials:
  username: testuser@example.com
  password: TestPass123
timeout:
  api: 30
  ui: 20
```

### Runtime Configuration

Set environment variables:

```bash
# Browser selection
BROWSER=firefox venv/bin/behave -t @ui

# Headless mode
HEADLESS=true venv/bin/behave -t @ui

# Environment selection
ENV=staging venv/bin/behave -t @api

# Open reports automatically after execution
OPEN_REPORT=true venv/bin/behave -t @smoke
```

### Behave Configuration

Edit `behave.ini` for Behave-specific settings:

```ini
[behave]
default_tags = -@wip -@skip
show_skipped = false
show_timings = true
color = true
```

---

## Best Practices

### 1. **Writing Feature Files**

```gherkin
Feature: User Authentication
  As a user
  I want to log in to the application
  So that I can access my account

  Background:
    Given I am on the login page

  @smoke @ui
  Scenario: Successful login with valid credentials
    When I enter username "testuser@example.com"
    And I enter password "TestPass123"
    And I click the login button
    Then I should be redirected to the dashboard
    And I should see the welcome message

  @ui @negative
  Scenario Outline: Login fails with invalid credentials
    When I enter username "<username>"
    And I enter password "<password>"
    And I click the login button
    Then I should see an error message "<error>"

    Examples:
      | username              | password    | error                |
      | invalid@example.com   | TestPass123 | Invalid credentials  |
      | testuser@example.com  | wrongpass   | Invalid credentials  |
```

### 2. **Organizing Tests with Tags**

- Use `@smoke` for critical path tests
- Use `@regression` for full test suite
- Use `@wip` (work in progress) for tests under development
- Use `@skip` for temporarily disabled tests

### 3. **Page Object Pattern**

```python
# Good: Using Page Object
login_page = LoginPage(driver)
login_page.login("user@test.com", "pass123")

# Bad: Direct element interaction in step
driver.find_element(By.ID, "username").send_keys("user@test.com")
```

### 4. **API Testing**

```python
# Good: Using API client with logging
response = api_client.get("/api/users")
assert response.status_code == 200

# Bad: Direct requests without logging
response = requests.get("https://api.com/users")
```

### 5. **Data Management**

```python
# Good: Using Faker for dynamic data
user_data = DataGenerator().generate_user_data()

# Bad: Hardcoded test data
user_data = {"email": "test@test.com", "name": "Test User"}
```

---

## Troubleshooting

### Common Issues

#### 1. **ModuleNotFoundError**

**Problem**: Missing Python packages

**Solution**:

```bash
source venv/bin/activate
pip install -r requirements.txt
pip install behave-html-pretty-formatter
```

#### 2. **Allure report keeps loading**

**Problem**: Opening HTML directly causes CORS issues

**Solution**:

```bash
# Use allure serve instead
allure serve reports/allure-results
```

#### 3. **Tests not executing with tags**

**Problem**: Running `behave -t @get` executes all tests

**Solution**: Use venv's behave:

```bash
venv/bin/behave -t @get --no-skipped
```

#### 4. **Virtual environment issues**

**Problem**: Packages installing globally instead of venv

**Solution**:

```bash
# Recreate venv
rm -rf venv
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### 5. **WebDriver errors**

**Problem**: ChromeDriver not found or version mismatch

**Solution**: The framework uses `webdriver-manager` which auto-downloads drivers. Ensure it's installed:

```bash
pip install webdriver-manager
```

---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 🚀 Quick Reference Guide

### Common Commands Cheat Sheet

```bash
# ===== INSTALLATION =====
python3.10 -m venv venv                    # Create virtual environment
source venv/bin/activate                   # Activate (macOS/Linux)
pip install -r requirements.txt            # Install dependencies

# ===== RUNNING TESTS (Makefile) =====
make help                                  # Show all available commands
make test-api                              # Run API tests
make test-ui                               # Run UI tests
make test                                  # Run all tests
make clean                                 # Clean reports and cache

# ===== RUNNING TESTS (Behave CLI) =====
behave -t @smoke                          # Run smoke tests
behave -t @api                            # Run API tests
behave -t @ui                             # Run UI tests
behave -t @regression                     # Run regression tests
behave -t @api -t @smoke                  # AND condition (both tags)
behave -t @api,@ui                        # OR condition (either tag)
behave -t ~@wip                           # Exclude work-in-progress

# ===== WITH ENVIRONMENTS =====
ENV=dev make test-api                     # Dev environment
ENV=staging behave -t @api                # Staging environment
ENV=prod behave -t @smoke                 # Production environment

# ===== VIEWING REPORTS =====
allure serve reports/allure-results       # Open Allure report
open reports/behave-html/report.html      # Open Behave report
./serve_allure.sh                         # Helper script for Allure

# ===== CLEANUP =====
make clean                                # Clean all reports
rm -rf reports/ logs/ __pycache__/        # Deep clean
```

### Report URLs

| Location                   | URL/Path                                                              |
| -------------------------- | --------------------------------------------------------------------- |
| **Local Behave Report**    | `reports/behave-html/report.html`                                     |
| **Local Allure Report**    | `allure serve reports/allure-results`                                 |
| **GitHub Pages Dashboard** | `https://YOUR_USERNAME.github.io/YOUR_REPO/`                          |
| **GitHub Pages Allure**    | `https://YOUR_USERNAME.github.io/YOUR_REPO/allure-report/`            |
| **GitHub Pages Behave**    | `https://YOUR_USERNAME.github.io/YOUR_REPO/behave-report/report.html` |
| **CI/CD Artifacts**        | GitHub → Actions → Workflow Run → Artifacts                           |

### Project Structure at a Glance

```
📁 features/          → BDD test scenarios (Gherkin)
📁 features/steps/    → Step implementations (Python)
📁 pages/             → Page Objects (UI automation)
📁 api/               → API clients
📁 config/            → Environment configurations
📁 utilities/         → Helper functions
📁 reports/           → Generated test reports
📁 logs/              → Execution logs
📄 Makefile           → Quick test commands
📄 requirements.txt   → Python dependencies
```

### Makefile Commands Explained

| Command         | What It Does                      | When to Use                            |
| --------------- | --------------------------------- | -------------------------------------- |
| `make help`     | Shows all available commands      | First time using framework             |
| `make install`  | Installs dependencies             | Initial setup or after pulling changes |
| `make test-api` | Runs API tests, generates reports | Testing API endpoints                  |
| `make test-ui`  | Runs UI tests, generates reports  | Testing web interfaces                 |
| `make test`     | Runs all tests                    | Full regression testing                |
| `make clean`    | Removes old reports and cache     | Before fresh test run                  |
| `make report`   | Generates and opens reports       | After manual behave run                |

### Test Tags Reference

| Tag           | Purpose              | Example Tests                   |
| ------------- | -------------------- | ------------------------------- |
| `@api`        | API/backend tests    | GET, POST, PUT, DELETE requests |
| `@ui`         | User interface tests | Login, navigation, forms        |
| `@smoke`      | Critical path tests  | Basic functionality check       |
| `@regression` | Full test suite      | Complete feature validation     |
| `@get`        | GET API requests     | Retrieve data operations        |
| `@post`       | POST API requests    | Create operations               |
| `@wip`        | Work in progress     | Tests under development         |

### GitHub Actions Workflow Triggers

| Trigger               | When It Runs | Default Tags | Publishes Reports      |
| --------------------- | ------------ | ------------ | ---------------------- |
| **Push to `main`**    | Automatic    | `@smoke`     | ✅ Yes (GitHub Pages)  |
| **Push to `develop`** | Automatic    | `@smoke`     | ❌ No (Artifacts only) |
| **Pull Request**      | Automatic    | `@smoke`     | ❌ No (Artifacts only) |
| **Manual Trigger**    | On demand    | Custom       | Depends on branch      |

### Environment Configuration Files

| File                               | Purpose     | Contains                    |
| ---------------------------------- | ----------- | --------------------------- |
| `config/environments/dev.yaml`     | Development | Dev URLs, test credentials  |
| `config/environments/staging.yaml` | Staging     | Staging URLs, test data     |
| `config/environments/prod.yaml`    | Production  | Production URLs (read-only) |

### Where to Find Things

| What You're Looking For | Location                        |
| ----------------------- | ------------------------------- |
| Test scenarios          | `features/api/`, `features/ui/` |
| Step definitions        | `features/steps/`               |
| Page objects            | `pages/`                        |
| API clients             | `api/`                          |
| Configuration           | `config/environments/`          |
| Reports                 | `reports/`                      |
| Logs                    | `logs/`                         |
| CI/CD workflow          | `.github/workflows/tests.yml`   |
| Dependencies            | `requirements.txt`              |

### Typical Workflows

#### 1. Daily Development Testing

```bash
# Pull latest code
git pull

# Run smoke tests
make test-api

# View results
# Allure server opens automatically
# Behave report opens in browser
```

#### 2. Pre-Commit Testing

```bash
# Run tests for your changes
ENV=dev behave -t @smoke

# Check results
open reports/behave-html/report.html

# If passed, commit
git add .
git commit -m "Your changes"
git push
```

#### 3. Full Regression (Local)

```bash
# Clean old reports
make clean

# Run everything
ENV=staging make test

# Review detailed Allure report
# Server starts automatically
```

#### 4. Testing Specific Feature

```bash
# Run specific feature file
behave features/api/user_api.feature

# Or with specific scenario
behave features/api/user_api.feature:10  # Line number
```

#### 5. CI/CD Deployment

```bash
# Push to main branch
git push origin main

# GitHub Actions automatically:
# 1. Runs smoke tests
# 2. Generates reports
# 3. Publishes to GitHub Pages
# 4. Makes artifacts available

# View live reports at:
# https://YOUR_USERNAME.github.io/YOUR_REPO/
```

### Troubleshooting Quick Fixes

| Issue                       | Solution                                       |
| --------------------------- | ---------------------------------------------- |
| `make: command not found`   | Install make: `brew install make` (macOS)      |
| `behave: command not found` | Use `venv/bin/behave` or activate venv         |
| `allure: command not found` | Install: `brew install allure` (macOS)         |
| Allure report shows blank   | Use `allure serve` instead of opening HTML     |
| Old test results showing    | Run `make clean` before tests                  |
| Browser not opening         | Check Chrome is installed, use `HEADLESS=true` |
| Permission denied           | Run `chmod +x run_tests.sh serve_allure.sh`    |

### Key Files to Know

| File                          | Purpose        | Edit When                 |
| ----------------------------- | -------------- | ------------------------- |
| `Makefile`                    | Test shortcuts | Adding new test targets   |
| `requirements.txt`            | Dependencies   | Adding new packages       |
| `features/environment.py`     | Test hooks     | Setup/teardown logic      |
| `.github/workflows/tests.yml` | CI/CD          | Changing automation       |
| `config/config.py`            | Config loader  | Changing config structure |

### Performance Tips

```bash
# Run tests in parallel (faster)
behave --processes 4 -t @api

# Run without Allure (faster)
behave -t @smoke --format pretty

# Headless browser (faster for UI)
HEADLESS=true behave -t @ui

# Skip specific tests
behave -t ~@slow -t @api
```

### Getting Help

```bash
# Behave help
behave --help

# Show available tags
behave --tags-help

# List all step definitions
behave --steps-catalog

# Dry run (validate without executing)
behave --dry-run -t @api

# Makefile help
make help
```

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Support

For issues and questions:

- 📧 Email: your-email@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/python-bdd-automation-framework/issues)
- 📖 Documentation: [Wiki](https://github.com/yourusername/python-bdd-automation-framework/wiki)

---

## Acknowledgments

- [Behave](https://behave.readthedocs.io/) - BDD framework for Python
- [Selenium](https://www.selenium.dev/) - Browser automation
- [Allure](https://docs.qameta.io/allure/) - Test reporting framework
- [Requests](https://requests.readthedocs.io/) - HTTP library for Python

```bash
# Create main directories
mkdir -p features/api features/ui features/steps
mkdir -p pages api config/environments utilities reports/allure-results reports/behave-html
mkdir -p tests logs data

# Create __init__.py files to make them packages
touch features/__init__.py pages/__init__.py api/__init__.py utilities/__init__.py tests/__init__.py

# On Windows use: type nul > features/__init__.py (and repeat for others)
```

---

## File Structure

```
python-bdd-automation-framework/
│
├── features/                           # BDD feature files
│   ├── __init__.py
│   ├── api/                           # API feature files
│   │   └── user_api.feature
│   ├── ui/                            # UI feature files
│   │   └── login.feature
│   ├── steps/                         # Step definitions
│   │   ├── __init__.py
│   │   ├── api_steps.py
│   │   └── ui_steps.py
│   └── environment.py                 # Behave hooks
│
├── pages/                             # Page Object Model
│   ├── __init__.py
│   ├── base_page.py
│   └── login_page.py
│
├── api/                               # API clients
│   ├── __init__.py
│   └── base_api_client.py
│
├── config/                            # Configuration files
│   ├── config.py
│   └── environments/
│       ├── dev.yaml
│       ├── staging.yaml
│       └── prod.yaml
│
├── utilities/                         # Helper functions
│   ├── __init__.py
│   ├── logger.py
│   ├── screenshot_helper.py
│   └── data_generator.py
│
├── reports/                           # Test reports
│   ├── allure-results/
│   └── behave-html/
│
├── tests/                             # Non-BDD pytest tests (optional)
│   └── __init__.py
│
├── logs/                              # Execution logs
│
├── data/                              # Test data files
│   └── test_data.json
│
├── requirements.txt                   # Dependencies
├── behave.ini                         # Behave configuration
├── pytest.ini                         # Pytest configuration
├── .gitignore
├── README.md
└── run_tests.sh                       # Test execution script
```

---

## Step-by-Step Implementation

### Step 4: Create requirements.txt

Your updated `requirements.txt` is already provided with latest versions.

Install dependencies:

```bash
pip install -r requirements.txt
```

### Step 5: Install Allure (for Reports)

**Windows (using Scoop):**

```bash
scoop install allure
```

**Mac:**

```bash
brew install allure
```

**Linux:**

```bash
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update
sudo apt-get install allure
```

**Verify Allure installation:**

```bash
allure --version
```

---

### Step 6: Create Configuration Files

#### config/config.py

```python
import os
import yaml
from pathlib import Path

class Config:
    # Project paths
    BASE_DIR = Path(__file__).resolve().parent.parent
    CONFIG_DIR = BASE_DIR / 'config'
    REPORTS_DIR = BASE_DIR / 'reports'
    LOGS_DIR = BASE_DIR / 'logs'
    DATA_DIR = BASE_DIR / 'data'

    # Browser settings
    BROWSER = os.getenv('BROWSER', 'chrome')
    HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'

    # Timeout settings
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 20
    PAGE_LOAD_TIMEOUT = 30

    # Screenshot settings
    SCREENSHOT_ON_FAILURE = True

    # Environment
    ENV = os.getenv('ENV', 'dev')

    @classmethod
    def load_environment_config(cls):
        """Load environment-specific configuration"""
        env_file = cls.CONFIG_DIR / 'environments' / f'{cls.ENV}.yaml'
        if env_file.exists():
            with open(env_file, 'r') as f:
                return yaml.safe_load(f)
        return {}

    @classmethod
    def get_base_url(cls):
        env_config = cls.load_environment_config()
        return env_config.get('base_url', 'https://example.com')

    @classmethod
    def get_api_base_url(cls):
        env_config = cls.load_environment_config()
        return env_config.get('api_base_url', 'https://api.example.com')
```

#### config/environments/dev.yaml

```yaml
environment: dev
base_url: https://dev.example.com
api_base_url: https://api-dev.example.com
credentials:
  username: testuser@example.com
  password: TestPass123
database:
  host: localhost
  port: 5432
timeout:
  api: 30
  ui: 20
```

#### config/environments/staging.yaml

```yaml
environment: staging
base_url: https://staging.example.com
api_base_url: https://api-staging.example.com
credentials:
  username: testuser@example.com
  password: TestPass123
timeout:
  api: 30
  ui: 20
```

#### config/environments/prod.yaml

```yaml
environment: prod
base_url: https://www.example.com
api_base_url: https://api.example.com
credentials:
  username: produser@example.com
  password: ProdPass123
timeout:
  api: 30
  ui: 20
```

---

### Step 7: Create Utility Files

#### utilities/logger.py

```python
import logging
import colorlog
from pathlib import Path
from datetime import datetime

class Logger:
    @staticmethod
    def get_logger(name):
        """Create and configure logger with color support"""
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        # Avoid adding handlers multiple times
        if logger.handlers:
            return logger

        # Create logs directory if not exists
        log_dir = Path(__file__).resolve().parent.parent / 'logs'
        log_dir.mkdir(exist_ok=True)

        # File handler
        log_file = log_dir / f'test_execution_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)

        # Console handler with colors
        console_handler = colorlog.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Formatters
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        console_formatter = colorlog.ColoredFormatter(
            '%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red,bg_white',
            }
        )

        file_handler.setFormatter(file_formatter)
        console_handler.setFormatter(console_formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger
```

#### utilities/screenshot_helper.py

```python
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
```

#### utilities/data_generator.py

```python
from faker import Faker

class DataGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate_user_data(self):
        """Generate random user data"""
        return {
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name(),
            'email': self.fake.email(),
            'phone': self.fake.phone_number(),
            'address': self.fake.address(),
            'company': self.fake.company(),
            'job_title': self.fake.job()
        }

    def generate_email(self):
        return self.fake.email()

    def generate_password(self, length=12):
        return self.fake.password(length=length, special_chars=True, digits=True, upper_case=True, lower_case=True)

    def generate_name(self):
        return self.fake.name()

    def generate_address(self):
        return self.fake.address()

    def generate_phone(self):
        return self.fake.phone_number()
```

---

### Step 8: Create Base Page Object

#### pages/base_page.py

```python
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
```

#### pages/login_page.py

```python
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
```

---

### Step 9: Create API Client

#### api/base_api_client.py

```python
import requests
import allure
import json
from utilities.logger import Logger
from config.config import Config

class BaseAPIClient:
    def __init__(self):
        self.base_url = Config.get_api_base_url()
        self.session = requests.Session()
        self.logger = Logger.get_logger(self.__class__.__name__)
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def _log_request(self, method, url, **kwargs):
        """Log request details"""
        self.logger.info(f"{method} request to: {url}")
        if 'json' in kwargs:
            self.logger.debug(f"Request body: {json.dumps(kwargs['json'], indent=2)}")
        if 'params' in kwargs:
            self.logger.debug(f"Query params: {kwargs['params']}")

    def _log_response(self, response):
        """Log response details"""
        self.logger.info(f"Response status: {response.status_code}")
        try:
            self.logger.debug(f"Response body: {json.dumps(response.json(), indent=2)}")
        except:
            self.logger.debug(f"Response text: {response.text}")

    @allure.step("Send GET request to {endpoint}")
    def get(self, endpoint, params=None, headers=None):
        """Send GET request"""
        url = f"{self.base_url}{endpoint}"
        request_headers = {**self.headers, **(headers or {})}

        self._log_request("GET", url, params=params)
        response = self.session.get(url, params=params, headers=request_headers)
        self._log_response(response)

        # Attach to Allure
        allure.attach(
            f"URL: {url}\nMethod: GET\nParams: {params}",
            name="Request Details",
            attachment_type=allure.attachment_type.TEXT
        )

        return response

    @allure.step("Send POST request to {endpoint}")
    def post(self, endpoint, data=None, json=None, headers=None):
        """Send POST request"""
        url = f"{self.base_url}{endpoint}"
        request_headers = {**self.headers, **(headers or {})}

        self._log_request("POST", url, json=json, data=data)
        response = self.session.post(url, data=data, json=json, headers=request_headers)
        self._log_response(response)

        # Attach to Allure
        if json:
            allure.attach(
                f"Request Body:\n{json}",
                name="POST Request Body",
                attachment_type=allure.attachment_type.JSON
            )

        return response

    @allure.step("Send PUT request to {endpoint}")
    def put(self, endpoint, data=None, json=None, headers=None):
        """Send PUT request"""
        url = f"{self.base_url}{endpoint}"
        request_headers = {**self.headers, **(headers or {})}

        self._log_request("PUT", url, json=json, data=data)
        response = self.session.put(url, data=data, json=json, headers=request_headers)
        self._log_response(response)

        return response

    @allure.step("Send PATCH request to {endpoint}")
    def patch(self, endpoint, data=None, json=None, headers=None):
        """Send PATCH request"""
        url = f"{self.base_url}{endpoint}"
        request_headers = {**self.headers, **(headers or {})}

        self._log_request("PATCH", url, json=json, data=data)
        response = self.session.patch(url, data=data, json=json, headers=request_headers)
        self._log_response(response)

        return response

    @allure.step("Send DELETE request to {endpoint}")
    def delete(self, endpoint, headers=None):
        """Send DELETE request"""
        url = f"{self.base_url}{endpoint}"
        request_headers = {**self.headers, **(headers or {})}

        self._log_request("DELETE", url)
        response = self.session.delete(url, headers=request_headers)
        self._log_response(response)

        return response

    def set_auth_token(self, token):
        """Set authentication token"""
        self.headers['Authorization'] = f'Bearer {token}'
        self.logger.info("Authentication token set")

    def set_header(self, key, value):
        """Set custom header"""
        self.headers[key] = value
        self.logger.info(f"Header set: {key}={value}")

    def clear_headers(self):
        """Clear all custom headers"""
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.logger.info("Headers cleared")
```

---

### Step 10: Create Feature Files

#### features/ui/login.feature

```gherkin
Feature: User Login Functionality
  As a user
  I want to log into the application
  So that I can access my account

  Background:
    Given I am on the login page

  @smoke @ui @positive
  Scenario: Successful login with valid credentials
    When I enter username "testuser@example.com"
    And I enter password "TestPass123"
    And I click the login button
    Then I should be redirected to the dashboard
    And I should see the welcome message

  @ui @negative
  Scenario: Login fails with invalid password
    When I enter username "testuser@example.com"
    And I enter password "wrongpassword"
    And I click the login button
    Then I should see an error message "Invalid credentials"
    And I should remain on the login page

  @ui @negative
  Scenario: Login fails with empty username
    When I enter username ""
    And I enter password "TestPass123"
    And I click the login button
    Then I should see an error message "Username is required"

  @ui @negative
  Scenario: Login fails with empty password
    When I enter username "testuser@example.com"
    And I enter password ""
    And I click the login button
    Then I should see an error message "Password is required"

  @ui @negative
  Scenario Outline: Login with various invalid credentials
    When I enter username "<username>"
    And I enter password "<password>"
    And I click the login button
    Then I should see an error message "<error_message>"

    Examples:
      | username              | password    | error_message           |
      | invalid@example.com   | TestPass123 | Invalid credentials     |
      | testuser@example.com  | short       | Invalid credentials     |
      | notanemail            | TestPass123 | Invalid email format    |
```

#### features/api/user_api.feature

```gherkin
Feature: User API Operations
  As an API client
  I want to perform CRUD operations on users
  So that I can manage user data

  @smoke @api @get
  Scenario: Get user details by ID
    Given I have a valid authentication token
    When I send a GET request to "/api/users/1"
    Then the response status code should be 200
    And the response should contain user details
    And the response should have field "id" with value "1"
    And the response should have field "email"

  @api @post @positive
  Scenario: Create a new user
    Given I have a valid authentication token
    And I have user data with:
      | first_name | John           |
      | last_name  | Doe            |
      | email      | john@test.com  |
    When I send a POST request to "/api/users"
    Then the response status code should be 201
    And the response should contain field "id"
    And the response should have field "email" with value "john@test.com"

  @api @put @positive
  Scenario: Update existing user
    Given I have a valid authentication token
    When I send a PUT request to "/api/users/1" with data:
      | first_name | Jane  |
      | last_name  | Smith |
    Then the response status code should be 200
    And the response should have field "first_name" with value "Jane"
    And the response should have field "last_name" with value "Smith"

  @api @delete @positive
  Scenario: Delete existing user
    Given I have a valid authentication token
    When I send a DELETE request to "/api/users/999"
    Then the response status code should be 204

  @api @delete @negative
  Scenario: Delete non-existent user
    Given I have a valid authentication token
    When I send a DELETE request to "/api/users/99999"
    Then the response status code should be 404

  @api @get @negative
  Scenario: Get user without authentication
    Given I do not have an authentication token
    When I send a GET request to "/api/users/1"
    Then the response status code should be 401
    And the response should have field "error" with value "Unauthorized"

  @regression @api
  Scenario: Get list of all users
    Given I have a valid authentication token
    When I send a GET request to "/api/users"
    Then the response status code should be 200
    And the response should be an array
    And the response array should not be empty
```

---

### Step 11: Create Step Definitions

#### features/steps/ui_steps.py

```python
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
```

#### features/steps/api_steps.py

```python
from behave import given, when, then
import json
import allure
from api.base_api_client import BaseAPIClient

@given('I have a valid authentication token')
def step_set_auth_token(context):
    """Set valid authentication token"""
    context.api_client = BaseAPIClient()
    # In real scenario, get token from login API
    context.api_client.set_auth_token("mock_token_12345")

@given('I do not have an authentication token')
def step_no_auth_token(context):
    """Initialize API client without auth token"""
    context.api_client = BaseAPIClient()

@given('I have user data with')
def step_prepare_user_data(context):
    """Prepare user data from table"""
    context.user_data = {}
    for row in context.table:
        context.user_data[row['first_name']] = row['last_name']

@when('I send a GET request to "{endpoint}"')
def step_send_get_request(context, endpoint):
    """Send GET request"""
    context.response = context.api_client.get(endpoint)

    # Attach to



    #Execution

    venv/bin/behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results -f behave_html_formatter:HTMLFormatter -o reports/behave-html/report.html -t @get
allure generate reports/allure-results -o reports/allure-report --clean

1.  rm -rf venv
2. python3.10 -m venv venv
2. python3.10 -m venv venv
3. source venv/bin/activate
python -m ensurepip --upgrade
pip install --upgrade pip setuptools wheel
4.pip install -r requirements.txt
pip install behave behave-html-formatter==0.9.9
5.behave -t @get




    behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results -f behave_html_formatter:HTMLFormatter -o reports/behave-html/report.html -t @get
```
