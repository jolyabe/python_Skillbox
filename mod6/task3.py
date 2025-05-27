# -------------------------------------
# Задача 3. JSON-логирование

import json
import logging

class JsonAdapter(logging.LoggerAdapter):

    def process(self, msg, kwargs):

        new_message = json.dumps(msg, ensure_ascii=False)
        return new_message, kwargs

if __name__ == '__main__':
    logger = JsonAdapter(logging.getLogger(__name__))
    logging.basicConfig(level=logging.DEBUG,
                        filename='skillbox_json_messages_task3.log',
                        format= '{"time": "%(asctime)s", "level": "%(levelname)s", "message": %(message)s}',
                        datefmt='%H:%M:%S')

    logger.info('Сообщение')
    logger.error('Кавычка)"')
    logger.debug("Еще одно сообщение")
