from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:

    def __init__(self, data):
        self.dojo_id = data['id']
        self.name = data['name']
        self.email = data['email']
        self.age = data['age']
        self.created = data['created_at']
        self.updated = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def createNinja(cls, data):
        query = "INSERT INTO ninjas (name, email, age, created_at, updated_at, dojo_id) VALUES (%(name)s, %(email)s, %(age)s, NOW(), NOW(), %(dojo_id)s)"
        print(query)
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def retrieveNinjasByDojoID(cls , data):
        query = """select ninjas.id, name, email, age, ninjas.created_at 
                   from ninjas 
                   left join dojos 
                   on ninjas.dojo_id = dojos.id
                   where dojos.id = %(id)s"""
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)