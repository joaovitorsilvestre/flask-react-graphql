import random, string

from flask import Response, request, jsonify

from backend import app, redis_store

@app.route('/signin', methods=['POST'])
def signin():
    from backend.User.models import User
    json_dict = request.get_json()

    name = json_dict['name']
    password = json_dict['password']

    user = User.objects(name=name, password=password).first()

    if user:
        secret = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(100))
        redis_store.set(secret, user.id)
        return jsonify({'success': 'Login realizado com sucesso', 'secret': secret}), 200
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


@app.route('/logout/<secret>', methods=['GET'])
def logout(secret):
    if secret:
        del redis_store['secret']
        return jsonify({'success': 'Logout com sucesso'}), 200
    else:
        return jsonify({'error': 'Você não está logado'}), 403
