
"""
0.导包
1.创建日志器对象
2.设置日志打印级别
loging.DEBUG 调式级别
loging.INFO 信息级别
loging.WARNING  警告级别
loging.ERRORG  错误级别
loging.CRITICAL  严重错误级别
3.创建处理器对象
创建 输出到控制台
创建 输出到日志文件
4.创建日志信息格式
5.将日志信息格式设置给处理器
设置给控制台处理器
设置给 日志文件处理器
6.给日志器添加处理器
给日志对象 添加 控制台处理器
给日志对象 添加 日志文件处理器
7.打印日志
"""

# 0.导包
import time
import logging
import logging.handlers

# 1.创建日志器对象
logger = logging.getLogger()
# 2.设置日志打印级别
logger.setLevel(logging.DEBUG)
# loging.DEBUG 调式级别
# loging.INFO 信息级别
# loging.WARNING  警告级别
# loging.ERRORG  错误级别
# loging.CRITICAL  严重错误级别

# 3.创建处理器对象
# 创建 输出到控制台
st = logging.StreamHandler()
# 创建 输出到日志文件
fh = logging.handlers.TimedRotatingFileHandler('a.log',when='midnight',interval=1,
                                               backupCount=3,encoding='utf-8')
# when 字符串 指定日志切分时间的单位，midnight：凌晨 12点
# interval 间隔时间的单位的个数，指等待多少个when 后继续进行日志记录
# backupCount 保留日志文件的个数

# 4.创建日志信息格式
fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d] - %(message)s"
formatter = logging.Formatter(fmt)

# 5.将日志信息格式设置给处理器
# 设置给控制台处理器
st.setFormatter(formatter)
# 设置给 日志文件处理器
fh.setFormatter(formatter)

# 6.给日志器添加处理器
# 给日志对象 添加 控制台处理器
logger.addHandler(st)
# 给日志对象 添加 日志文件处理器
logger.addHandler(fh)

# 7.打印日志
while True:
    # logging.debug('我是一个调式级别的日志')
    # loging.INFO 信息级别
    # loging.WARNING  警告级别
    # loging.ERRORG  错误级别
    # loging.CRITICAL  严重错误级别
    logging.warning("警告级别")
    time.sleep(1)
