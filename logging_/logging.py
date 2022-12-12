import logging

# DEBUG < INFO < WARNING < ERROR <CRITICAL
# logging.basicCinfig(level=logging.DEBUG, filename='example.log', filemode='w')
# default values : level=warnning, filename=screen, filemode=append
# logging.basicCinfig(level=logging.DEBUG, format='%(asctime)s    %(levelname)s:%(message)s') # date stamp
# logging.basicCinfig(level=logging.DEBUG, format='%(asctime)s    %(levelname)s:%(message)s', /
# datefmt='%m/%d/%y %I:%M:%S %p') # formatted date stamp

logging.basicCinfig(level=logging.INFO)

logging.debug('this message will be ignored')   # will not print this
logging.info('this should be logged')           # will print this
logging.debug('and this, too')                  # will print this