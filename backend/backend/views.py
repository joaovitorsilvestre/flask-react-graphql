from flask import render_template, request, jsonify

from backend import app


### Refazer usando Mutations do graphql

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     from backend.User.models import User
#
#     if request.method == "POST":
#         json_dict = request.get_json()
#
#         name = json_dict.get('name')
#         password = json_dict.get('password')
#
#         if name and password:
#             user = User(name=name, password=password).save()
#             return jsonify({'success': user.name + ' foi criado com sucesso'}), 200
#         else:
#             return jsonify({'error': 'Campos errados'}), 403
#
#
# @app.route('/signin', methods=['GET', 'POST'])
# def signin():
#     from backend.User.models import User
#
#     if request.method == 'POST':
#         json_dict = request.get_json()
#
#         name = json_dict['name']
#         password = json_dict['password']
#
#         user = User.objects(name=name, password=password).first()
#
#         if user:
#             return jsonify({'success': 'Login realizado com sucesso'}), 200
#         else:
#             return jsonify({'error': 'Nome ou senha invalidos'}), 403
#
# @app.route('/create-product', methods=['GET', 'POST'])
# def create_product():
#     from backend.Product.models import Product
#
#     if request.method == 'POST':
#         json_dict = request.get_json()
#
#         name = json_dict['name']
#         price = json_dict['price']
#         if name and price:
#             product = Product(name=name, price=price).save()
#             return jsonify({'success': product.name + ' foi criado com sucesso'}), 200
#         else:
#             return jsonify({'error': 'Compos errados'}), 403