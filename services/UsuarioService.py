from database.database import SessionLocal
from models.Usuario import Usuario

db = SessionLocal()


class UsuarioService:
    def __init__(self):
        pass

    def login(self, email, senha):
        usuario = db.query(Usuario).filter(Usuario.email == email).first()

