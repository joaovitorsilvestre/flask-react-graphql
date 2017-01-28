from flask import render_template, request, jsonify
from flask_login import LoginManager, login_user, current_user

from backend import app


login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    from backend.User.models import User
    return User.objects.get(int(id))

@app.route('/signin', methods=['POST'])
def signin():
    from backend.User.models import User
    json_dict = request.get_json()

    name = json_dict['name']
    password = json_dict['password']

    user = User.objects(name=name, password=password).first()

    if user:
        login_user(user)
        return jsonify({'success': 'Login realizado com sucesso'}), 200
    else:
        return jsonify({'error': 'Nome ou senha invalidos'}), 403

@app.route('/register', methods=['POST'])
def register():
    from backend.User.models import User
    json_dict = request.get_json()

    name = json_dict['name']
    password = json_dict['password']

    user = User(name=name, password=password, active=True).save()

    if user:
        return jsonify({'success': 'Conta criada com sucesso'}), 200
    else:
        return jsonify({'error': 'Algo errado não está certo'}), 500