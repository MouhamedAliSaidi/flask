from flask import Flask,render_template
app = Flask(__name__)


users=  [
    {'first_name': 'Michael','Last_name': 'Choi'},
    {'first_name' : 'John' , 'Last_name' : 'Suspupîn'},
    {'first_name' : 'Mark', 'Last_name' : 'Guillen'},
    {'first_name' : 'KB' , 'Last_name' : 'Tonel'}
]

@app.route('/')
def index():
    return render_template("index.html", users=users)


if __name__=="__main__":
    app.run(debug=True)
