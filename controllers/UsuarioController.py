import json

from flask import Blueprint, Response
from flask_restx import Namespace, Resource

import config
from dtos.ErroDto import ErroDto
from dtos.UsuarioDto import UsuarioBaseDto
from utils import Decorators

usuario_controller = Blueprint('usuario_controller', __name__)

api = Namespace('Usuário', description="Rota de usuário")


@api.route('/', methods=['GET'])
class UsuarioController(Resource):

    @Decorators.token_required
    def get(self):
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
