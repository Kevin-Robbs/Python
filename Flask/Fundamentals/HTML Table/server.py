from flask import *
app = Flask(__name__)

users = [
    {'f_name': 'Michael', 'l_name': 'Choi'},
    {'f_name': 'John', 'l_name': 'Supsupin'},
    {'f_name': 'Mark', 'l_name': 'Guillen'},
    {'f_name': 'Kevin', 'l_name': 'Robbs'}
]

@app.route('/')
def indexRoute():
    return render_template('index.html', users=users)

if __name__=='__main__':
    app.run(debug=True)