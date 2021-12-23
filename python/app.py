from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World v1.1+mergebranch!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
