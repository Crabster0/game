from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Ahoj! Flask aplikace úspěšně běží na Renderu!"

if __name__ == "__main__":
    app.run(debug=True)
