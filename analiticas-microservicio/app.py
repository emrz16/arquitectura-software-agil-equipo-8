from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from .modelos import db
from .vistas import VistaAnaliticas
from .modelos import Candidato
import random
from faker import Faker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbapp.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

cors = CORS(app)

api = Api(app)
api.add_resource(VistaAnaliticas, '/analitica')

REQUEST_INTERVAL = 30
fake = Faker()
def generar_cantidatos(n=20):
    for x in range(n):
        nombre_candidato = fake.name()
        profesion_candidato = fake.job()
        edad_candidato = random.randint(20, 50)
        telefono_candidato = fake.phone_number()
        nuevo_candidato = Candidato(nombre=nombre_candidato, profesion=profesion_candidato,
                                    edad=edad_candidato, telefono=telefono_candidato)
        db.session.add(nuevo_candidato)
        db.session.commit()

generar_cantidatos()
