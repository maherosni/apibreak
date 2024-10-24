from flask import Flask, request, render_template
from flask_restx import Api, Resource, Namespace, fields
from controllers.categorias_controller import categoria_ns
from controllers.product_controller import product_ns
from controllers.user_controller import user_ns  # Asegúrate de importar tu Namespace
from controllers.cart_controller import cart_ns

app = Flask(__name__)

# Crear una sola instancia de API
api = Api(app, version='1.0', title='API de Gestión',
          description='API para la gestión de carrito, productos, usuarios y categorías',
          doc='/documentacion')  # Cambia la ruta de Swagger a /documentacion

# Registrar los namespaces
api.add_namespace(cart_ns, path='/carrito')
api.add_namespace(product_ns, path='/productos')
api.add_namespace(user_ns, path='/usuarios')
api.add_namespace(categoria_ns, path='/categorias')

# Si estás usando Blueprints (solo descomenta si los necesitas)
# app.register_blueprint(categoria_bp)
# app.register_blueprint(product_bp)
# app.register_blueprint(user_bp)
# app.register_blueprint(cart_bp)

if __name__ == '__main__':
    app.run(debug=True)