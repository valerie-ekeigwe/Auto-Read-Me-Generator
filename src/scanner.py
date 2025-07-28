import os

def scan_project(path):
    files = os.listdir(path)
    tech = []
    
    if "requirements.txt" in files:
        tech.append("Python")
    if "package.json" in files:
        tech.append("JavaScript / Node.js")
    if any(f.endswith(".ipynb") for f in files):
        tech.append("Jupyter Notebook")

    return {
        "has_tests": "tests" in files or "test" in files,
        "tech_stack": tech
    }
