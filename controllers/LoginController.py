from flask import Blueprint, Response, request
from flask_restx import Namespace, Resource, fields

import json

from dtos.ErroDto import ErroDto

login_controller = Blueprint('login_controller', __name__)

api = Namespace('Login', description="Realizar login na aplicação")

login_fields = api.model('LoginDTO', {
    "login": fields.String,
    "senha": fields.String
})

@api.route('/login', methods=['POST'])
class Login(Resource):
    @api.doc(responses={200: 'Login realizado com sucesso'})
    @api.doc(responses={400: 'Parâmetros de entrada inválidos'})
    @api.doc(responses={500: 'Não foi possível efetuar o login, tente novamente maist arde'})
    @api.response(200, 'Success')
    @api.expect(login_fields)
    def post(self):
        try:
            body = request.get_json()

            if not body or "login" not in body or "senha" not in body:
                return Response(
                    'Parâmetros de entrada inválidos',
                    status=400,
                    mimetype='application/json')

            return Response(json.dumps(ErroDto('Usuário autenticado com sucesso', status=200).__dict__),
                            mimetype='application/json')
        except Exception as e:
            return Response(json.dumps(
                ErroDto("Não foi possível efetuar o login, tente novamente mais tarde", status=500).__dict__),
                            mimetype='application/json')
