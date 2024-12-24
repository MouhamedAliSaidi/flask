from flask import Flask , render_template , session , redirect , request
app=Flask(__name__)
app.secret_key='xyz'

@app.route('/')
def index():
    if 'counter' in session:
        session['counter']+=1
    else:
        session['counter']=1
    return render_template('index.html', counter=session['counter'])

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')


@app.route('/add_one' , methods=['POST'])
def add_one():
    if 'counter' in session:
        session['counter']+= int(request.form.get('increment_by',1))
    else:
        session['counter']= int(request.form.get('increment_by',1))
    return redirect('/')    

@app.route('/reset')
def reset():
    session.pop('counter',None)
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)