from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key="YOUR_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=user_input
    )

    return jsonify({"reply": response.output_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
