import json
from functools import wraps

import jwt
from flask import request, Response

from dtos.ErroDto import ErroDto
from services import JWTService
from services.UsuarioService import UsuarioService


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        headers = request.headers

        if not 'Authorization' in headers:
            return Response(
                json.dumps(ErroDto("E necessario um token para essa requisiçao", 400).__dict__),
                status=400,
                mimetype="application/json"
            )

        try:
            token = str(headers['Authorization'].replace('Bearer ', ''))
            user_id = JWTService.decodificar_token(token)
            print(user_id)

            usuario_atual = UsuarioService().filtrar_por_id(user_id['id_usuario'])

            if not usuario_atual:
                return Response(
                    json.dumps(ErroDto("Token não autorizado", 401).__dict__),
                    status=401,
                    mimetype='application/json'
                )

        except jwt.ExpiredSignatureError:
            return Response(
                json.dumps(ErroDto("Token expirado", 401).__dict__),
                status=401,
                mimetype='application/json'
            )

        except jwt.InvalidTokenError:
            return Response(
                json.dumps(ErroDto("Token não autorizado", 401).__dict__),
                status=401,
                mimetype='application/json'
            )

        except Exception:
            return Response(
                json.dumps(ErroDto("Não foi possível efetuar a requisição, tente novamente mais tarde", 500).__dict__),
                status=500,
                mimetype='application/json'
            )

        return f(usuario_atual)

    return decorated
