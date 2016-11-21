#celery seems to actually run as a seperate application
#but that still does not make sense to me as it would need to integrate with the app
#I really dont understand how this works
#
#
from __future__ import absolute_import, unicode_literals
from celery import Celery

task = Celery('cel',broker='amqp://guest@localhost//',
			backend='amqp://guest@localhost//',
			include=['cel.tasks'],
			loglevel='DEBUG')

if __name__ == '__main__':
	task.start()