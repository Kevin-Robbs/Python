from operator import length_hint
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:

    def __init__(self, data):
        self.f_name = data['f_name']
        self.l_name = data['l_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def retrieveUser(cls, data):
        query = "SELECT id, f_name, l_name, email, password, created_at, updated_at FROM users WHERE email = %(email)s"
        return connectToMySQL('login').query_db(query, data)

    @classmethod
    def createUser(cls, data):
        query = "INSERT INTO users (f_name, l_name, email, password, created_at, updated_at) VALUES (%(f_name)s, %(l_name)s, %(email)s, %(password)s, NOW(), NOW())"

        return connectToMySQL('login').query_db(query, data)

    @staticmethod
    def validateUser(user):
        isValid = True
        print(user)

        if len(user['password']) < 12:
            flash('Password does not meet length requirements')
            isValid = False
        if not email_regex.match(user['email']):
            flash('Improper email format ex.(myemail@mail.com)')
            isValid = False
        
        return isValid
        

#you will initialize variables to reflect column names in Database table