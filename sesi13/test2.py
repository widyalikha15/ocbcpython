import unittest
from directors import read_all, read_one
from movies import read_all, read_one
import config

connex_app = config.connex_app
connex_app.add_api("swagger.yml")

class Test(unittest.TestCase):
    '''
    Test read_all
    '''
    def test_get_directors(self):
        self.assertIs(type(read_all), list)

    def test_get_movies(self):
        self.assertIs(type(read_all), list)
    
    '''
    Test read_one
    '''
    def test_get_director(self):
        self.assertIs(type(read_one(7110)), dict)

    def test_get_movie(self):
        self.assertIs(type(read_one(7110,48399)), dict)

class MyTestCase(unittest.TestCase):
    '''
    Test connexion
    '''
    def setUp(self):
        connex_app.app.testing = True
        self.connex_app = connex_app.app.test_client()
    '''
    Test route is success or not
    '''
    def test_directors(self):
        result = self.connex_app.get('/api/directors')
        self.assertEqual(result.status_code, 200)

    def test_movies(self):
        result = self.connex_app.get('/api/movies')
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()