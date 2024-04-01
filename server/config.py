from loguru import logger

SECRET_KEY = 'Секретный сука ключ'
ALGORITHM = 'HS256'
logger.add('logs.log', encoding="utf-8")
