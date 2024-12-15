from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def say_dojo():
    return'Dojo!'

@app.route('/say/<name>')
def speller(name):
    return 'hi %s' % name

# @app.route('/say/flask')
# def say_flask():
#     return 'Hi Flask!'

# @app.route('/say/michael')
# def say_michael():
#     return  'Hi Michael'

# @app.route('/say/john')
# def say_john():
#     return 'hi john!'

from flask import Flask

app = Flask(__name__)

@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    return word * num

if __name__ == "__main__":
    app.run(debug=True)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

