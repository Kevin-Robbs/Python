from flask_app import app
from flask_app.Models import *
from flask import render_template, redirect, request, session, flash

from flask_app.Models.dojos import Dojo
from flask_app.Models.ninjas import Ninja

###############################################################
#                           Renderings                        #
###############################################################

@app.route('/')
def indexRoute():
    dojos = Dojo.retrieveDojos()
    return render_template('index.html', dojos = dojos)

@app.route('/dojo/<dojo>')
def retrieveDojo(dojo):

    data = {
        'id': int(dojo)
    }

    dojo = Dojo.retrieveDojoByID(data)

    return render_template('dojo.html', dojo = dojo, ninjas = Ninja.retrieveNinjasByDojoID(data))

@app.route('/addNinja')
def userRoute():
    dojos = Dojo.retrieveDojos()
    return render_template('addNinja.html', dojos = dojos)


###############################################################
#                           Redirects                         #
###############################################################
@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    data = {
        'd_name': request.form['d_name']
    }

    Dojo.createDojo(data)

    return redirect('/')

@app.route('/create_ninja', methods=['POST'])
def create_ninja():
     data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_select']
     }

     Ninja.createNinja(data)

     return redirect("/dojo/" + data['dojo_id'])