import logging
import os
from logging.handlers import RotatingFileHandler

from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = "login"
mail = Mail(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
babel = Babel(app)

from app import routes, models, errors

if not app.debug:

    if not os.path.exists("logs"):
        os.mkdir("logs")

    file_handler = RotatingFileHandler("logs/microblog.log",

                                       maxBytes=100 * 1024 * 1024,
                                       backupCount=7)
    formatter = logging.Formatter("[%(asctime)s %(levelname)s ][%(message)s  ]")
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info("Microblog startup")


@babel.localeslector
def get_locale():
    return request.accept_languages.best_match(app.config["LANGUAGES"])
