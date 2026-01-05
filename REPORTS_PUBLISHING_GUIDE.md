# Publishing Both Allure and Behave Reports to GitHub Pages

## Overview

Your GitHub workflow has been updated to publish **both Allure and Behave HTML reports** to GitHub Pages. When tests run on the `main` branch, both reports are automatically deployed to your GitHub Pages site.

## What Was Updated

### 1. Workflow Changes (`.github/workflows/tests.yml`)

The workflow now:

✅ **Creates a unified landing page** with links to both reports
✅ **Organizes reports** in separate directories:

- `allure-report/` - Allure test report
- `behave-report/` - Behave HTML report

✅ **Deploys to GitHub Pages** using the `deploy-reports` job (renamed from `deploy-report`)

### 2. Report Structure on GitHub Pages

After deployment, your reports will be accessible at:

```
https://YOUR_USERNAME.github.io/YOUR_REPO/
├── index.html (Landing page with links to both reports)
├── allure-report/
│   └── index.html (Allure report)
└── behave-report/
    └── report.html (Behave report)
```

## How to Enable

### Step 1: Configure GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** → **Pages**
3. Under "Source", select **GitHub Actions**
4. Click **Save**

### Step 2: Push to Main Branch

```bash
git add .
git commit -m "Update workflow to publish both reports"
git push origin main
```

### Step 3: Wait for Workflow

1. Go to **Actions** tab in your repository
2. Wait for the workflow to complete
3. The `deploy-reports` job will publish to GitHub Pages

### Step 4: Access Your Reports

Visit: `https://YOUR_USERNAME.github.io/YOUR_REPO/`

You'll see a dashboard with two cards:

- **📊 Allure Report** - Click to view detailed test analytics
- **📝 Behave HTML Report** - Click to view BDD scenario reports

## Features

### Landing Page Dashboard

A professional landing page displays:

- Test reports title and description
- Two report cards with descriptions
- Direct links to each report
- Responsive design that works on mobile and desktop

### Automatic Updates

- Reports update automatically when tests run on the `main` branch
- Pull requests and other branches don't trigger deployment (but reports are still available as artifacts)
- Both reports are always in sync from the same test run

## Troubleshooting

### Reports Not Showing

1. **Check GitHub Pages is enabled**

   - Settings → Pages → Source should be "GitHub Actions"

2. **Check workflow permissions**

   - Settings → Actions → General → Workflow permissions
   - Should be "Read and write permissions" OR
   - Should have "pages: write" and "id-token: write" permissions

3. **Verify workflow ran successfully**
   - Go to Actions tab
   - Check both `test` and `deploy-reports` jobs completed

### 404 Error

- Wait 1-2 minutes after deployment completes
- GitHub Pages may take time to propagate
- Check the workflow logs for any errors

### Reports Not Updating

- Deployment only happens on `main` branch
- Check you pushed to the correct branch
- Verify the `deploy-reports` job executed

## Accessing Reports as Artifacts

Even if you don't use GitHub Pages, reports are available as downloadable artifacts:

1. Go to **Actions** → Select workflow run
2. Scroll to **Artifacts** section
3. Download:
   - `behave-html-report`
   - `allure-report`
   - `allure-results`
   - `test-logs`

## Customization

### Change Landing Page Style

Edit the HTML in the workflow's "Create index page" step in [.github/workflows/tests.yml](.github/workflows/tests.yml)

### Add More Reports

To add additional reports to GitHub Pages:

1. Upload them as artifacts in the `test` job
2. Download them in the `deploy-reports` job
3. Copy them to the `gh-pages/` directory
4. Update the index.html to link to them

## URLs Quick Reference

Replace `YOUR_USERNAME` and `YOUR_REPO` with your actual values:

| Report         | URL                                                                   |
| -------------- | --------------------------------------------------------------------- |
| Main Dashboard | `https://YOUR_USERNAME.github.io/YOUR_REPO/`                          |
| Allure Report  | `https://YOUR_USERNAME.github.io/YOUR_REPO/allure-report/`            |
| Behave Report  | `https://YOUR_USERNAME.github.io/YOUR_REPO/behave-report/report.html` |

## Next Steps

1. ✅ Enable GitHub Pages (if not already done)
2. ✅ Push changes to `main` branch
3. ✅ Wait for workflow to complete
4. ✅ Access your reports dashboard
5. 🎉 Share the URL with your team!

---

**Note**: Reports are published only when tests run on the `main` branch. For other branches, reports are available as workflow artifacts.
