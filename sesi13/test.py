import unittest

from directors import read_all, read_one
from movies import read_all, read_one


class TestDirectors(unittest.TestCase):
    """
    Testing read all data directors
    """
    def test_read_all(self):
        self.assertIs(type(read_all()), list)
        

    def test_read_all_err(self):
        self.assertIsNot(type(read_all()), dict)


class TestMovies(unittest.TestCase):
    """
    Testing read all data movies
    """
    def test_read_all(self):
        self.assertIs(type(read_all()), list)
    """
    Testing read satu data movies dengan movie_id=43597
    """
    def test_read_one(self):
        self.assertIs(type(read_one(movie_id=43597)), dict)

if __name__ == '__main__':
    unittest.main()