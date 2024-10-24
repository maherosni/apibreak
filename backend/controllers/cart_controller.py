from flask import request, jsonify
from flask_restx import Api, Resource, Namespace, fields
from models.cart_model import Cart

# Crear el Namespace para Swagger
cart_ns = Namespace('carrito', description='Operaciones relacionadas con el carrito de compras')

# Modelo para agregar productos al carrito en Swagger
cart_model = cart_ns.model('AddToCart', {
    'user_id': fields.Integer(required=True, description='ID del usuario'),
    'product_id': fields.Integer(required=True, description='ID del producto'),
    'quantity': fields.Integer(required=True, description='Cantidad del producto')
})

# Rutas de la API usando Flask-RESTPlus
@cart_ns.route('/')
class CartOperations(Resource):
    @cart_ns.expect(cart_model)
    @cart_ns.doc('add_to_cart')
    def post(self):
        """Añadir un producto al carrito"""
        data = request.get_json()
        Cart.add_to_cart(data)
        return jsonify({'message': 'Producto añadido al carrito con éxito'}), 201


@cart_ns.route('/<int:iduser>')
class UserCart(Resource):
    @cart_ns.doc('get_user_cart')
    def get(self, iduser):
        """Obtener el carrito de un usuario"""
        cart = Cart.get_user_cart(iduser)
        return jsonify(cart)