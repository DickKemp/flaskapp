from __future__ import annotations
import flask
from flask_restx import Namespace, Resource, fields

from core.blokus import runn, SQUARE, TRIANGLE, ISOTRIANGLE, PENTAGON, HEXAGON
from io import StringIO

api = Namespace('blocks', description='blockus operations')

@api.route('/<shape>/<int:num>')
class Blocks(Resource):
    @api.doc('get shapes')
    def get(self, shape, num):
        '''get shapes'''

        stream = StringIO()
        if shape == 'square':
            runn("SQUARE", SQUARE, num, stream, True)
        elif shape == 'tri':
            runn("TRIANGLE", TRIANGLE, num, stream, True)
        elif shape == 'iso':
            runn("ISOTRIANGLE", ISOTRIANGLE, num, stream, False)
        elif shape == 'pent':
            runn("PENTAGON", PENTAGON, num, stream, True)
        elif shape == 'hex':
            runn("HEXAGON", HEXAGON, num, stream, True)
        else:
            return "INVALID SHAPE:  should be one of: square, tri, iso, pent, hex"

        response = flask.make_response(stream.getvalue())
        response.headers['content-type'] = 'image/svg+xml'
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'

        return response      
