from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

AURORA_API_KEY = os.environ.get("AURORA_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    feedback = ""
    if request.method == "POST":
        insha = request.form.get("insha")  # GET insha from the web form

        # Call Aurora Alpha API
        headers = {
            "Authorization": f"Bearer {AURORA_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "prompt": f"Tafadhali chambua insha hii na toa maoni ya makosa, urefu, sentensi, na mapendekezo ya kuboresha:\n\n{insha}",
            "max_tokens": 300
        }

        try:
            response = requests.post(
                "https://api.aurora-alpha.com/v1/ai",  # example endpoint
                headers=headers,
                json=data
            )
            result = response.json()
            feedback = result.get("feedback") or result.get("text") or "Hakuna matokeo yaliyopatikana."
        except Exception as e:
            feedback = f"Hitilafu ya AI: {str(e)}"

    return render_template("index.html", feedback=feedback)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


