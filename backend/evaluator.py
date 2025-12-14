def evaluate_repo(repo):
    # Safely extract values (None → 0)
    stars = repo.get("stars") or 0
    commits = repo.get("commit_count") or 0
    files = repo.get("file_count") or 0
    has_readme = repo.get("has_readme", False)
    has_tests = repo.get("has_tests", False)
    has_ci = repo.get("has_ci", False)

    score = 0
    roadmap = []

    # ⭐ Stars
    if stars > 100:
        score += 20
    elif stars > 20:
        score += 10

    # 🧾 Commits
    if commits > 20:
        score += 20
    elif commits > 5:
        score += 10
    else:
        roadmap.append("Improve commit frequency and consistency")

    # 📂 Files
    if files > 20:
        score += 20
    elif files > 5:
        score += 10

    # 📘 README
    if has_readme:
        score += 20
    else:
        roadmap.append("Add a detailed README.md")

    # 🧪 Tests
    if has_tests:
        score += 10
    else:
        roadmap.append("Add unit tests")

    # ⚙️ CI/CD
    if has_ci:
        score += 10
    else:
        roadmap.append("Add CI/CD using GitHub Actions")

    # 🎖️ Level
    if score >= 80:
        level = "Advanced (Gold)"
    elif score >= 50:
        level = "Intermediate (Silver)"
    else:
        level = "Beginner (Bronze)"

    summary = f"This repository demonstrates a {level.lower()} skill level with a score of {score}/100."

    return {
        "score": score,
        "level": level,
        "summary": summary,
        "roadmap": roadmap
    }
