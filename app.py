from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/")
def home():
    return "Glory AI is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are Glory AI, a helpful assistant."},
            {"role": "user", "content": user_message},
        ]
    )

    reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
