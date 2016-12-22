from __future__ import absolute_import, unicode_literals
from cel.cel import task
from src import db
import pexpect
import logging
#*args is testing hook
logging.basicConfig(level=logging.INFO)
@task.task
def run_command(command, password, taskid, *args): #runs built command and determines if become password needs to be used
	rules = ['-k' in command,
			'--ask-sudo-pass' in command,
			'-K' in command,
			'--ask-pass' in command]
	logging.debug(command)
	logging.debug(password)
	process = pexpect.spawnu(command, timeout=None)
	if any(rules):
		logging.debug('enter password')
		process.expect('password')
		process.sendline(password)
	stdout = process.read()
	logging.debug(stdout)
	db.db_updateinput(stdout, taskid)