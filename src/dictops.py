import logging
class dict_mgm:
	logging.basicConfig(level=logging.DEBUG)
	#creates ansible command to run
	def make_play(data,db_data,location):
		if dict_mgm.data_check(data, db_data) == 'OK':
			command = 'ansible-playbook {location}'.format(location=location)
			#did and incredi bad if else thing
			logging.debug(data.keys())
			command+=data['name']+' '
			if 'params' in data.keys():
				command+= dict_mgm.sort_params(data['params'])
			if 'args' in data.keys():
				command+= dict_mgm.sort_args(data['args'])
			if 'password' in data.keys():
				password = data['password']
			else:
				password = None
			logging.debug(command)
			logging.debug(password)
			return command, password
		else:
			return 'Error', None
			
	#check integrity of submitted data compared to its schema model
	def data_check(data,db_data):
		logging.debug(data)
		logging.debug(db_data)
		if len(data) != len(db_data):
			logging.debug('triggered 1')
			return 'Error'

		if data.keys() != db_data.keys():
			logging.debug('triggered 2')
			return 'Error'
		
		if len(data.values()) != len(db_data.values()):
			logging.debug('triggered 3')
			return 'Error'
		#for playbooks that have no params/args
		try:
			if len(data['params']) != len(db_data['params']):
				logging.debug('triggered 4')
				return 'Error'
		except KeyError:
			pass

		try:
			if len(data['args']) != len(db_data['args']):
				logging.debug('triggered 5')
				return 'Error'
		except KeyError:
			pass
		logging.debug('OK')
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