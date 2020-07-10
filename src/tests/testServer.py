import unittest 
import jsonpickle
import json
from server import app

class TestServer(unittest.TestCase): 

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_home(self):
        result = self.app.get('/') 
        self.assertEqual(result.status_code, 200) 

    def test_post_resource_errors_no_contents(self):
        result = self.app.post('/resource', content_type='application/json') 
        self.assertEqual(result.status_code, 400) 
        result = jsonpickle.decode(result.data)
        self.assertEqual(result['error'], 'No request contents', 'Should be No request contents')
    
    def test_post_resource_errors_no_json(self):
        result = self.app.post('/resource', data=json.dumps({'text':'test'}))
        self.assertEqual(result.status_code, 400) 
        result = jsonpickle.decode(result.data)
        self.assertEqual(result['error'], 'Request content not in JSON format', 'Request content not in JSON format')

if __name__ == '__main__':
    unittest.main()