import logging


def setup_logging():
    # Настройка логирования
    logging.basicConfig(
        level=logging.DEBUG, format="[%(levelname)s][%(asctime)s][%(name)s] %(message)s"
    )
    logger = logging.getLogger(__name__)

    # Конфигурация для файла
    file_handler = logging.FileHandler("app.log")
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("[%(levelname)s][%(asctime)s][%(name)s] %(message)s")
    file_handler.setFormatter(formatter)

    # Конфигурация для консоли
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
