from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "POC-7: GitHub + Jenkins + Docker + Ansible Deployment Successful!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
