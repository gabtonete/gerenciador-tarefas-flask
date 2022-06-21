import json

from flask import Blueprint, Response, request
from flask_restx import Namespace, Resource

import config
from dtos.ErroDto import ErroDto
from dtos.UsuarioDto import UsuarioBaseDto, UsuarioCreateDto
from utils import Decorators
from utils.Criptografia import criptografar_senha

usuario_controller = Blueprint('usuario_controller', __name__)

api = Namespace('Usuário', description="Rota de usuário")


@api.route('/', methods=['GET', 'POST'])
class UsuarioController(Resource):

    @Decorators.token_required
    def get(usuario):
        try:
            return Response(
                json.dumps(UsuarioBaseDto("Gabriel Tonete", config.LOGIN_TESTE).__dict__),
                status=200,
                mimetype="application/json"
            )

        except Exception:
            return Response(
                json.dumps(ErroDto("Não foi possível efetuar a requisição, tente novamente mais tarde", 500).__dict__),
                status=500,
                mimetype='application/json')

    def post(self):
        try:
            body = request.get_json()

            if "nome" not in body or "email" not in body or "senha" not in body:
                return Response(
                    json.dumps(ErroDto("Parâmetros inválidos", 401).__dict__),
                    status=401,
                    mimetype='application/json'
                )

            return Response(
                json.dumps(UsuarioCreateDto(body["nome"], body["email"], criptografar_senha(body["senha"])).__dict__),
                status=201,
                mimetype='application/json'
            )
        except Exception:
            return Response(
                json.dumps(ErroDto("Não foi possível efetuar a requisição, tente novamente mais tarde", 500).__dict__),
                status=500,
                mimetype='application/json')
