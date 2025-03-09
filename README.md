[![CI](https://github.com/norgeitall/norgeitall/actions/workflows/ci.yml/badge.svg)](https://github.com/norgeitall/norgeitall/actions) [![Netlify Status](https://api.netlify.com/api/v1/badges/de5a3ecd-f354-43e0-82bd-53f9555a0f16/deploy-status)](https://app.netlify.com/sites/norgeitall/deploys)

# Norge i tall

_Norge i tall_ is built on [Evidence - Business Intelligence as Code](https://evidence.dev/). In addition, we use Python to build data sources.

## How it works

[`main.py`](main.py) fetches data from APIs and websites such as OECD’s and Norges Bank’s. It then stores this data as CSV files in [`sources/oecd/`](sources/oecd), [`sources/norges_bank`](sources/norges_bank), and so on.

Then, Evidence makes these CSV files available to query with SQL, and builds the website based on Markdown files.

## Development environment setup

### Prerequisites

1. Python package and project manager [uv](https://docs.astral.sh/uv/)
2. JavaScript runtime environment [Node.js](https://nodejs.org/en)

If you use [Homebrew](https://brew.sh/), simply run `brew install uv node`.

### Setup

```bash
git clone git@github.com:norgeitall/norgeitall.git  # Clone the repository
cd norgeitall  # Navigate into the project folder
uv sync  # Install Python dependencies
npm install  # Install Node.js dependencies
source .venv/bin/activate  # Activate Python virtual environment
pre-commit install  # Install pre-commit hooks
pre-commit run --all-files  # Run automatic quality checks
./main.py  # Fetch data and store in CSV files
npm run sources  # Extract data from sources
npm run dev  # Start development server
```

[http://localhost:3000/](http://localhost:3000/) should now be opened in your default browser.
