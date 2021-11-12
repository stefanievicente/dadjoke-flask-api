from flask import Flask
from flask_restful import Api

from joke import DadJoke
from errors import errors

app = Flask(__name__)
api = Api(app, errors=errors)

api.add_resource(DadJoke, '/', '/dadjoke')

if __name__ == '__main__':
    app.run(debug=True)