from flask_restx import Api

from .namespace1 import api as ns1
from .namespace2 import api as ns2
from .blocks import api as blocks

api = Api(
    title='My Title',
    version='1.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(ns1)
api.add_namespace(ns2)
api.add_namespace(blocks)
