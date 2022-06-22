import json

from flask import Blueprint, Response, request
from flask_restx import Namespace, Resource, fields

from dtos.ErroDto import ErroDto
from dtos.UsuarioDto import UsuarioLoginDto
from services import JWTService
from services.UsuarioService import UsuarioService

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
    @api.doc(responses={500: 'Não foi possível efetuar o login, tente novamente mais tarde'})
    @api.response(200, 'Success')
    @api.expect(login_fields)
    def post(self):
        try:
            body = request.get_json()

            erros = []

            if not body:
                return Response(
                    json.dumps(ErroDto("Body não pode ser vazio", 400).__dict__),
                    status=400,
                    mimetype='application/json'
                )

            if "login" not in body or "senha" not in body:
                erros.append("Parâmetros inválidos")

            if erros:
                return Response(
                    json.dumps(ErroDto(erros, 400).__dict__),
                    status=400,
                    mimetype='application/json'
                )

            usuario_encontrado = UsuarioService().login(body["login"], body["senha"])

            if usuario_encontrado:
                token = JWTService.gerar_token(usuario_encontrado.id)

                return Response(
                    json.dumps(UsuarioLoginDto(usuario_encontrado.nome, usuario_encontrado.email, token).__dict__),
                    status=200,
                    mimetype='application/json'
                )

            return Response(
                json.dumps(ErroDto("Usuário ou senha inválidos", 401).__dict__),
                status=401,
                mimetype="application/json")
        except Exception as e:
            return Response(
                json.dumps(ErroDto("Não foi possível efetuar o login, tente novamente mais tarde", 500).__dict__),
                status=500,
                mimetype='application/json')
