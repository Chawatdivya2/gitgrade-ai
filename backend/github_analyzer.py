import requests

def analyze_repo(repo_url):
    parts = repo_url.rstrip("/").split("/")
    owner, repo = parts[-2], parts[-1]
    base_url = f"https://api.github.com/repos/{owner}/{repo}"

    data = {}

    repo_info = requests.get(base_url).json()
    data["name"] = repo_info.get("name")
    data["stars"] = repo_info.get("stargazers_count")

    # Languages
    languages = requests.get(f"{base_url}/languages").json()
    data["languages"] = list(languages.keys())

    # Commits
    commits = requests.get(f"{base_url}/commits").json()
    data["commit_count"] = len(commits) if isinstance(commits, list) else 0

    # Contents
    contents = requests.get(f"{base_url}/contents").json()
    data["file_count"] = len(contents) if isinstance(contents, list) else 0

    # README
    readme_status = requests.get(f"{base_url}/readme").status_code
    data["has_readme"] = True if readme_status == 200 else False

    # Test & CI checks (basic)
    data["has_tests"] = any(
        "test" in item["name"].lower()
        for item in contents
        if isinstance(contents, list)
    )

    data["has_ci"] = any(
        item["name"] == ".github"
        for item in contents
        if isinstance(contents, list)
    )

    return data

