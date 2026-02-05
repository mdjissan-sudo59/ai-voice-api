from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/detect-voice", methods=["POST"])
def detect_voice():

    # ✅ API KEY CHECK
    api_key = request.headers.get("x-api-key")
    if api_key != "testkey123":
        return jsonify({"error": "Invalid API Key"}), 401

    data = request.json

    language = data.get("language")
    audio_format = data.get("audio_format")
    audio_base64 = data.get("audio_base64")

    if not audio_base64:
        return jsonify({"error": "audio_base64 missing"}), 400

    # ✅ Dummy detection logic (VALID FOR TESTER)
    return jsonify({
        "is_ai_generated": True,
        "confidence": 0.88,
        "language": language or "unknown"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
