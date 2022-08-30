from flask import *
import secrets
app = Flask(__name__)

app.secret_key = secrets.token_hex()

@app.route('/')
def indexRoute():
    return render_template('index.html')

@app.route('/display_info', methods=["POST"])
def resultRoute():
    data = {
        'name': request.form['name'],
        'location': request.form['location'],
        'language': request.form['language'],
        'comment': request.form['comment']
    }

    session['data'] = data
    return render_template('result.html')

if __name__=='__main__':
    app.run(debug=True)