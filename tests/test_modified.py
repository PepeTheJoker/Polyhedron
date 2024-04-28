import unittest
from unittest.mock import patch, mock_open
from math import sqrt
from shadow.polyedr import Polyedr


class TestPolyedr(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """40.0	90	90	90
5	5	16
2	0	2
-2	0	2
-2	0	-2
2	0	-2
0	4	0
4	1    2    3    4
3	1    2    5
3	2    3    5
3	3    4    5
3	4    1    5"""
        fake_file_path = 'data/pyramid.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 5)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 5)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 16)

    def test_length(self):
        self.assertAlmostEqual(
            40 * (4 + 4 * sqrt(2)) * 2,
            self.polyedr.length
        )
