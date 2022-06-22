import json

from flask import Blueprint, Response, request
from flask_restx import Namespace, Resource

from dtos.ErroDto import ErroDto
from dtos.UsuarioDto import UsuarioCreateDto
from services.UsuarioService import UsuarioService

usuario_controller = Blueprint('usuario_controller', __name__)

api = Namespace('Usuário', description="Rota de usuário")


@api.route('/', methods=['GET', 'POST'])
class UsuarioController(Resource):
    def post(self):
        try:
            body = request.get_json()
            if "nome" not in body or "email" not in body or "senha" not in body:
                return Response(
                    json.dumps(ErroDto("Parâmetros inválidos", 401).__dict__),
                    status=401,
                    mimetype='application/json'
                )

            usuario_criado = UsuarioService().criar_usuario(body['nome'], body['email'], body['senha'])

            if not usuario_criado:
                return Response(
                    json.dumps(ErroDto('E-mail já cadastrado', 400).__dict__),
                    status=400,
                    mimetype='application/json'
                )

            return Response(
                json.dumps(UsuarioCreateDto(usuario_criado.id, usuario_criado.nome, usuario_criado.email,
                                            usuario_criado.senha).__dict__),
                status=201,
                mimetype='application/json'
            )
        except Exception:
            return Response(
                json.dumps(ErroDto("Não foi possível efetuar a requisição, tente novamente mais tarde", 500).__dict__),
                status=500,
                mimetype='application/json')
