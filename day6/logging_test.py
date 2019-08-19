import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='logger.log',
    filemode="w",
    format="%(asctime)s %(filename)s [%(lineno)d] %(message)s"
)

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')

