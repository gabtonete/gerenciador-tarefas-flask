class UsuarioBaseDto:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class UsuarioCreateDto(UsuarioBaseDto):
    def __init__(self, id, nome, email, senha):
        super().__init__(nome, email)
        self.id = id
        self.senha = senha


class UsuarioLoginDto(UsuarioBaseDto):
    def __init__(self, nome, email, token):
        super().__init__(nome, email)
        self.token = token
