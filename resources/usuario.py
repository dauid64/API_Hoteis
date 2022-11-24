from flask_restful import Resource, reqparse
from models.usuario import UserModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
import hmac
from blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('login', type = str, required=True, help="The field 'login' cannot be left blank")
atributos.add_argument('senha', type = str, required=True, help="The field 'senha' cannot be left blank")

class User(Resource):

    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return {'message': 'User not found'}, 404 # not found
            
    @jwt_required()
    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            try:
                user.delete_user()
            except:
                return {'message': 'An internal error ocurred trying to delete user.'}, 500 # Internal Server Error
                
            return {'message': 'User Deleted.'}
        
        return {'message': 'User not found.'}, 404

class UserRegister(Resource):
    def post(self):

        dados = atributos.parse_args()

        if UserModel.find_by_login(dados['login']):
            return {"message": f"The login '{dados['login']}' already exists."}
    
        user = UserModel(**dados)
        try:
            user.save_user()
        except:
            return {'message': 'An internal error ocurred trying to create a new user .'}, 500 # Internal Server Error
        return {'message': 'User created sucessfully'}, 201 # Created

class UserLogin(Resource):

    @classmethod
    def post(cls):
        dados = atributos.parse_args()

        user = UserModel.find_by_login(dados['login'])

        if user and hmac.compare_digest(user.senha, dados['senha']):
            token_de_acesso = create_access_token(identity=user.user_id)
            return {'acess_token': token_de_acesso}, 200
        
        return {'message': 'The username or password is incorrect.'}, 401 # Unauthorize

class UserLogout(Resource):

    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti'] # JWT Token Identifier
        BLACKLIST.add(jwt_id)
        return {'message': 'Logget out sucessfully'}, 200
