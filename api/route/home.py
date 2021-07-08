from http import HTTPStatus
from flask import current_app
from flask import Blueprint
from flasgger import swag_from
from api.schema.hello import HelloSchema
from api.model.hello import HelloModel

home_api = Blueprint('api', __name__)

@home_api.route('/')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome to the Flask Starter Kit',
            'schema': HelloSchema
        }
    }
})
def welcome():
    """
    1 liner about the route
    A more detailed description of the endpoint
    ---
    """
    result = HelloModel()
    return HelloSchema().dump(result), 200


@home_api.route('/hello')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'response from hello'
        }
    }
})
def hello():
    """
    this is the first line description

    this is the more detailed description 
    of teh service
    ---
    """
    result = HelloModel()
    result.message = 'hi rich'
    return HelloSchema().dump(result), 200



@home_api.route('/config')
@swag_from({
    'responses': {
            HTTPStatus.OK.value: {
                'description': 'response from config'
            }
        }
})
def config():
    ret = f'Hey.  Env: {current_app.config["TEST_ENV_VARIABLE"]}'
    return ret

@home_api.route('/goodbye')
@swag_from({
    'responses': {
            HTTPStatus.OK.value: {
                'description': 'response from goodbye'
            }
        }
})
def goodbuy():
    return 'Goodbye cruel world!',200
