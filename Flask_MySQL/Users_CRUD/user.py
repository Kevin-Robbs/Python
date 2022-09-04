from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.full_name = data['full_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.update_at = data['updated_at']
    
    @classmethod
    def retrieveUsers(cls): #complete
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_cr').query_db(query)
        users = []

        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def addUser(cls, data):
        query = "INSERT INTO users (full_name, email, created_at) VALUES (%(full_name)s, %(email)s, NOW())"
        return connectToMySQL('users_cr').query_db(query, data)
        
    @classmethod
    def retrieveUserByID(cls, data):

        query = "SELECT * FROM users WHERE id=%(value)s"
        return connectToMySQL('users_cr').query_db(query, data)

    @classmethod
    def editUser(cls, data):
        query = "UPDATE users SET full_name=%(full_name)s, email=%(email)s, updated_at=NOW() WHERE id=%(id)s"
        return connectToMySQL('users_cr').query_db(query, data)

    @classmethod
    def deleteUser(cls, data):
        query = "DELETE FROM users WHERE id=%(id)s"
        return connectToMySQL('users_cr').query_db(query, data)