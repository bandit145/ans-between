from __future__ import absolute_import, unicode_literals
from cel.cel import task
from src import db, logging
import pexpect
#*args is testing hook
@task.task
def run_command(command, password, taskid, *args): #runs built command and determines if become password needs to be used
	#rules = ['-k' in command,
	#		'--ask-sudo-pass' in command,
	#		'-K' in command,
	#		'--ask-pass' in command]
	logging.debug(command)
	logging.debug(password)
	#if any(rules):
	#try except fall through
	try:
		process = pexpect.spawnu(command, timeout=None)
		logging.debug('enter password')
		process.expect('password')
		process.sendline(password)
		pexpect_readout(password, taskid)
	except pexpect.exceptions.EOF:
		process = pexpect.spawnu(command, timeout=None)
		pexpect_readout(process, taskid)


def pexpect_readout(process, taskid):
	stdout = process.read()
	logging.debug(stdout+ 'stdout')
	db.db_updateinput(stdout, taskid)