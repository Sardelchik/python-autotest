import logging

def setup_logging():
    logging.basicConfig(filename='request.log', level=logging.INFO,
                        format='[%(asctime)s] %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S,%f')