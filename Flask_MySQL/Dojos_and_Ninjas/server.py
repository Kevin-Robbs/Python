from flask_app.controllers import routes

if __name__=='__main__':
    routes.app.run(debug=True)