import logging

# After debugging, the level could be set at logging.ERROR
logging.basicConfig(level=logging.DEBUG, format=\
	' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to logged.')
logging.error('An error has occurred.')
logging.critical('The progeam is unable to recover!')
