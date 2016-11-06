#!/usr/bin/env python3
import unittest
from src.db import *
from src.dictops import *
class TestDB(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.testdb = db_mgm()
		self.dbdict = self.testdb.db_lookup('test1')

	def test_createdb(self):
		#return dict from db create function and test that the last test is in it
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
		self#dictionary passed to fill up
	#need shit down here boy
	def test_datacheck(self):
		self.assertTrue(dict_mgm.data_check({'name':'test1','params':[{'-i','thinginign'},{}],'args':['arg1','arg2']},{'name':'test1','params':[{},{}],'args':['arg1','arg2']}) == 'OK')
		self.assertTrue(dict_mgm.data_check({'name':'test1','params':[{}],'args':['arg1','arg2']},{'name':'test1','params':[{},{}],'args':['arg1','arg2']}) == 'Error')
		#eventually run through and try every type of broken dict possible
	def test_sortparams(self):
		self.assertTrue(dict_mgm.sort_params([{'-i':'inv'},{'-i':'otherinv'}]) == '-i inv -i otherinv ' )

	def test_sortargs(self):
		self.assertTrue(dict_mgm.sort_args(['arg1','arg2']) == 'arg1 arg2 ')

	def test_insert(self):
		#defined in the schema for each book will be the params/args empty to be filled in by request
		#web request will have params as such
		#{'param':'info', 'param':'info'}
		#This will be looped through pulling out the info and popping 
		#it into the dict template from the db
		self.assertTrue(dict_mgm.make_play({'name':'test1','params':[{'-i':'192.168.1.8'}],'args':['arg1','arg2']},{'name':'test1','params':[{'-i':'192.168.1.8'}],'args':['arg1','arg2']}) == ('ansible_playbook test1 -i 192.168.1.8 arg1 arg2 ', None))
		self.assertTrue(dict_mgm.make_play({'name':'test1','params':[{'-i':'192.168.1.8'}],'args':['arg1','arg2'],'password':'123456'},{'name':'test1','params':[{'-i':'192.168.1.8'}],'args':['arg1','arg2'],'password':'123456'}) == ('ansible_playbook test1 -i 192.168.1.8 arg1 arg2 ', '123456'))
		#TODO: test looking for password in password dict	


if __name__=='__main__':
	unittest.main()