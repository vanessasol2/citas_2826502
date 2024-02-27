from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#####importar el config
from .config import Config


#########Crear objecto de aplicacion
app = Flask(__name__)

#####configurar el objecto flask con el config
app .config.from_object(Config)

#####objecto SQLALchemy
db = SQLAlchemy(app)

######objecto para las migraciones
migrate = Migrate(app, db)

######importar los modelos 
from .models import Medico, Paciente, Consultorio, Cita

#########ejecutarnel objecto
if __name__=='__main__':
    app.run()