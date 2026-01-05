# Getting Started - Complete Checklist

Follow this checklist to set up and start using the framework.

## ✅ Setup Checklist

### 1. Prerequisites Installation

- [ ] Install Python 3.10: `python3.10 --version`
- [ ] Install Git: `git --version`
- [ ] Install Allure: `allure --version`
- [ ] Install Chrome browser (for UI tests)
- [ ] Have a code editor (VS Code recommended)

### 2. Project Setup

```bash
# Clone or download the project
cd python-bdd-automation-framework

# Create virtual environment
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
venv/bin/behave --version
allure --version
```

- [ ] Virtual environment created and activated
- [ ] All dependencies installed successfully
- [ ] Behave and Allure commands work

### 3. Configuration

- [ ] Review `config/environments/dev.yaml` and update API URLs
- [ ] Update base URLs in environment files if needed
- [ ] Configure credentials (if testing real APIs)

### 4. First Test Run

```bash
# Run a simple test
venv/bin/behave -t @get

# View Behave HTML report
open reports/behave-html/report.html

# View Allure report
allure serve reports/allure-results
```

- [ ] Tests executed successfully
- [ ] Behave HTML report generated
- [ ] Allure report opened in browser

### 5. GitHub Setup (Optional)

```bash
# Initialize git repository
git init
git add .
git commit -m "Initial commit"

# Create GitHub repository and push
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

- [ ] Code pushed to GitHub
- [ ] GitHub Actions workflow visible in Actions tab
- [ ] First workflow run completed successfully

### 6. Enable GitHub Pages (Optional)

- [ ] Go to Settings → Pages
- [ ] Select "GitHub Actions" as source
- [ ] Wait for workflow to complete
- [ ] Access report at `https://YOUR_USERNAME.github.io/YOUR_REPO/`

---

## 🚀 Quick Commands Reference

### Running Tests

```bash
# Recommended: Use Makefile
make test-api        # Run API tests
make test-ui         # Run UI tests
make test            # Run all tests
make clean           # Clean reports

# Manual commands
venv/bin/behave -t @smoke                    # Smoke tests
venv/bin/behave -t @api                      # API tests
venv/bin/behave -t @ui                       # UI tests
venv/bin/behave -t @regression               # Full suite

# With environment
ENV=staging venv/bin/behave -t @api
```

### Viewing Reports

```bash
# Behave HTML (simple)
open reports/behave-html/report.html

# Allure (recommended)
allure serve reports/allure-results

# Helper script
./serve_allure.sh
```

### Development

```bash
# Activate environment
source venv/bin/activate

# Run specific feature
venv/bin/behave features/api/user_api.feature

# Run with verbose output
venv/bin/behave -t @api --no-capture

# List all steps
venv/bin/behave --steps

# Dry run (no execution)
venv/bin/behave --dry-run
```

---

## 📝 Next Steps

### For Test Development

1. **Create new feature file**:

   ```bash
   touch features/api/new_feature.feature
   ```

2. **Write scenarios** in Gherkin syntax

3. **Implement steps** in `features/steps/`

4. **Run and validate**:
   ```bash
   venv/bin/behave features/api/new_feature.feature
   ```

### For API Testing

1. Update `config/environments/dev.yaml` with your API base URL
2. Create feature file in `features/api/`
3. Use existing steps in `features/steps/api_steps.py`
4. Run: `venv/bin/behave -t @api`

### For UI Testing

1. Create page object in `pages/`
2. Create feature file in `features/ui/`
3. Implement steps in `features/steps/ui_steps.py`
4. Run: `venv/bin/behave -t @ui`

### For CI/CD

1. Push code to GitHub
2. Check Actions tab for workflow runs
3. Configure GitHub Pages for report hosting
4. Set up notifications (optional)

---

## 📚 Documentation

- **README.md** - Complete framework documentation
- **QUICK_START.md** - Quick reference guide
- **GITHUB_ACTIONS.md** - CI/CD setup and usage
- **FrameworkInstructions.md** - Detailed implementation guide

---

## 🆘 Troubleshooting

### Issue: `behave: command not found`

**Solution**: Use `venv/bin/behave` instead of just `behave`

### Issue: Reports not generating

**Solution**:

```bash
# Ensure using venv's behave
venv/bin/behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results \
                -f behave_html_pretty_formatter:PrettyHTMLFormatter -o reports/behave-html/report.html \
                -t @get
```

### Issue: Allure report loading forever

**Solution**: Use `allure serve reports/allure-results` instead of opening HTML directly

### Issue: Python packages not found

**Solution**:

```bash
# Ensure venv is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
pip install behave-html-pretty-formatter
```

### Issue: ChromeDriver errors

**Solution**: The framework auto-downloads drivers via `webdriver-manager`. Ensure it's installed:

```bash
pip install webdriver-manager
```

---

## 💡 Pro Tips

1. **Use tags effectively**:

   ```bash
   venv/bin/behave -t @smoke          # Quick validation
   venv/bin/behave -t @api,@ui        # Multiple categories
   venv/bin/behave -t @api -t ~@wip   # Exclude WIP
   ```

2. **View step definitions**:

   ```bash
   venv/bin/behave --steps
   venv/bin/behave --steps-catalog    # User-friendly format
   ```

3. **Debug failing tests**:

   ```bash
   venv/bin/behave -t @failing --no-capture  # See print statements
   venv/bin/behave --no-skipped              # Hide skipped scenarios
   ```

4. **Generate test data**:

   ```python
   from utilities.data_generator import DataGenerator
   user_data = DataGenerator().generate_user_data()
   ```

5. **Environment variables**:
   ```bash
   HEADLESS=true venv/bin/behave -t @ui       # Headless browser
   ENV=staging venv/bin/behave -t @api        # Change environment
   OPEN_REPORT=true venv/bin/behave -t @smoke # Auto-open reports
   ```

---

## ✅ You're Ready!

If you completed all checkboxes above, you're ready to:

- ✅ Write BDD tests
- ✅ Execute tests locally
- ✅ Generate reports
- ✅ Push to GitHub
- ✅ Run tests in CI/CD
- ✅ View results on GitHub Pages

**Happy Testing! 🎉**
