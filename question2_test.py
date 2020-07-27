import unittest
from question2 import print_depth,Person,a



class testquestion2(unittest.TestCase):
    def test_path_func(self):
        ans='key1: 1\nkey2: 1\nkey3: 2\nkey4: 2\nkey5: 3\nuser: 3\nfirst_name: 4\nlast_name: 4\nfather: 4\nfirst_name: 5\nlast_name: 5\nfather: 5\n'        
        out = print_depth(a)
        self.assertEquals(ans,out)