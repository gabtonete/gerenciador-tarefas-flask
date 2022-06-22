import sqlalchemy as db
# specify database configurations
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import config

db_user = config.MYSQL_USER
db_pwd = config.MYSQL_PASSWORD
db_host = config.MYSQL_HOST
db_port = config.MYSQL_PORT
db_name = config.MYSQL_DATABASE
# specify connection string
connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
# connect to database
engine = db.create_engine(connection_str)
engine.execute(f'CREATE DATABASE IF NOT EXISTS {config.MYSQL_DATABASE}')
engine.execute(f'USE {config.MYSQL_DATABASE}')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# connection = engine.connect()
# # pull metadata of a table
# metadata = db.MetaData(bind=engine)
# metadata.reflect(only=['test_table'])
#
# test_table = metadata.tables['test_table']
# test_table
