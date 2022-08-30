from pydoc import render_doc
from flask import *
app = Flask(__name__)

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
    return render_template('result.html', information = data)

if __name__=='__main__':
    app.run(debug=True)