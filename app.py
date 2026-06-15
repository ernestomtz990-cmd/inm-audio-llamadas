from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("EVENTO TELNYX:", data)
    return jsonify({"ok": True}), 200

@app.route("/", methods=["GET"])
def home():
    return "Telnyx webhook activo", 200

if __name__ == "__main__":
    app.run(port=5000)