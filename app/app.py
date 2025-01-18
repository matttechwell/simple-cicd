from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Docker CI/CD!"

@app.route('/api/data')
def get_data():
    data = {
        "name": "GitHub Copilot",
        "role": "AI Programming Assistant"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)