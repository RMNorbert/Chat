from flask import Flask, request, jsonify
from chatbot.responseProvider.responseProvider import get_response

app = Flask(__name__)


@app.post("/predict")
def predict():
    request_body = request.get_json()
    cat_personality = request_body['cat']
    text = request_body['message']
    if text is not None or '':
        response = get_response(text, cat_personality)
        message = {"answer": response}
        return jsonify(message)
    else:
        return jsonify({"error": "Invalid request format"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    