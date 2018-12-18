# -*- coding: utf-8 -*-
import unittest
import os
import sys
import glob

sys.path.insert(0,'../../')
from qifparse.parser import QifParser


class TestQIFParsing(unittest.TestCase):
    testfiles=[]
    standardFiles=[]
    transactionsfile=""
    @classmethod
    def setUpClass(cls):
        cls.transactionsfile = os.path.join(os.path.dirname(__file__), 'transactions_only.qif')
        cls.testfiles = glob.glob('file*.qif')
        cls.standardFiles = glob.glob('fileStandard*.qif')
    
    def testParseFile(self):
        for filename in self.testfiles:
            with open(filename) as f:
                qif = QifParser.parse(f)
                self.assertTrue(qif)

    def testWriteFile(self):
        for filename in self.standardFiles:
            with open(filename) as f:
                data = f.read()
                f.seek(0)
                qif = QifParser.parse(f)
        #        out = open('out.qif', 'w')
        #        out.write(str(qif))
        #        out.close()
                self.assertEquals(data, str(qif))

    def testParseTransactionsFile(self):
        with open(self.transactionsfile) as f:
            data = f.read()
            f.seek(0)
            qif = QifParser.parse(f)
    #        out = open('out.qif', 'w')
    #        out.write(str(qif))
    #        out.close()
            self.assertEquals(data, str(qif))

if __name__ == "__main__":
    import unittest
    unittest.main()
