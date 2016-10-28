import unittest
from src.db import *
from src.dicto import *
class TestDB(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.testdb = db()
		self.dbdict = self.testdb.db_lookup('test1')

	def test_createdb(self):
		#return dict from db create function and test that thr last test is in it
		self.assertTrue(self.dbdict['name'] == 'test1')

	def test_params(self):
		#test for parameter syntax
		self.assertTrue(self.dbdict['params'][0] == {'-i':'192.168.1.8'})
		
	def test_args(self):
		#test for args
		self.assertTrue(self.dbdict['args'] == ['arg1','arg2'])

class TestDM(unittest.TestCase):#dict mgmt
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.dictmgm  = dict_mgm()#dictionary passed to fill up
	#need shit down here boy
	def test_insert(self):
		#defined in schema for each book will have the params/args empty to be filled in by request
		#web request will have params as such
		#{'param':'info', 'param':'info'}
		#This will be looped through pulling out the info and popping 
		#it into the dict template from the db
		self.assertTrue(self.dictmgm.dict('dict from user to parse') == #result)
		



if __name__=='__main__':
	unittest.main()