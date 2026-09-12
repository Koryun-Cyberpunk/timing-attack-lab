from flask import Flask, render_template, request, jsonify
import time
import os

app = Flask(__name__)

# Deliberately vulnerable lab secret.
# This is for the timing-attack demonstration only.
SECRET = os.environ.get("LAB_SECRET", "A11b12c13d14e15$")

# Artificial delay per correctly matched character.
DELAY = 0.030  # 30 ms

def vulnerable_check(candidate: str) -> bool:
    """Intentionally leaks timing information."""
    if len(candidate) != len(SECRET):
        # Keep length handling simple for the lab.
        return False

    for supplied, expected in zip(candidate, SECRET):
        if supplied != expected:
            return False
        time.sleep(DELAY)

    return True

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/check")
def check():
    data = request.get_json(silent=True) or {}
    candidate = str(data.get("password", ""))

    started = time.perf_counter()
    ok = vulnerable_check(candidate)
    elapsed_ms = (time.perf_counter() - started) * 1000

    return jsonify({
        "ok": ok,
        "elapsed_ms": round(elapsed_ms, 3),
        "length": len(candidate)
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
