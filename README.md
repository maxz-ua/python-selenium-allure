# Python Selenium Allure Test Framework

This repository contains an automated test framework using Python, Selenium WebDriver, Pytest, and Allure for reporting. The framework demonstrates a clean Page Object Model (POM) structure and includes smoke, sanity, and regression test stages, all integrated with GitHub Actions CI.

## Features
- **Selenium WebDriver** for browser automation
- **Pytest** for test execution and fixtures
- **Allure** for rich, interactive test reports
- **Page Object Model (POM)** for maintainable test code
- **Test markers** for smoke, sanity, and regression suites
- **GitHub Actions** for CI/CD with staged test execution and Allure report publishing

## Project Structure
```
.
├── pages/                # Page Object classes
│   └── base_page.py      # BasePage and GoogleMainPage
├── tests/                # Test cases
│   ├── test_google_search_smoke.py
│   ├── test_google_search_sanity.py
│   ├── test_google_search_regression.py
│   └── test_google_search_failed.py
├── conftest.py           # Pytest fixtures
├── requirements.txt      # Python dependencies
├── pytest.ini            # Pytest configuration
└── .github/workflows/    # GitHub Actions workflow
```

## Getting Started

### Prerequisites
- Python 3.8+
- Google Chrome or Firefox browser
- ChromeDriver or GeckoDriver in your PATH

### Install dependencies
```bash
pip install -r requirements.txt
```

## Running Tests Locally

Run all tests:
```bash
pytest --alluredir=allure-results
```

Run only smoke, sanity, or regression tests:
```bash
pytest -m smoke --alluredir=allure-results
pytest -m sanity --alluredir=allure-results
pytest -m regression --alluredir=allure-results
```

## Viewing Allure Reports Locally
1. Install the Allure CLI:
   - [Download from Allure](https://docs.qameta.io/allure/#_get_started)
   - Or use [Scoop](https://scoop.sh/) or [Chocolatey](https://chocolatey.org/):
     ```bash
     scoop install allure
     # or
     choco install allure.commandline
     ```
2. Generate and open the report:
   ```bash
   allure serve allure-results
   ```

## Continuous Integration

This project uses [GitHub Actions](https://github.com/features/actions) for CI/CD:
- Runs smoke, sanity, and regression tests in order
- Generates and uploads an Allure report as an artifact
- Can be triggered manually or on a schedule

You can view workflow runs and download the Allure report from the [Actions tab](../../actions).

---

Feel free to contribute or adapt this framework for your own testing needs! 