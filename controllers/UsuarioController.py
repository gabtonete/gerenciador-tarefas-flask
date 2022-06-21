from flask import Blueprint, Response
from flask_restx import Namespace, Resource

import config
import json

from dtos.ErroDto import ErroDto
from dtos.UsuarioDto import UsuarioBaseDto

usuario_controller = Blueprint('usuario_controller', __name__)

api = Namespace('Usuário', description="Rota de usuário")


@api.route('/', methods=['GET'])
class UsuarioController(Resource):
    def get(self):
        try:
            return Response(
                json.dumps(UsuarioBaseDto("Gabriel Tonete", config.LOGIN_TESTE).__dict__),
                status=200,
                mimetype="application/json"
            )
        except Exception:
            return Response(
                json.dumps(ErroDto("Não foi possível efetuar o login, tente novamente mais tarde", 500).__dict__),
                status=500,
                mimetype='application/json')
