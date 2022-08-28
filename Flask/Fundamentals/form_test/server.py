from flask import *
app = Flask(__name__)

@app.route('/')
def indexRoute():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form['name'])
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)