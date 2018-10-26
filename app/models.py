from flask import session, flash, abort
from app.database import users


class UserAPI:
    def validate(self, user):
        errors = {}
        if len(user.first_name) < 1:
            flash("First name cannot be blank", 'first_name')
            errors['first_name'] = "blank"
        if len(user.last_name) < 1:
            flash("Last name cannot be blank", 'last_name')
            errors['last_name'] = "blank"
        if len(user.email) < 1:
            flash("Email cannot be blank", 'email')
            errors['email'] = "blank"
        # if '_flashes' in session.keys():
        if errors:
            print(session['_flashes'])
            return "Invalid User"
        return "Creating New User"

    def get_all(self):
        return users

    def get_one(self, id):
        result = [user for user in users if user['id'] == id]
        if len(result) == 0:
            abort(404)
        return result

    def create(self, user):
        db_connection = "connecting to database"
        query = '''
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        '''
        result = "{} {}".format(db_connection, query)
        return result

    def update(self, id, data):
        data = data
        db_connection = "connecting to database"
        query = ("UPDATE users"
                 "SET user.data={} WHERE user_id={}".format(data, id))
        result = "{} {}".format(db_connection, query)
        return result

    def delete(self, id):
        db_connection = "connecting to database"
        query = "DELETE FROM users WHERE user_id={}".format(id)
        result = "{} {}".format(db_connection, query)
        return result


class Users:
    def __init__(self, form):
        self.first_name = form['first_name']
        self.last_name = form['last_name']
        self.email = form['email']
        self.password = form['password']

    def __repr__(self):
        return "User {}, email {}".format(self.first_name, self.email)
