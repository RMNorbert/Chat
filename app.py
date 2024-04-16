from flask import Flask, request, jsonify
from chatbot.responseProvider.responseProvider import get_response
import py_eureka_client.eureka_client as eureka_client
import os

chatbot_server_port = 5000
eureka_user = os.getenv("EUREKA_USER")
eureka_password = os.getenv("EUREKA_PASSWORD")
eureka_host = os.getenv("EUREKA_HOST")
client_host = os.getenv("HOST")


eureka_client.init(eureka_server=f"http://{eureka_user}:{eureka_password}@{eureka_host}:8761/eureka",
                   app_name="chatbot-service",
                   instance_host=f"{client_host}",
                   instance_id="chatbot-service",
                   instance_port=chatbot_server_port)

app = Flask(__name__)


@app.post("/predict")
def predict():
    request_body = request.get_json()
    accept_language = request.accept_languages
    cat_personality = request_body['cat']
    text = request_body['message']
    if text is not None or '':
        response = get_response(text, cat_personality)
        message = {"answer": response}
        return jsonify(message)
    else:
        return jsonify({"error": "Invalid request format"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=chatbot_server_port)
    