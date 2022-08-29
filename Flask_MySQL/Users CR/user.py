from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.full_name = data['full_name']
        self.email = data['email']
        self.created_at = data['created_at']
    
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
        query = "INSERT INTO users (full_name, email, created_at) VALUES ( %(fname)s , %(email)s , NOW())"
        return connectToMySQL('users_cr').query_db(query, data)
        