from flask import Response, jsonify
import requests
from flask_restful import Resource

from errors import InternalServerError

class DadJoke(Resource):
    def get(self):
        try:
            req = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
            return Response(req)
        except Exception:
            raise InternalServerError
            
    