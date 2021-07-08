import os
from flask import Flask
from flasgger import Swagger
from api.route.home import home_api

def create_app(test_config=None):

    app = Flask(__name__, static_url_path='', static_folder='api/static')

    app.config['SWAGGER'] = {
        'title': 'The Rich API'
    }
    
    app.config["TEST_ENV_VARIABLE"] = os.environ['TEST_ENV_VARIABLE']

    swagger = Swagger(app)

    app.register_blueprint(home_api, url_prefix='/api')

    return app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(port=port)

