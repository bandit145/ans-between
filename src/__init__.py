#for importing all src files
import logging
from src.db import *
from src.dictops import *
from config import dbdir
try:
	logging.basicConfig(level=logging.INFO, 
		filename='/var/log/ans-between/ans-between.log', 
		filemode='a',
		datefmt='%Y-%m-%d %H:%M:%S',
		format='%(asctime)s %(levelname)s:%(message)s')

except FileNotFoundError:
	print('[X]/var/log/ans-between not found')
	logging.basicConfig(level=logging.INFO, 
		filename='ans-between.log', 
		filemode='a',
		datefmt='%Y-%m-%d %H:%M:%S',
		format='%(asctime)s %(levelname)s:%(message)s')

db = db_mgm(dbdir)