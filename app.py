<<<<<<< HEAD
#!/usr/bin/env python3
from bottle import route, run, request, response
from src.db import *
from src.dictops import *
import pexpect
import json
import subprocess

def run_command(command, password):
	process = pexpect.spawnu(command)
	if '-K' in command or '--ask-sudo-pass' in command or '-k' in command or '--ask-pass' in command :
		process.sendline(password)
	process.logfile_read  = stdout
	return stdout

@route('/job', method='POST')
def run_job():
	job = str(request.json)
	job = json.loads(job)
	db_playbook = db.db_lookup(job['name'])
	if db_playbook != 'Error':
		ans_command, password = dictmgm.make_play(job, db_playbook)
		if ans_command != 'Error':
			output = run_command(ans_command, password)
			response.status = 202
			response.content_type = 'application/json'
			return json.dumps({'success':output})
		else:
			response.status = 400
			response.content_type = 'application/json'
			return json.dumps({'error':'Data submitted does not match corresponding blueprint in db'})
	else:
		respone.status = 400
		response.content_type = 'application/json'
		return json.dumps({'error':'No playbook by that name in the database'})

if __name__ == '__main__':
	db = db_mgm()
	dictmgm = dict_mgm
	run(host='0.0.0.0', port=80)#might move to config file
=======
#!/usr/bin/env python3
from bottle import route, run, request, response
from src.db import *
from src.dictops import *
import json
import subprocess
from config import *
import logging
logging.basicConfig(level=logging.DEBUG)
def check_auth(sent_auth): #Checks auth token
	if sent_auth == auth:
		return 'OK'
	else: 
		return 'Error'

def run_command(command, password): #runs built command and determines if become password needs to be used
	loggin.debug(command)
	process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	if '-k' in command or '--ask-sudo-pass' in command or '-K' in command or '--ask-password' in command:
		stdout = process.communicate(input=password+'\n')
	else:
		stdout = process.communicate()
	return stdout

@route('/job', method='POST')
def run_job():
	job = request.json
	try:
		if check_auth(job['auth']) == 'Error': #check auth token, if it errs throw a 403 and end
			response.status = 403
			response.content_type = 'application/json'
			return json.dumps({'error':'Authorization incorrect'})	
		logging.debug(job)
		del job['auth'] #remove auth so sent data passes data check
		db_playbook = db.db_lookup(job['name']) #data check
		if db_playbook != 'Error': # if no error continue 
			ans_command, password = dict_mgm.make_play(job, db_playbook) #parse dict into command and return command and password
			if ans_command != 'Error': #if make_play did not fail continue
				output = run_command(ans_command, password) #run command on server and get stdout
				response.status = 202
				response.content_type = 'application/json'
				return json.dumps({'success':output})
			else: #handles datacheck error
				response.status = 400
				response.content_type = 'application/json'
				return json.dumps({'error':'Data submitted does not match corresponding blueprint in db'})
		else:
			respone.status = 400 #playbook not found in the database
			response.content_type = 'application/json'
			return json.dumps({'error':'No playbook by that name in the database'})
	except KeyError: #missing name or auth field
		print('[X] No name or auth contained in request')
		response.status = 400
		response.content_type = 'application/json'
		return json.dumps({'error':' No name or auth contained in request'})
	except FileNotFoundError: #signified file not found/ansible not installed
		print('[X] Ansible not installed')
		response.status = 400
		response.content_type = 'application/json'
		return json.dumps({'error':'Ansible not installed'})
	except IndexError: #empty dict in request
		response.status = 400
		response.content_type = 'application/json'
		print('[X] Empty dict in params section of request')
		return json.dumps({'error':'empty dict in params section of request'})

if __name__ == '__main__':
	db = db_mgm()
	run(host=host, port=port, server=server, workers=workers, ciphers=ciphers)#might move to config file
>>>>>>> e418a0383adecf1cd48651d1f20ee0e8df88f070
