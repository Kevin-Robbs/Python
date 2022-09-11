from flask_app.controllers import controllers

if __name__=='__main__':
    controllers.app.run(debug=True)