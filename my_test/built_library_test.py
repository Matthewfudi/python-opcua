import sys
'''
sys 模块包含了系统指定的函数功能。一般我想了解些系统相关的信息时会用到这个模块。
'''
print(sys.modules.keys())

print(sys.argv)

# import os
# '''
# os模块封装了常用的文件以及目录操作。
# '''
# os.makedirs("D:\\python学习资料\\qianfeng\\newfile")   #创建了新的文件夹

#这个库也包含了内置函数（builtins.py模块)中函数的和异常 --- 不需要 import 语句就可以在所有Python代码中使用的对象
# abs()

# import json
# json.dump()

from opcua.server.server import Server

ffd = Server(shelffile=fadsf, iserver=dfa)
