from flask import request, jsonify
from flask_restx import Api, Resource, Namespace, fields
from models.user_model import User

# Crear el Namespace para Swagger
user_ns = Namespace('usuarios', description='Operaciones relacionadas con usuarios')

# Modelo para la creación de usuarios en Swagger
register_model = user_ns.model('Register', {
    'username': fields.String(required=True, description='El nombre de usuario'),
    'email': fields.String(required=True, description='El correo del usuario'),
    'password': fields.String(required=True, description='La contraseña del usuario')
})

# Modelo para el login de usuarios en Swagger
login_model = user_ns.model('Login', {
    'username': fields.String(required=True, description='El nombre de usuario'),
    'password': fields.String(required=True, description='La contraseña del usuario')
})

# Rutas de la API usando Flask-RESTPlus
@user_ns.route('/register')
class RegisterUser(Resource):
    @user_ns.expect(register_model)
    @user_ns.doc('register_user')
    def post(self):
        """Registrar un nuevo usuario"""
        data = request.get_json()
        User.create(data)
        return jsonify({'message': 'Usuario registrado con éxito'}), 201


@user_ns.route('/login')
class LoginUser(Resource):
    @user_ns.expect(login_model)
    @user_ns.doc('login_user')
    def post(self):
        """Iniciar sesión como usuario"""
        data = request.get_json()
        user = User.authenticate(data['username'], data['password'])
        if user:
            return jsonify({'message': 'Login exitoso', 'user': user})
        return jsonify({'message': 'Credenciales incorrectas'}), 401