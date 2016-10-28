from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage
import ast
class db:
	def __init__(self):
		self.db = TinyDB(storage=MemoryStorage)
		self.playbooks = Query()
		#load db
		with open('schema') as schema:
			for line in schema:
				self.db.insert(ast.literal_eval(line))

	def db_lookup(self,playbook):
		#grab playbook
		if self.db.contains(self.playbooks.name == playbook):
			response = self.db.search(self.playbooks.name == playbook)
			response = response[0]
			return response
		else:
			return None
	




