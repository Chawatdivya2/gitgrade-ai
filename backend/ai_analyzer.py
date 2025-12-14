import requests

GITHUB_API = "https://api.github.com/repos"


def collect_repo_context(owner, repo):
    repo_url = f"{GITHUB_API}/{owner}/{repo}"
    commits_url = f"{repo_url}/commits"
    languages_url = f"{repo_url}/languages"
    contents_url = f"{repo_url}/contents"

    repo_data = requests.get(repo_url).json()
    commits_data = requests.get(commits_url).json()
    languages_data = requests.get(languages_url).json()
    contents_data = requests.get(contents_url).json()

    has_readme = any(
        file["name"].lower().startswith("readme")
        for file in contents_data
        if file["type"] == "file"
    )

    has_tests = any(
        "test" in file["name"].lower()
        for file in contents_data
        if file["type"] == "file"
    )

    return {
        "stars": repo_data.get("stargazers_count", 0),
        "forks": repo_data.get("forks_count", 0),
        "files": len(contents_data),
        "commits": len(commits_data) if isinstance(commits_data, list) else 0,
        "has_readme": has_readme,
        "has_tests": has_tests,
        "languages": list(languages_data.keys())
    }


def analyze_with_ai(repo):
    score = 0
    roadmap = []

    if repo["has_readme"]:
        score += 20
    else:
        roadmap.append("Add a detailed README file")

    if repo["has_tests"]:
        score += 20
    else:
        roadmap.append("Add unit and integration tests")

    if repo["commits"] > 10:
        score += 20
    else:
        roadmap.append("Increase commit frequency with meaningful messages")

    if repo["files"] > 10:
        score += 20
    else:
        roadmap.append("Improve project structure with more modules")

    if repo["stars"] > 10:
        score += 20
    else:
        roadmap.append("Improve documentation and visibility to gain stars")

    if score >= 85:
        level = "Advanced (Gold)"
    elif score >= 60:
        level = "Intermediate (Silver)"
    else:
        level = "Beginner (Bronze)"

    return {
        "score": score,
        "level": level,
        "summary": (
            f"This repository shows {level.lower()} development practices "
            f"based on structure, activity, and documentation."
        ),
        "roadmap": roadmap
    }
