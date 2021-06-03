from peewee import *
import dotenv
import os


dotenv.load_dotenv(os.getcwd() + '/config.env')
host_db, user_db, db_db, password_db, port_db = os.getenv('host'), os.getenv('user'), os.getenv('db'), os.getenv(
    'password'), os.getenv('port')
conn = MySQLDatabase(user=user_db, host=host_db, database=db_db, password=password_db)


class migrator(Model):
    class Meta:
        database = conn
