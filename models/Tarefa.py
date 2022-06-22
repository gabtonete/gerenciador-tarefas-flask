from sqlalchemy import Column, Integer, String, inspect, Date, ForeignKey

import config
from database.database import Base, engine, metadata


class Tarefa(Base):
    __tablename__ = 'tarefa'
    metadata

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    dataPrevistaConclusao = Column(Date)
    dataConclusao = Column(Date)

    idUsuario = Column(Integer, ForeignKey('usuario.id'))


if not inspect(engine).has_table('tarefa', schema=config.MYSQL_DATABASE):
    Tarefa.__table__.create(engine)
