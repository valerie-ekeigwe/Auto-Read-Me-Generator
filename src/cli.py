import os
import argparse
from pathlib import Path
from dotenv import load_dotenv
from src.github_api import get_repo_stats
from src.scanner import scan_project
from src.readme_generator import render_readme


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate a README from local scan and optional GitHub metadata."
    )
    parser.add_argument("--repo", required=True, help="Path to the local repository")
    parser.add_argument("--github_user", help="GitHub username")
    parser.add_argument("--repo_name", help="GitHub repository name")
    parser.add_argument("--template", default="minimal", help="Template name (e.g. minimal, webapp)")
    parser.add_argument("--out", default="README.md", help="Output filename or absolute path")
    parser.add_argument("--dry-run", action="store_true", help="Print to stdout instead of writing a file")
    return parser


def main() -> None:
    env_path = Path(".env")
    if env_path.exists():
        load_dotenv()
    else:
        print("No .env file found. GitHub stats will be skipped.")

    args = build_parser().parse_args()

    repo_path = Path(args.repo).resolve()
    if not repo_path.is_dir():
        print(f"Error: repository path not found: {repo_path}")
        return

    github_data = {}
    token = os.getenv("GITHUB_TOKEN")
    if token and args.github_user and args.repo_name:
        try:
            github_data = get_repo_stats(args.github_user, args.repo_name)
        except Exception as exc:
            print(f"GitHub request failed: {exc}")

    local_data = scan_project(repo_path)
    context = {
        "title": args.repo_name or repo_path.name,
        "description": (github_data.get("description") or "No description available.").strip(),
        "tech_stack": ", ".join(local_data.get("tech_stack", [])) or "N/A",
        "has_tests": bool(local_data.get("has_tests", False)),
        "stars": int(github_data.get("stars", 0)),
        "forks": int(github_data.get("forks", 0)),
        "watchers": int(github_data.get("watchers", 0)),
        "language": github_data.get("language", local_data.get("language", "N/A")),
    }

    output = render_readme(context, template_name=args.template)

    out_path = Path(args.out)
    if not out_path.is_absolute():
        out_path = repo_path / out_path

    if args.dry_run:
        print(output)
        return

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(output, encoding="utf-8")
    print(f"README generated at: {out_path}")


if __name__ == "__main__":
    main()
