from flask_restx import Api
from .namespace1 import api as ns1
from .namespace2 import api as ns2
from .blocks_api import api as blocks

api = Api(
    etitle='The APIs',
    version='1.0',
    description='THese are some APIs',
)

api.add_namespace(ns1)
api.add_namespace(ns2)
api.add_namespace(blocks)
