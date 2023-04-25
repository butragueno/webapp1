import logging
from logging import handlers
import sys
import os

# 日志初始化函数
def log_initiate():
    FORMAT = '[%(asctime)s]%(levelname)-8s[%(module)s-%(funcName)s] %(message)s'
    DATEFMT = '%Y-%m-%d %H:%M:%S'
    if not os.path.isdir('./log/'):
        os.makedirs('./log/')

    logger = logging.getLogger('logger1')
    logger.setLevel('DEBUG')

    # 所有等级日志输出到all.log，满1MB后分割，最多七次分割
    all_handler = handlers.RotatingFileHandler(
        filename='./log/all.log', maxBytes=1024*1024, backupCount=7)
    all_handler.setLevel('DEBUG')
    all_handler.setFormatter(logging.Formatter(fmt=FORMAT, datefmt=DATEFMT))

    # warning以上日志输出到warning.log，无分割
    warning_handler = logging.FileHandler(filename='./log/warning.log')
    warning_handler.setLevel('WARNING')
    warning_handler.setFormatter(
        logging.Formatter(fmt=FORMAT, datefmt=DATEFMT))

    # 命令行输出info以上日志
    output_handler = logging.StreamHandler(sys.stderr)
    output_handler.setLevel('INFO')
    output_handler.setFormatter(logging.Formatter(fmt=FORMAT, datefmt=DATEFMT))

    logger.addHandler(all_handler)
    logger.addHandler(warning_handler)
    logger.addHandler(output_handler)
    return logger


logger = log_initiate()
