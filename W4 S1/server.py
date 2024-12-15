from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Hello there!")



# @app.route("/home")
# def home():
#     return "Welcome to the homepage"

# @app.route("/welcome/<name>")
# def welcome(name):
#     return "Welcome {name}here"

# if __name__ == "__main__":
#     app.run(debug=True)




