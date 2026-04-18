from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Jarvis is running"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")

    if not message:
        return jsonify({"reply": "No message received"})

    # simple placeholder reply for now (we add AI next)
    return jsonify({"reply": "You said: " + message})

if __name__ == "__main__":
    app.run()