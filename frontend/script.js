async function analyzeRepo() {
    const repoUrl = document.getElementById("repoUrl").value.trim();
    const resultDiv = document.getElementById("result");

    // Clear previous result
    resultDiv.innerHTML = "";

    // Validation
    if (!repoUrl) {
        alert("Please enter a GitHub repository URL");
        return;
    }

    // Show loading state
    resultDiv.innerHTML = `
        <p style="font-size:16px;">⏳ Analyzing repository, please wait...</p>
    `;

    try {
        // Call backend API
        const response = await fetch("http://127.0.0.1:5000/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                repo_url: repoUrl
            })
        });

        const data = await response.json();

        // Error from backend
        if (data.error) {
            resultDiv.innerHTML = `
                <p style="color:red; font-weight:bold;">
                    ❌ ${data.error}
                </p>
            `;
            return;
        }

        const analysis = data.ai_analysis;

        // Render result UI
        resultDiv.innerHTML = `
            <div style="
                max-width: 650px;
                margin-top: 20px;
                padding: 20px;
                border-radius: 12px;
                background: #ffffff;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            ">
                <h2>📊 Score: ${analysis.score}/100</h2>
                <h3>🏅 Level: ${analysis.level}</h3>

                <p style="margin-top:10px;">
                    <strong>📝 Summary</strong><br>
                    ${analysis.summary}
                </p>

                <h4 style="margin-top:15px;">🚀 Improvement Roadmap</h4>
                <ul>
                    ${analysis.roadmap.map(item => `<li>${item}</li>`).join("")}
                </ul>
            </div>
        `;

    } catch (error) {
        console.error("Frontend error:", error);
        resultDiv.innerHTML = `
            <p style="color:red; font-weight:bold;">
                ❌ Error connecting to backend. Make sure the server is running.
            </p>
        `;
    }
}
