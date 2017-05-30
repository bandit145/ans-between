#!venv/bin/python3
from bottle import route, run, request, response
from src import db, dict_mgm, logging
import json
import subprocess
from config import *
import pexpect
from cel.tasks import run_command
import atexit
def purge_db():
	db.db_exit()

def response_build(status, returndata):
	response.status = status
	response.content_type = 'application/json'
	return json.dumps(returndata)

def check_auth(sent_auth): #Checks auth token
	if sent_auth == auth:
		return 'OK'
	else: 
		return 'Error'

@route('/job', method='POST')
def run_job():
	job = request.json
	try:
		if check_auth(request.headers.get('Authorization')) == 'Error': #check auth token, if it errs throw a 403 and end
			return response_build(403,{'error':'Authorization incorrect'})
		logging.debug(job)
		logging.debug('passed auth')
		db_playbook = db.db_lookup(job['name']) #data check
		logging.debug('passed name lookup')
		if db_playbook != 'Error': # if no error continue 
			ans_command, password = dict_mgm.make_play(job, db_playbook, location) #parse dict into command and return command and password
			if ans_command != 'Error': #if make_play did not fail continue
				items = db.db_outputid()
				db.db_stdoutinput('No current stdout')
				task = run_command.delay(ans_command, password, items)
				return response_build(202,{'taskid':items})
			else: #handles datacheck error
				logging.info('[X] Data submitted does not match corresponding blueprint in db')
				return response_build(400,{'error':'Data submitted does not match corresponding blueprint in db'})
		else:
			logging.info('[X] No playbook by that name in the database')
			return response_build(400,{'error':'No playbook by that name in the database'})
	except KeyError: #missing name or auth field
		logging.info('[X] No name or auth contained in request')
		return response_build(400,{'error':' No name or auth contained in request'})
	except IndexError: #empty dict in request
		logging.info('[X] Empty dict in params section of request')
		return response_build(400,{'error':'empty dict in params section of request'})

@route('/tasks/:taskid', method='GET')
def return_id(taskid):
	output = db.db_completed(taskid)
	logging.debug(output)
	if output == None:
		logging.debug('[X] Processing')
		return response_build(202,{'info':'processing has not finished'})
	else:
		return response_build(200,{'output':output})



atexit.register(purge_db)
if __name__ == '__main__':
	db.start_db(schemaloc)
	run(host=host, port=port,server=server, workers=1)#might move to config file