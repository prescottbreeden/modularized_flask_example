from app import app
from app.controllers import Controllers
from flask import request, session
app.secret_key = 'rubber baby buggy bumpers'
controllers = Controllers()


@app.route('/')
def index():
    return controllers.index()


# ----------------- #
# User API endpoint #
# ----------------- #
@app.route('/users')
def get_all():
    return controllers.get_all()


@app.route('/users/<id>')
def get_one(id):
    return controllers.get_one(int(id))


@app.route('/users/create', methods=['POST'])
def insert():
    form = request.form
    return controllers.create(form)


@app.route('/users/edit/<id>', methods=['POST'])
def update(id):
    form = request.form
    print(form)
    return controllers.update(int(id))


@app.route('/users/delete/<id>')
def delete(id):
    return controllers.delete(int(id))
