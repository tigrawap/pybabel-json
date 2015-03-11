import re
from subprocess import PIPE, Popen
import os

__author__ = 'tigra'


import unittest

class TestExtraction(unittest.TestCase):

    def setUp(self):
        stderr = None if 'PYBABEL_JSON_DEBUG' in os.environ else PIPE
        dirname = os.path.dirname(__file__)
        cfg = 'babel.cfg'
        pot_file = 'messages.pot'

        self.found_transes = Popen(['pybabel','extract','-F',cfg,'-o',pot_file,'.'],stdout=PIPE,stderr=stderr).stdout.read()
        with open(pot_file, 'r') as output:
            self.output = output.read()

    def test_number_of_occurences(self):
        self.assertEqual(len(re.findall(r'msgid "',self.output)),1+10,"Wrong number of found translations")
        self.assertEqual(len(re.findall(r'msgid_plural',self.output)),4,"Wrong number of plural translations")



if __name__ == '__main__':
    unittest.main()
