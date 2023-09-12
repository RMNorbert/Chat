from flask import Flask, request, jsonify
from chatbot.chat import get_response

app = Flask(__name__)


@app.post("/predict")
def predict():
    text = request.get_json()
    if text is not None or '':
        response = get_response(text)
        message = {"answer": response}
        return jsonify(message)
    else:
        return jsonify({"error": "Invalid request format"})


if __name__ == "__main__":
    app.run(debug=True)
