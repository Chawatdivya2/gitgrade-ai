from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_analyzer import collect_repo_context, analyze_with_ai

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    if not data or "repo_url" not in data:
        return jsonify({"error": "Repository URL missing"}), 400

    repo_url = data["repo_url"]

    # Extract owner and repo name
    parts = repo_url.rstrip("/").split("/")
    if len(parts) < 5:
        return jsonify({"error": "Invalid GitHub repository URL"}), 400

    owner = parts[-2]
    repo = parts[-1]

    try:
        # Collect repository content
        repo_context = collect_repo_context(owner, repo)

        # AI analysis
        ai_response = analyze_with_ai(repo_context)

        return jsonify({
            "ai_analysis": ai_response
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
