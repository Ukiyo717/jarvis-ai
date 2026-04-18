from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "OK"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(silent=True) or {}
        message = data.get("message", "empty")

        return jsonify({
            "reply": f"You said: {message}"
        })

    except Exception as e:
        return jsonify({
            "reply": f"Server error: {str(e)}"
        }), 200

if __name__ == "__main__":
    app.run()