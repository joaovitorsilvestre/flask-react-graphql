from flask import render_template, request, jsonify

from backend import app


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    from backend.User.models import User

    if request.method == "POST":
        json_dict = request.get_json()

        name = json_dict['name']
        cpf = json_dict['cpf']

        user = User(name=name, cpf=cpf).save()

        return user.name + ' foi criado com sucesso'