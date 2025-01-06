from flask import Flask, request, render_template, session, redirect

app = Flask(__name__)
app.secret_key = '123'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_form():
    session['name'] = request.form.get('name', 'No Name Provided')
    session['location'] = request.form.get('location', 'No Location Provided')
    session['language'] = request.form.get('language', 'No Language Provided')
    session['comments'] = request.form.get('comments', 'No Comments Provided')
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html', session=session)

if __name__ == "__main__":
    app.run(debug=True)
