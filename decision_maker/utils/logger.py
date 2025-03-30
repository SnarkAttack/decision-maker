import logging

logger = logging.get_logger('decision_maker')
formatter = logging.Formatter('%(levelname)s - %(name)s: %(message)s')

ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)