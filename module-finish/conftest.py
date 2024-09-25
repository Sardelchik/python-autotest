import logging
from logging.handlers import RotatingFileHandler

# Настройка формата логирования
log_format = "[%(asctime)s] %(levelname)s - %(message)s"
logging.basicConfig(
   level=logging.DEBUG,
   format='[%(levelname)s][%(asctime)s][%(name)s] %(message)s',
   datefmt='%Y-%m-%d %H:%M:%S'
)

# Создание обработчика для записи логов в файл с ротацией
handler = RotatingFileHandler('request.log', maxBytes=5000000, backupCount=5)
handler.setFormatter(logging.Formatter(log_format))

# Получение экземпляра логгера и добавление обработчика
logger = logging.getLogger(__name__)
logger.addHandler(handler)

# Пример записи в лог
logger.info('request: Request was sended')


pytest_plugins=[
   "src.tests.browser"
]