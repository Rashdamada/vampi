import os
from logging.config import dictConfig

import connexion
from flask import request
from flask_sqlalchemy import SQLAlchemy
from env import FLASK_DEBUG

if FLASK_DEBUG:
    dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {
                    "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
                },
                "simpleformatter": {
                    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                },
            },
            "handlers": {
                "wsgi": {"class": "logging.StreamHandler", "formatter": "default"},
                "custom_handler": {
                    "class": "logging.FileHandler",
                    "formatter": "simpleformatter",
                    "filename": "WARN.log",
                    "level": "WARN",
                },
            },
            "root": {"level": "INFO", "handlers": ["wsgi", "custom_handler"]},
        }
    )


vuln_app = connexion.App(__name__, specification_dir='./openapi_specs')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(vuln_app.root_path, 'database/database.db')
vuln_app.app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
vuln_app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if FLASK_DEBUG:
    vuln_app.app.logger.info("Logging all request for FLASK_DEBUG!")

vuln_app.app.config['SECRET_KEY'] = 'random'
# start the db
db = SQLAlchemy(vuln_app.app)

vuln_app.add_api("openapi3.yml")


if FLASK_DEBUG:

    @vuln_app.app.after_request
    def log_after_request(response):
        vuln_app.app.logger.info(
            "path: %s | method: %s | headers: %s | body: %s | status: %s | size: %s",
            request.path,
            request.method,
            str(request.headers),
            str(request.data),
            response.status,
            response.content_length,
        )

        return response
