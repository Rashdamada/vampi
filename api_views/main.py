from flask import Response

from models.user_model import *
from env import vuln

WAS_CALLED = False


def populate_db():
    global WAS_CALLED
    if WAS_CALLED:

        response = Response(
            '{ "message": "Database already populated." }',
            200,
            mimetype="application/json",
        )
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response
    WAS_CALLED = True
    db.drop_all()
    db.create_all()
    User.init_db_users()
    response_text = '{ "message": "Database populated." }'
    response = Response(response_text, 200, mimetype="application/json")
    response.headers["Access-Control-Allow-Origin"] = "*"
    # response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response

def basic():
    response_text = '{ "message": "VAmPI the Vulnerable API", "help": "VAmPI is a vulnerable on purpose API. It was ' \
                    'created in order to evaluate the efficiency of third party tools in identifying vulnerabilities ' \
                    'in APIs but it can also be used in learning/teaching purposes.", "vulnerable":' + "{}".format(vuln) + "}"
    response = Response(response_text, 200, mimetype='application/json')
    #response.headers['Access-Control-Allow-Origin'] = 'http://foo.example'
    #response.headers['Access-Control-Allow-Credentials'] = 'false'
    return response
