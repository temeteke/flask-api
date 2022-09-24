import platform

import requests
from flask import Flask
from flask_healthz import healthz
from flask_restx import Api, Resource

app = Flask(__name__)

app.register_blueprint(healthz, url_prefix="/healthz")
app.config['HEALTHZ'] = {
    "live": lambda: None,
    "ready": lambda: None,
}

api = Api(app)

@api.route('/hello')
class Hello(Resource):
    def get(self):
        return "hello"

@api.route('/hostname')
class HostName(Resource):
    def get(self):
        return platform.node()

@api.route('/ipinfo')
class IpinfoResource(Resource):
    def get(self):
        return requests.get('https://ipinfo.io/').json()
