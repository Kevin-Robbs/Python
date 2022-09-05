from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['d_name']
        self.created = data['created_at']
        self.updated = data['updated_at']

    @classmethod
    def retrieveDojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []

        for dojo in results:
            dojos.append(cls(dojo))

        return dojos

    @classmethod
    def createDojo(cls, data):
        query = "INSERT INTO dojos (d_name, created_at, updated_at) VALUES (%(d_name)s, NOW(), NOW())"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def retrieveDojoByID(cls, data):
        query = "SELECT * FROM dojos WHERE id=%(id)s"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)


#you will initialize variables to reflect column names in Database table