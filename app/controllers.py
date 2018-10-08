from flask import render_template
from app.models import Users, UserManager
user_manager = UserManager()


class Controllers:
    def index(self):
        return render_template('index.html')

    # ----------------------------- #
    # user API endpoint controllers #
    # ----------------------------- #
    def get_all(self):
        response = user_manager.get_all()
        return "Returning data: {}".format(response)

    def get_one(self, id):
        response = user_manager.get_one(id)
        return "Returning data: {}".format(response)

    def create(self, form):
        new_user = Users(form)
        valid = user_manager.validate(new_user)
        if valid:
            response = "creating new user"
        else:
            response = "something went wrong"
        return "Returning data: {}".format(response)

    def update(self, id):
        return "Updating data: {}".format(id)

    def delete(self, id):
        return "Deleting data: {}".format(id)
