from flask import Flask, render_template, redirect, request
from user import User

app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

@app.route('/')
def indexRoute():
    users = User.retrieveUsers()
    return render_template('index.html', all_users = users)

@app.route('/new_user')
def newUserRoute():
    return render_template('new_user.html')

@app.route('/user/<userid>')
def showUserInfo(userid):
    userid = int(userid)
    
    data = {
        "column_name": 'id',
        "value": userid
    }

    single_user = User.retrieveUserByID(data)

    return render_template('user_page.html', user = single_user)

@app.route('/edit_user/<id>')
def editUser(id):
    data = {
        'value': id
    }

    user = User.retrieveUserByID(data)
    first_name = user[0]['full_name'].split(' ')[0]
    last_name = user[0]['full_name'].split(' ')[1]
    user[0]['first_name'] = first_name
    user[0]['last_name'] = last_name

    return render_template('edit_user.html', user = user)

@app.route('/create_user', methods=["POST"])
def create_user():
    fullname = request.form["f_name"] + ' ' + request.form["l_name"]
    data = {
        "full_name": fullname,
        "email": request.form["email"]
    }
    User.addUser(data)

    return redirect('/')

@app.route('/edit_user', methods=['POST'])
def edit_user():
    fullname = request.form["f_name"] + ' ' + request.form["l_name"]

    data = {
        'id': request.form['user_id'],
        'full_name': fullname,
        'email': request.form['email']
    }

    User.editUser(data)

    id = request.form['user_id']

    return redirect('/user/' + str(id))

@app.route('/delete/<userid>')
def del_user(userid):
    data = {
        'id': userid
    }

    User.deleteUser(data)

    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)