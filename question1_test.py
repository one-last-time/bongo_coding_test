import unittest
from question1 import print_depth

class testquestion1(unittest.TestCase):
    def  test_print_depth(self):
        a= {'key1':1,
            'key2':{
                    'key3':1,
                    'key4':{
                            'key5':5,
                             }
                     }
            }
        ans='key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\n'
        self.assertEqual(print_depth(a),ans) 