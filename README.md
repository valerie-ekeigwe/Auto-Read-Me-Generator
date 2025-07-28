# 🤖 Auto ReadMe Generator

Welcome to the **Auto ReadMe Generator** It ia a Python powered tool that scans your local GitHub project and GitHub metadata to generate a clean, informative, and stylish `README.md` file automatically!

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Open Source](https://img.shields.io/badge/Open--Source-Yes-brightgreen?style=for-the-badge&logo=github)

---

## ✨ Features

- 🧠 **Intelligent project scanning** — detects tech stack and test presence
- 🔗 **GitHub integration** — pulls real-time stars, forks, watchers, language
- 📄 **Templated Markdown output** — generates a clean, styled README file
- 💬 **Future: AI summary of project purpose (Coming Soon)**

---

## 🚀 Quick Start

> **IMPORTANT:** Requires a GitHub [Personal Access Token (PAT)](https://github.com/settings/tokens) saved in a `.env` file.

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/valerie-ekeigwe/Auto-Read-Me-Generator.git
cd Auto-Read-Me-Generator
```

### 2️⃣ Create a `.env` file

Duplicate `.env.example` and rename it to `.env`:

```bash
cp .env.example .env
```

Then add your GitHub token:

```env
GITHUB_TOKEN=your_personal_access_token_here
```

### 3️⃣ Set up the virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4️⃣ Configure the generator

Open `generate.py` and update the `Args` class to match your local setup:

```python
class Args:
    repo = "/Users/yourname/Path/To/Your/ClonedRepo"  # local path
    github_user = "your-github-username"
    repo_name = "your-repo-name"
```

Make sure the project you're scanning is cloned locally and publicly visible on GitHub.

### 5️⃣ Run the generator

```bash
python generate.py
```

🎉 A new `README.md` will be created or overwritten in your project folder.

---

## 📂 Project Structure

```
Auto-Read-Me-Generator/
├── generate.py                # Main script to run
├── .env.example               # Example environment config
├── requirements.txt           # Dependencies
├── templates/
│   └── README_template.md     # Markdown template used for generation
├── src/
│   ├── github_api.py          # GitHub metadata fetcher
│   ├── scanner.py             # Local project analyzer
│   ├── readme_generator.py    # Markdown renderer
│   ├── ai_generator.py        # (future) AI-powered descriptions
│   └── cli.py                 # (optional) CLI interface
```

---

## 📦 Example Output

Here's an example snippet from an auto-generated README:

```md
# My Cool Project

A modern web landing page using HTML, CSS, and JavaScript.

## 🧰 Tech Stack
- HTML, CSS, JS
- Responsive Design

## ⭐ GitHub Stats
- Stars: 12  |  Forks: 3  |  Watchers: 7
```

---

## 🤝 Contributing

Pull requests are welcome! If you'd like to:

- Add a CLI interface
- Improve the tech stack detection
- Enable GitHub Pages previews
- Add multi-template support

Feel free to open a PR or file an issue ✨

---

## 🛡️ License

This project is licensed under the [MIT License](LICENSE).

---

## ❤️ Credits

Built with care by [valerie-ekeigwe](https://github.com/valerie-ekeigwe)

---

## 💡 Tip

Use this tool after cloning a new project or updating an old one — make every repo portfolio-ready with a single command!

---

> Have feedback? Create an issue or drop a star ⭐
