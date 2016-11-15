class dict_mgm:
	#create ansible command to run
	def make_play(self,data,db_data):
		if self.data_check(data, db_data) == 'OK':
			command = 'ansible_playbook '
			#did and incredi bad if else thing
			command+=data['name']+' '
			command+= self.sort_params(data['params'])
			command+= self.sort_args(data['args'])
			if 'password' in data.keys():
				password = data['password']
			else:
				password = None
			return command, password
		else:
			return 'Error'	
			
	#check integrity of submitted data compared to its schema model
	def data_check(self, data,db_data):
		if len(data) != len(db_data):
			return 'Error'

		elif data.keys() != db_data.keys():
			return 'Error'
		
		elif len(data.values()) != len(db_data.values()):
			return 'Error'
		
		elif len(data['params']) != len(db_data['params']):
			return 'Error'

		elif len(data['args']) != len(db_data['args']):
			return 'Error'
		else:
			return 'OK'

	def sort_params(self,params):#deals with param dicts
		command = '' 
		for item in params:
			keys= list(item.keys())
			values= list(item.values())
			command+=keys[0]+' '+values[0]+' '
		return command
	
	def sort_args(self, args): #deals with args list
		command = ''
		for arg in args:
			command+= arg+' '
		return command