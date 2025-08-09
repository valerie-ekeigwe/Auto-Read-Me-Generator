# Auto ReadMe Generator

The **Auto ReadMe Generator** is a Python powered tool that scans your local project, pulls key details from GitHub, and builds a professional, ready-to-use `README.md` file in seconds.  
Perfect for keeping your repos clean, consistent, and portfolio ready.

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Open Source](https://img.shields.io/badge/Open%20Source-Yes-brightgreen?style=for-the-badge&logo=github)

---

## What’s New in This Version

- Complete **CLI refactor** for a smoother workflow  
- Support for **multiple templates** (e.g., minimal, webapp)  
- Cleaner, more natural README templates  
- Better GitHub metadata integration  
- Lighter dependencies and improved structure  

---

## Features

- **Smart project scanning** : detects your tech stack and whether tests exist  
- **Live GitHub stats** : pulls stars, forks, watchers, and main language  
- **Markdown templates** : choose from different layouts for your README  
- **Customizable output** : run in dry mode to preview before saving  

---

## Getting Started

> You’ll need a [GitHub Personal Access Token](https://github.com/settings/tokens) in a `.env` file to pull repository stats.

### 1. Clone this repo

```bash
git clone https://github.com/valerie-ekeigwe/Auto-Read-Me-Generator.git
cd Auto-Read-Me-Generator
```

### 2. Set up your `.env` file

Copy the example file and fill in your GitHub token:

```bash
cp .env.example .env
```

```env
GITHUB_TOKEN=your_personal_access_token_here
```

### 3. Create a virtual environment and install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate   # Mac/Linux
pip install -r requirements.txt
```

### 4. Run the generator

```bash
python3 -m src.cli --repo /path/to/project --template minimal
```

Add `--dry-run` to preview without saving:

```bash
python3 -m src.cli --repo /path/to/project --template webapp --dry-run
```

---

## Example Output

```md
# My Project Name

Short project description goes here.

## Tech Stack
Python, Flask

## GitHub
- Stars: 10
- Forks: 2
- Watchers: 5
- Primary language: Python

## Tests
Tests are present in this repository.
```

---

## Project Structure

```
Auto-Read-Me-Generator/
├── src/
│   ├── cli.py               # CLI entry point
│   ├── github_api.py        # GitHub API integration
│   ├── scanner.py           # Local project scanning
│   └── readme_generator.py  # Template rendering
├── templates/
│   ├── minimal.md.j2
│   └── webapp.md.j2
├── tests/
│   ├── test_cli_smoke.py
│   └── test_scanner.py
├── requirements.txt
└── .env.example
```

---

## Contributing

Improvements are always welcome.  
You can help by adding more templates, improving tech stack detection, or refining GitHub integration.  

---

## License

Licensed under the [MIT License](LICENSE).
