from plan import Plan
from os import getcwd

WORKING_DIR = getcwd() + '/../'
cron = Plan("lyke_cron")

cron.script('example.py', every='1.minute', path=WORKING_DIR)

if __name__ == '__main__':
	cron.run('update')