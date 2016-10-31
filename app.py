#!/usr/bin/env python3
from bottle import route, run, request, response
from src.db import *
from src.dictops import *
import json
import subprocess

def run_command(command, password):
	process = subprocess.Popen(command, stdin=PIPE, stdout=PIPE)
	if '-k' in command or '--ask-sudo-pass':
		stdout = process.communicate(input=password+'\n')
	else:
		stdout = process.communicate()
	return stdout

@route('/job', method='POST')
def run_job():
	job = request.json
	job = json.load(job)
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
	run(host=0.0.0.0, port=80)#might move to config file