import logging.config
from os import path

log_file = path.join(path.dirname(path.abspath(__file__)), 'logging.ini')
logging.config.fileConfig(log_file)

pytest_plugins = [
    "example.src.fixtures"
]
