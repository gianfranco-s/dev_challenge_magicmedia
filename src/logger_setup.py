import logging
import time

from logging import Logger
from typing import Callable


def create_execution_time_logger() -> Logger:
    logger = logging.getLogger('execution_time_logger')
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler('execution_times.log')
    file_handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s'))

    logger.addHandler(file_handler)
    return logger


execution_time_logger = create_execution_time_logger()


def log_execution_time(func: Callable) -> Callable:
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time_logger.info(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper
