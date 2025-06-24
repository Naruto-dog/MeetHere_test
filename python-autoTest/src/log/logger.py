import logging

class LogGet:

    @staticmethod
    def log_get():
        formatter = ('%(asctime)s - %(levelname)s - %(name)s - %(filename)s - %(funcName)s: '
                     '- %(lineno)d - %(message)s')
        file_path = 'E:/testpro/MeetHere/python-autoTest/src/log/MeetHere_test.log'
        logger = logging.getLogger('test_logger')
        logger.setLevel(logging.INFO)
        # 避免重复添加handler
        if not logger.handlers:
            # 创建文件handler
            file_handler = logging.FileHandler(file_path, encoding='utf-8')
            file_handler.setFormatter(logging.Formatter(formatter))
            logger.addHandler(file_handler)
        return logger


