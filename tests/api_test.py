import unittest
from appfactory import create_app

class TestApi(unittest.TestCase):
    
    def setUp(self) -> None:
        pass
        app = create_app()
        self.app = app.test_client()


    def test_ns1(self):
        
        expected = b'{"id": "felix", "name": "Felix"}'
        getcats = self.app.get('cats/')
        self.assertTrue( expected in getcats.data )
