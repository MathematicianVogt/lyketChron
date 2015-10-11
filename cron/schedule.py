from plan import Plan
from os import getcwd

WORKING_DIR = getcwd() + '/../'
cron = Plan("lyket_ingestion_cron")

cron.script('LyketJob.py', every='1.minute', path=WORKING_DIR)

if __name__ == '__main__':
	cron.run('update')
