from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage
import ast
class db_mgm:
	def __init__(self):
		self.db = TinyDB('database/db.json')
		self.output = self.db.table('output')
		self.query = Query()
		
	def start_db(self):
		#load db
		with open('schema') as schema:
			for line in schema:
				self.db.insert(ast.literal_eval(line))

	def db_lookup(self,playbook):
		#grab playbook
		if self.db.contains(self.query.name == playbook):
			response = self.db.search(self.query.name == playbook)
			response = response[0]
			return response
		else:
			return 'Error'
	
	def db_outputid(self):
		items = len(self.output)
		return str(items+1)
		
	def db_stdoutinput(self, data):
		items = self.db_outputid()
		self.output.insert({'id':items,'output':data})

	def db_updateinput(self, data, taskid):
		self.output.update({'id':taskid,'output':data}, self.query.id == taskid)

	def db_completed(self, taskid):
		output = self.output.get(self.query.id == taskid)
		output = output['output']
		return output

	def db_exit(self):
		self.db.purge_tables()
