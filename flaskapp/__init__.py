import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    env_var = app.config.get('TEST_ENV_VARIABLE', "not set")
    env_var2 = os.environ['TEST_ENV_VARIABLE']

    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # config
    @app.route('/config')
    def config():
        ret = f'Hey.  Env: {env_var}, and Env2: {env_var2}'
        return ret

    # a simple page that says hello
    @app.route('/goodbye')
    def goodbuy():
        return 'Goodbye cruel world!'

    return app

