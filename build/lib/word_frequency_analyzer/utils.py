import logging
import time

logger_utils = logging.getLogger(__name__)


def setup_logging():
    logging.basicConfig(filename='app.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG,
                        datefmt='%Y-%m-%d %H:%M:%S')


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start_time
        logger_utils.info(f"Application has worked for {execution_time:.10f} seconds.")
        return result

    return wrapper
