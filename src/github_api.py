from github import Github
import os
from dotenv import load_dotenv

load_dotenv()

def get_repo_stats(user, repo_name):
    token = os.getenv("GITHUB_TOKEN")
    
    if not token:
        raise ValueError("GITHUB_TOKEN not found. Make sure it is in your .env file and loaded.")
    
    g = Github(token)
    repo = g.get_user(user).get_repo(repo_name)
    
    return {
        "stars": repo.stargazers_count,
        "forks": repo.forks_count,
        "watchers": repo.watchers_count,
        "language": repo.language,
        "description": repo.description or "No description provided."
    }
