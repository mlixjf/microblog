import os

"""
os.environ是环境变量字典
os.getenv是一个函数
注：使用flask-wtf需要首先配置SECRET_KEY属性, CSRF需要密钥
"""


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
