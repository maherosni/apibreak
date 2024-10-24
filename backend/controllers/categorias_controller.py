from flask import request, jsonify
from flask_restx import Api, Resource, Namespace, fields
from models.categorias_model import Categoria

# Crear el Namespace para Swagger
categoria_ns = Namespace('categorias', description='Operaciones relacionadas con categorías')

# Modelo para la creación de categorías en Swagger
categoria_model = categoria_ns.model('Categoria', {
    'nombre': fields.String(required=True, description='El nombre de la categoría')
})

# Rutas de la API usando Flask-RESTPlus
@categoria_ns.route('/')
class CategoriaList(Resource):
    @categoria_ns.doc('get_all_categorias')
    def get(self):
        """Obtener todas las categorías"""
        categorias = Categoria.get_all()
        return jsonify(categorias)

    @categoria_ns.expect(categoria_model)
    @categoria_ns.doc('create_categoria')
    def post(self):
        """Crear una nueva categoría"""
        data = request.get_json()
        Categoria.create(data)
        return jsonify({'message': 'Categoría creada con éxito'}), 201

@categoria_ns.route('/<int:id>')
class CategoriaDetail(Resource):
    @categoria_ns.doc('get_categoria')
    def get(self, id):
        """Obtener una categoría por su ID"""
        categoria = Categoria.get_by_id(id)
        if categoria:
            return jsonify(categoria)
        return jsonify({'message': 'Categoría no encontrada'}), 404

    @categoria_ns.expect(categoria_model)
    @categoria_ns.doc('update_categoria')
    def put(self, id):
        """Actualizar una categoría existente"""
        data = request.get_json()
        updated = Categoria.update(id, data)
        if updated:
            return jsonify({'message': 'Categoría actualizada con éxito'})
        return jsonify({'message': 'Categoría no encontrada'}), 404

    @categoria_ns.doc('delete_categoria')
    def delete(self, id):
        """Eliminar una categoría"""
        deleted = Categoria.delete(id)
        if deleted:
            return jsonify({'message': 'Categoría eliminada con éxito'})
        return jsonify({'message': 'Categoría no encontrada'}), 404
