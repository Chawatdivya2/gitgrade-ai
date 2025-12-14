from github_analyzer import analyze_repo
from evaluator import evaluate_repo

repo = "https://github.com/torvalds/linux"

repo_data = analyze_repo(repo)
evaluation = evaluate_repo(repo_data)

print("\n--- REPO DATA ---")
print(repo_data)

print("\n--- AI EVALUATION ---")
print(evaluation)
