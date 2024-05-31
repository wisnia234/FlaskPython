import logging

def log(flaskApp):

    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s %(name)s: %(message)s')
    
    levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    for level in levels:
        flaskApp.logger.info(f'Log level: {level}')

    flaskApp.logger.info('Registered endpoints:')
    for rule in flaskApp.url_map.iter_rules():
        flaskApp.logger.info(f'{rule.endpoint}: {rule.rule}')