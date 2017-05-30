#!/usr/bin/env python3
import unittest
from src.db import *
from config import dbdir, schemaloc
from src.dictops import *
from cel.tasks import run_command
class TestDB(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.testdb = db_mgm(dbdir)
		self.testdb.start_db(schemaloc)
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
	#dictionary passed to fill up
	def test_datacheck(self):
		self.assertTrue(dict_mgm.data_check({'name':'test1','params':[{'-i','192.168.1.34'},{}],'args':['arg1','arg2']},{'name':'test1','params':[{'-i':'192.168.1.34'},{}],'args':['arg1','arg2']}) == 'OK')
		#test param eval
		self.assertTrue(dict_mgm.data_check({'name':'test1','params':[{}],'args':['arg1','arg2']},{'name':'test1','params':[{},{}],'args':['arg1','arg2']}) == 'Error')
		#test args eval 
		self.assertTrue(dict_mgm.data_check({'name':'test1','params':[{},{}],'args':['arg1','arg2']},{'name':'test1','params':[{},{}],'args':['arg2']}) == 'Error')
		#eventually run through and try every type of broken dict possible
		#test with no params
		self.assertTrue(dict_mgm.data_check({'name':'test1','args':['arg1','arg2']},{'name':'test1','args':['arg1','arg2']}) == 'OK')
		#no args test
		self.assertTrue(dict_mgm.data_check({'name':'test1','params':[{},{}]},{'name':'test1','params':[{},{}]}) == 'OK')
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
		self.assertTrue(dict_mgm.make_play({'name':'test1','params':[{'-i':'192.168.1.8'}],'args':['arg1','arg2']},{'name':'test1','params':[{'-i':'192.168.1.8'}],'args':['arg1','arg2']},'/') == ('ansible-playbook /test1 -i 192.168.1.8 arg1 arg2 ', None))
		self.assertTrue(dict_mgm.make_play({'name':'test1','params':[{'-i':'192.168.1.8'}],'args':['arg1','arg2'],'password':'123456'},{'name':'test1','params':[{'-i':'192.168.1.8'}],'args':['arg1','arg2'],'password':'123456'},'/') == ('ansible-playbook /test1 -i 192.168.1.8 arg1 arg2 ', '123456'))
		#TODO: test looking for password in password dict	


class celeryTest(unittest.TestCase):
	#testing celery functions
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.db = db_mgm(dbdir)
		self.db.start_db(schemaloc)
	def test_runcommand(self):
		self.db.db_stdoutinput('placeholder')
		run_command('echo test',None, '1', self.db)
		#print(':'.join(['{:02x}'.format(ord(x)) for x in self.db.db_completed('1')])) 
		self.assertTrue(self.db.db_completed('1') == 'test\r\n')


if __name__=='__main__':
	unittest.main()
