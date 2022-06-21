import json
from functools import wraps

import jwt
from flask import request, Response

import config
from dtos.ErroDto import ErroDto
from dtos.UsuarioDto import UsuarioBaseDto
from services import JWTService


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

            usuario_atual = UsuarioBaseDto("Gabriel Tonete", config.LOGIN_TESTE)
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

    return decorated
