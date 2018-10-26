from flask import request
from flask import render_template
from flask import jsonify
from flask import make_response
from flask import abort
from app.models import Users, UserAPI
user_api = UserAPI()


class Controllers:
    def index(self):
        return render_template('index.html')

    def process(self, form):
        new_user = Users(form)
        response = user_api.validate(new_user)
        return "Returning data: {}".format(response)

    # ----------------------------- #
    # user API endpoint controllers #
    # ----------------------------- #
    def get_all(self):
        response = user_api.get_all()
        return jsonify({'users': response})

    def get_one(self, id):
        response = user_api.get_one(id)
        return jsonify({'user': response})

    def create(self, user):
        if not request.json or 'title' not in request.json:
            abort(400)
        return jsonify

    def update(self, id):
        return "Updating data: {}".format(id)

    def delete(self, id):
        return "Deleting data: {}".format(id)

    def not_found(self, error):
        return make_response(jsonify({'error': 'Not found'}), 404)
