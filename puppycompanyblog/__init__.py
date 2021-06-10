# puppycompanyblog/__init__
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



app = Flask(__name__)

##########################
# Database setup
#########################
basedir = os.path.abspath(os.path.dir(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)

###################################
######LOGIN CONFIGARATION#########
###################################

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'user.login'



# Registration Blueprint
from puppycompanyblog.core.views import core
from puppycompanyblog.error_pages.handlers import error_pages


app.register_blueprint(core)
app.register_blueprint(error_pages)
