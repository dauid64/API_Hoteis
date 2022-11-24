from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from flask_jwt_extended import jwt_required
import sqlite3
from resources.filtros import normalize_path_params, consulta_sem_cidade, consulta_com_cidade
from models.site import SiteModel

# path /hoteis?cidade=Rio de Janeiro&estrelas_min=4&diaria_max=400
path_param = reqparse.RequestParser()
path_param.add_argument('cidade', type=str)
path_param.add_argument('estrelas_min', type=float)
path_param.add_argument('estrelas_max', type=float)
path_param.add_argument('diaria_min', type=float)
path_param.add_argument('diaria_max', type=float)
path_param.add_argument('limit', type=float)
path_param.add_argument('offset', type=float)


class Hoteis(Resource):
    def get(self):

        connection = sqlite3.connect('instance/banco.db')
        cursor = connection.cursor()

        dados = path_param.parse_args()

        #                cidade: None
        dados_validos = {chave:dados[chave] for chave in dados if dados[chave] is not None}

        parametros = normalize_path_params(**dados_validos)

        #usar get para não quebrar o codigo se der None
        if not parametros.get('cidade'):
            tupla = tuple([parametros[chave] for chave in parametros])
            resultado = cursor.execute(consulta_sem_cidade, tupla)
        else:
            tupla = tuple([parametros[chave] for chave in parametros])
            resultado = cursor.execute(consulta_com_cidade, tupla)
        
        hoteis = []

        for linha in resultado:
            hoteis.append({
            'hotel_id': linha[0],
            'nome': linha[1],
            'estrelas': linha[2],
            'diaria': linha[3],
            'cidade': linha[4],
            'site_id': linha[5]
        })

        return {'hoteis': hoteis} # SELECT * FROM hoteis

# CRUD

class Hotel(Resource):

    # Pegando todos os args que o cliente passar
    argumentos = reqparse.RequestParser()
    # adicionando somente os que queremos
    argumentos.add_argument('nome', type=str, required=True, help="The field 'nome' cannot be left blank")
    argumentos.add_argument('estrelas', type=float, required=True, help="The field 'estrelas' cannot be left blank")
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')
    argumentos.add_argument('site_id', type=int, required=True, help="Every hotel needs to be linked with a site")

    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        return {'message': 'Hotel not found'}, 404 # not found

    @jwt_required()
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {"message": f"Hotel id '{hotel_id}' already exists."}, 400 # Bad Request

        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)

        if not SiteModel.find_by_id(dados.get('site_id')):
            return {'message': 'The hotel must be associated to a valid site id.'}, 400 # Bad Request

        try:
            hotel.save_hotel()
        except:
            return {'message': 'An internal error ocurred trying to save hotel.'}, 500 # Internal Server Error

        return hotel.json()

    @jwt_required()       
    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_encontrado = HotelModel.find_hotel(hotel_id)

        if hotel_encontrado: # se tiver algum hotel com este nome
            hotel_encontrado.update_hotel(**dados) # altera
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200

        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message': 'An internal error ocurred trying to save hotel.'}, 500 # Internal Server Error
        return hotel.json(), 201 # created criado

    @jwt_required()
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'message': 'An internal error ocurred trying to delete hotel.'}, 500 # Internal Server Error
                
            return {'message': 'Hotel Deleted.'}
        
        return {'message': 'Hotel not found.'}, 404


    