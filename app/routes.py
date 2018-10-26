from app import app
from app.controllers import Controllers
from flask import request, session
app.secret_key = 'rubber baby buggy bumpers'
controllers = Controllers()


@app.route('/')
def index():
    session['id'] = 1
    return controllers.index()


# ----------------- #
# User API endpoint #
# ----------------- #
@app.route('/api/v1.0/users', methods=['GET'])
def get_all():
    return controllers.get_all()


@app.route('/api/v1.0/users/<int:id>', methods=['GET'])
def get_one(id):
    return controllers.get_one(int(id))


@app.route('/api/v1.0/users/create', methods=['POST'])
def insert():
    form = request.form
    return controllers.create(form)


@app.route('/api/v1.0/users/edit/<id>', methods=['PUT'])
def update(id):
    form = request.form
    print(form)
    return controllers.update(int(id))


@app.route('/api/v1.0/users/delete/<id>', methods=['DELETE'])
def delete(id):
    return controllers.delete(int(id))


@app.errorhandler(404)
def not_found(error):
    return controllers.not_found(error)
