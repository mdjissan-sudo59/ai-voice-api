from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Voice Detection API is running"

@app.route("/detect-voice", methods=["POST"])
def detect_voice():
    return jsonify({
        "is_ai_generated": True,
        "confidence": 0.9,
        "language": "en"
    }), 200
