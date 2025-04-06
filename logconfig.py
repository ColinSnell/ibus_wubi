import logging
import logging.config

_init = False

# 定义日志系统的配置字典，用于 logging.config.dictConfig() 高级配置
dict_config = {
    'version': 1,  # 指定日志配置的版本，必须为 1
    'formatters': {  # 格式化器（决定日志输出的格式）
        'simple': {  # 名为 simple 的格式器
            'format': '%(asctime)s - %(filename)s:%(lineno)3s %(funcName)20s - %(levelname)s - %(message)s'
            # 输出格式说明：
            # %(asctime)s      : 日志时间
            # %(filename)s     : 文件名
            # %(lineno)3s      : 行号，占3位
            # %(funcName)20s   : 函数名，占20位（右对齐）
            # %(levelname)s    : 日志级别
            # %(message)s      : 日志信息内容
        }
    },
    'handlers': {  # 处理器（决定日志输出到哪里：控制台、文件等）
        'console': {  # 控制台输出处理器
            'class': 'logging.StreamHandler',  # 使用标准输出流处理器
            'level': 'DEBUG',  # 设置日志级别为 DEBUG（及以上级别会被处理）
            'formatter': 'simple',  # 使用名为 simple 的格式器
            'stream': 'ext://sys.stdout'  # 输出到标准输出（即终端）
        },
        'file': {  # 文件输出处理器
            'class': 'logging.handlers.RotatingFileHandler',  # 使用可轮转的文件处理器
            'level': 'DEBUG',  # 设置日志级别为 DEBUG
            'formatter': 'simple',  # 使用名为 simple 的格式器
            'filename': '/tmp/iwubi.log',  # 日志输出文件路径
            'maxBytes': 1048576,  # 单个日志文件最大为 1MB（超出后轮转）
            'backupCount': 3  # 最多保留 3 个历史文件（会生成 iwubi.log.1、.2、.3）
        }
    },
    'root': {  # 根 Logger 配置（默认 logger）
        'level': 'DEBUG',  # 日志最低级别为 DEBUG
        'handlers': ['console', 'file']  # 同时使用 console 和 file 两个 handler 输出日志
    }
}



def get_logger():
    global _init
    if not _init:
        # with open(os.path.join(os.path.dirname(__file__), 'logconfig.yaml'), 'r') as f:
        #     config = yaml.safe_load(f.read())
        #     logging.config.dictConfig(config)
        logging.config.dictConfig(dict_config)
        _init = True
    return logging.getLogger()
