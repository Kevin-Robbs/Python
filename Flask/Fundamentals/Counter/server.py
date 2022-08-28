from flask import Flask, render_template, request, redirect, session
import secrets
app = Flask(__name__)

app.secret_key = secrets.token_hex()

@app.route('/')
def counterIndex():
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] += 1
    return render_template('index.html')

@app.route('/destroy')
def destroySession():
    session.clear()
    return redirect('/')
    
if __name__=='__main__':
    app.run(debug=True)