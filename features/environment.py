# File: `features/environment.py`
import os
import subprocess
import shutil

def before_all(context):
    # allow overrides via behave userdata (e.g. -D reports_dir=custom)
    userdata = getattr(context, "config", None) and getattr(context.config, "userdata", {}) or {}
    reports_dir = userdata.get("reports_dir", "reports")
    context.reports_dir = os.path.abspath(reports_dir)
    context.allure_results = os.path.join(context.reports_dir, userdata.get("allure_results_dir", "allure-results"))
    context.allure_report = os.path.join(context.reports_dir, userdata.get("allure_report_dir", "allure-report"))
    # Always expect Behave HTML at reports/behave-html/report.html
    context.html_report = os.path.join(context.reports_dir, "behave-html", "report.html")

    # Clean old Allure report (not results) and create directories
    print("Preparing reports directories...")
    if os.path.isdir(context.allure_report):
        try:
            shutil.rmtree(context.allure_report)
            print(f"Removed old Allure report: {context.allure_report}")
        except Exception as e:
            print(f"Failed to remove {context.allure_report}: {e}")

    # Create fresh directories
    os.makedirs(context.allure_results, exist_ok=True)
    os.makedirs(context.reports_dir, exist_ok=True)
    os.makedirs(os.path.dirname(context.html_report), exist_ok=True)

    print(f"Reports directory: {context.reports_dir}")
    print(f"Expecting Allure results in: {context.allure_results}")
    print(f"Expecting Behave HTML at: {context.html_report}")

def after_all(context):
    print("\n" + "="*60)
    print("POST-RUN REPORT GENERATION")
    print("="*60)
    
    # show what's in the results folder for debugging
    if os.path.isdir(context.allure_results):
        items = os.listdir(context.allure_results)
        print(f"\nAllure results folder contents ({context.allure_results}): {len(items)} items")
        if items:
            for i, f in enumerate(items[:10], 1):
                print(f"  {i}. {f}")
        else:
            print("  (empty - no Allure results generated)")
    else:
        print(f"\nNo Allure results folder found at {context.allure_results}")

    # Check Behave HTML
    if os.path.isfile(context.html_report):
        size = os.path.getsize(context.html_report)
        print(f"\nBehave HTML report: {context.html_report} ({size} bytes)")
    else:
        print(f"\nNo Behave HTML report found at: {context.html_report}")
        print("Make sure you ran behave with: -f behave_html_formatter:HTMLFormatter -o reports/behave-html/report.html")

    # Check if Allure results exist
    allure_results_available = False
    if os.path.isdir(context.allure_results) and os.listdir(context.allure_results):
        items = os.listdir(context.allure_results)
        print(f"\n✓ Allure results generated: {len(items)} files")
        allure_results_available = True
    else:
        print("\n✗ No Allure results to generate report from.")
        print("Make sure you ran behave with:")
        print("  behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results ...")

    # Summary
    print("\n" + "="*60)
    print("AVAILABLE REPORTS:")
    print("="*60)
    if allure_results_available:
        print(f"✓ Allure Results: {context.allure_results}")
        print(f"  To view: allure serve {context.allure_results}")
    if os.path.isfile(context.html_report):
        print(f"✓ Behave HTML: {context.html_report}")
    print("="*60 + "\n")

    # optionally open reports
    open_report_env = os.environ.get("OPEN_REPORT", "") or (getattr(context.config, "userdata", {}) or {}).get("open_report", "")
    if str(open_report_env).lower() in ("1", "true", "yes"):
        if os.path.isfile(context.html_report):
            try:
                subprocess.run(["open", context.html_report])
            except Exception as e:
                print(f"Failed to open Behave HTML report: {e}")
        if allure_results_available:
            print("\nStarting Allure server...")
            print("(This will open in your browser automatically)")
            try:
                subprocess.run(["allure", "serve", context.allure_results])
            except Exception as e:
                print(f"Failed to start Allure server: {e}")
                print(f"Run manually: allure serve {context.allure_results}")
