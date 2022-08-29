from flask import *
from user import User
app = Flask(__name__)

@app.route('/')
def indexRoute():
    users = User.retrieveUsers()

    return render_template('all_users.html', siteUsers = users)

@app.route('/add_user')
def addUserIndex():
   return render_template('add_user.html')

@app.route('/create_user', methods=["POST"])
def addUser():
    data = {
        "fname": request.form["fname"],
        "email" : request.form["email"]
    }

    User.addUser(data)

    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)