from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.Models.model import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

#################################################
#                     Routes                    #
#################################################

@app.route('/')
def indexRoute():
    return render_template('index.html')

@app.route('/register')
def registerRoute():
    return render_template('register.html')

@app.route('/dashboard')
def dashboardRoute():
    if 'user_id' in session:
        return render_template('dashboard.html')
    else:
        session.clear()
        return redirect('/')
    


#################################################
#                   Redirects                   #
#################################################

@app.route('/login_user', methods = ['POST', 'GET'])
def login_user():

    data = {
        'email': request.form['email'] 
    }

    user = User.retrieveUser(data)

    if not user:
        flash('Invalid Email')
        return redirect('/')
    elif not bcrypt.check_password_hash(user[0]['password'], request.form['password']):
        flash('Invalid Password')
        return redirect('/')
    else:
        session['user_id'] = user[0]['id']
        return redirect('/dashboard')


@app.route('/register_user', methods = ['POST', 'GET'])
def register_user():
    email = {
        'email': request.form['email']
    }

    user = User.retrieveUser(email)

    if user:
        flash('Email already exists')
        return redirect('/register')
    else:
        data = {
            'email': request.form['email'],
             'password': request.form['password']
        }

        if not User.validateUser(data):
            return redirect('/register')
        else:
            h_pass = bcrypt.generate_password_hash(request.form['password'])

            data = {
                'f_name': request.form['f_name'],
                'l_name': request.form['l_name'],
                'email': request.form['email'],
                'password': h_pass
            }

            User.createUser(data)
            return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')