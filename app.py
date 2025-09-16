from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flasgger import Swagger
from flask_login import UserMixin


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)
swagger = Swagger(app)

# Modelagem
# User (id, username, password)
class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), nullable=False, unique=True)  
  password = db.Column(db.String(80), nullable=True)

# Definindo a classe Product com os atributos
# Product (id, name, price, description)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

# Adicionando a rota e os metodos
@app.route('/login', methods=["POST"])
def login():
  data = request.json
  
  user = User.query.filter_by(username=data.get("username")).first()
  print(user)
  return jsonify({"message": "Logged in successfully"})
  

@app.route('/api/products/add', methods=["POST"])
def add_product():
    """
    Adicionar um novo produto
    ---
    tags:
      - Produtos
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - name
            - price
          properties:
            name:
              type: string
              example: "Teclado Gamer"
            price:
              type: number
              example: 199.90
            description:
              type: string
              example: "Teclado mecânico RGB"
    responses:
      200:
        description: Produto adicionado com sucesso
    """
    data = request.json
    if "name" in data and "price" in data:    
        product = Product(name=data["name"], price=data["price"], description=data.get("description", ""))
        db.session.add(product)
        db.session.commit()
        return jsonify({"message": "Product added successfully"})
    return jsonify({"message": "Invalid product data"}), 400


@app.route('/api/products/delete/<product_id>', methods=["DELETE"])
def delete_product(product_id):
    """
    Deletar um produto pelo ID
    ---
    tags:
      - Produtos
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
        description: ID do produto
    responses:
      200:
        description: Produto deletado com sucesso
    """
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully"})
    return jsonify({"message": "Product not found"}), 404


@app.route('/api/products/<product_id>', methods=["GET"])
def get_product_details(product_id):
    """
    Buscar detalhes de um produto
    ---
    tags:
      - Produtos
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
        description: ID do produto
    responses:
      200:
        description: Produto encontrado
    """
    product = Product.query.get(product_id)
    if product:
        return jsonify({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description
        })
    return jsonify({"message": "Product not found"}), 404


@app.route('/api/products/update/<product_id>', methods=["PUT"])
def update_product(product_id):
    """
    Atualizar um produto
    ---
    tags:
      - Produtos
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            name:
              type: string
            price:
              type: number
            description:
              type: string
    responses:
      200:
        description: Produto atualizado
    """
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"message": "Product not found"})
    data = request.json
    if "name" in data:
        product.name = data['name']
    if "price" in data:
        product.price = data['price']
    if "description" in data:
        product.description = data['description']
    db.session.commit()
    return jsonify({"message": "Product updated successfully"})


@app.route('/api/products', methods=["GET"])
def get_all_products():
    """
    Listar todos os produtos
    ---
    tags:
      - Produtos
    responses:
      200:
        description: Lista de produtos
    """
    products = Product.query.all()
    product_list = []
    for product in products:
        product_data = {
            "id": product.id,
            "name": product.name,
            "price": product.price
        }
        product_list.append(product_data)
    return jsonify(product_list)


@app.route("/")
def hello_world():
    return 'Hello World'


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
