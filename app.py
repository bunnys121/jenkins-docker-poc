from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "POC-2: Git to Jenkins to Docker deployment successful!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
