from os.path import dirname, abspath
print(abspath(__file__))            # 获取当前执行文件的绝对路径
print(dirname(abspath(__file__)))