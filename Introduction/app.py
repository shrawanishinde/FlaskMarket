from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello World!</h1>"

@app.route("/about")
def about():
    return "this is about"

@app.route("/about/<username>")
def user(username):
    return f"hello this is {username}"

if __name__ == "__main__":
    app.run(debug=True)