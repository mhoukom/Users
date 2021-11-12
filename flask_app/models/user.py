from flask_app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for row in results:
            users.append(cls(row))

        print(users)
        return users

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        results = connectToMySQL('users_schema').query_db(query, data)

        return results

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('users_schema').query_db(query, data)

        if len(results) == 0:
            return False

        return User(results[0]) 


    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        results = connectToMySQL('users_schema').query_db(query, data)

        return results

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"

        connectToMySQL('users_schema').query_db(query, data)