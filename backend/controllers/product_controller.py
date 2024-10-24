from flask import request, jsonify
from flask_restx import Api, Resource, Namespace, fields
from models.product_model import Product

# Crear el Namespace para la documentación de Swagger
product_ns = Namespace('productos', description='Operaciones relacionadas con productos')

# Modelo para la creación y actualización de productos en Swagger
product_model = product_ns.model('Product', {
    'nombre': fields.String(required=True, description='El nombre del producto'),
    'descripcion': fields.String(required=True, description='La descripción del producto'),
    'precio': fields.Float(required=True, description='El precio del producto'),
    'idcategoria': fields.Integer(required=True, description='El ID de la categoría')
})

# Rutas de la API usando Flask-RESTPlus
@product_ns.route('/')
class ProductList(Resource):
    @product_ns.doc('list_products')
    def get(self):
        """Obtener todos los productos"""
        products = Product.get_all()
        return jsonify(products)

    @product_ns.expect(product_model)
    @product_ns.doc('create_product')
    def post(self):
        """Crear un nuevo producto"""
        data = request.get_json()
        Product.create(data)
        return jsonify({'message': 'Producto creado con éxito'}), 201


@product_ns.route('/<int:idprod>')
@product_ns.param('idprod', 'El identificador del producto')
class ProductResource(Resource):
    @product_ns.doc('get_product')
    def get(self, idprod):
        """Obtener un producto por su ID"""
        product = Product.get_by_id(idprod)
        if product:
            return jsonify(product)
        return {'message': 'Producto no encontrado'}, 404

    @product_ns.expect(product_model)
    @product_ns.doc('update_product')
    def put(self, idprod):
        """Actualizar un producto existente"""
        data = request.get_json()
        Product.update(idprod, data)
        return jsonify({'message': 'Producto actualizado con éxito'})

    @product_ns.doc('delete_product')
    def delete(self, idprod):
        """Eliminar un producto por su ID"""
        Product.delete(idprod)
        return jsonify({'message': 'Producto eliminado con éxito'})


@product_ns.route('/categoria')
class ProductByCategory(Resource):
    @product_ns.doc('get_products_by_category')
    def get(self):
        """Obtener productos agrupados por categoría"""
        products_grouped = Product.get_all_grouped_by_category()
        return jsonify(products_grouped)
