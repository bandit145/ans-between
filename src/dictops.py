import logging
class dict_mgm:
	logging.basicConfig(level=logging.DEBUG)
	#creates ansible command to run
	def make_play(data,db_data):
		if dict_mgm.data_check(data, db_data) == 'OK':
			command = 'ansible_playbook '
			#did and incredi bad if else thing
			command+=data['name']+' '
			command+= dict_mgm.sort_params(data['params'])
			command+= dict_mgm.sort_args(data['args'])
			if 'password' in data.keys():
				password = data['password']
			else:
				password = None
			return command, password
		else:
			return 'Error', None
			
	#check integrity of submitted data compared to its schema model
	def data_check(data,db_data):
		print(data)
		print(db_data)
		if len(data) != len(db_data):
			logging.debug('triggered 1')
			return 'Error'

		elif data.keys() != db_data.keys():
			logging.debug('triggered 2')
			return 'Error'
		
		elif len(data.values()) != len(db_data.values()):
			logging.debug('triggered 3')
			return 'Error'
		
		elif len(data['params']) != len(db_data['params']):
			logging.debug('triggered 4')
			return 'Error'

		elif len(data['args']) != len(db_data['args']):
			logging.debug('triggered 5')
			return 'Error'
		else:
			return 'OK'

	def sort_params(params):#deals with param dics
		command = '' 
		for item in params:
			keys= list(item.keys())
			values= list(item.values())
			logging.debug(keys)
			logging.debug(values)
			command+=keys[0]+' '+values[0]+' '
		return command
	
	def sort_args(args): #deals with args list
		command = ''
		for arg in args:
			command+= arg+' '
		return command