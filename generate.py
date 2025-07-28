import os
import argparse
from dotenv import load_dotenv
from src.github_api import get_repo_stats
from src.scanner import scan_project
from src.readme_generator import render_readme

# Load .env file to access GitHub token
load_dotenv()

def parse_args():
    parser = argparse.ArgumentParser(description="Auto-generate a professional README.md file for your project.")
    parser.add_argument("--repo", required=True, help="Local path to your cloned GitHub repo")
    parser.add_argument("--github_user", required=True, help="Your GitHub username")
    parser.add_argument("--repo_name", required=True, help="Name of your GitHub repository")
    return parser.parse_args()

def main():
    args = parse_args()

    # Validate GitHub token
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("❌ Error: GITHUB_TOKEN not found. Make sure you have a .env file with GITHUB_TOKEN=your_token")
        return

    try:
        # Fetch GitHub repo data
        github_data = get_repo_stats(args.github_user, args.repo_name)

        # Scan local project for tech stack info
        local_data = scan_project(args.repo)

        # Prepare content for README generation
        context = {
            "title": args.repo_name,
            "description": github_data.get("description", "No description available."),
            "tech_stack": ", ".join(local_data["tech_stack"]),
            "has_tests": local_data["has_tests"],
            "stars": github_data["stars"],
            "forks": github_data["forks"],
            "watchers": github_data["watchers"],
            "language": github_data["language"]
        }

        # Generate and write README.md
        output = render_readme(context)
        readme_path = os.path.join(args.repo, "README.md")
        with open(readme_path, "w") as f:
            f.write(output)

        print(f"✅ README.md successfully generated at: {readme_path}")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
