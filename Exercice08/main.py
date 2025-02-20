import logging

logging.basicConfig(level=logging.INFO)

def log_decorator(func):
    def wrapper():
        logging.info('Started')
        result = func()
        logging.info('Finished')
        return result
    return wrapper
 
@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")

function_test()
