from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

# The Flask framework controls when the `home` function is called.
if __name__ == "__main__":
    app.run()
