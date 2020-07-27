import unittest
from question3 import build_graph_and_query

class testLCA(unittest.TestCase):
    def test_graph_and_query(self):
        nd =[(1,None),(2,1),(3,1),(4,2),(5,2),(6,3),(7,3),(8,4),(9,4)]
        qs=[(9,5),(1,9),(1,7),(4,9),(9,7),(1,1)]
        ans=[2,1,1,4,1,1]
        self.assertEqual(build_graph_and_query(nd,qs),ans)
        