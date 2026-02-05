from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/detect-voice", methods=["POST"])
def detect_voice():
    auth = request.headers.get("Authorization")

    if auth != "Bearer testkey123":
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    audio_url = data.get("audio_url")

    if not audio_url:
        return jsonify({"error": "audio_url missing"}), 400

    return jsonify({
        "is_ai_generated": True,
        "confidence": 0.85,
        "language": "unknown"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
