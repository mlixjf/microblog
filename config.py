import os
from pathlib import Path

"""
os.environ是环境变量字典
os.getenv是一个函数
注：使用flask-wtf需要首先配置SECRET_KEY属性, CSRF需要密钥
"""

basedir = Path(__file__).parent


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = (os.environ.get("DATABASE_URL") or
                               "sqlite:///" + os.path.join(basedir, 'app.db') +
                               "?" +
                               "check_same_thread=False")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True


if __name__ == '__main__':
    print(Config.SQLALCHEMY_DATABASE_URI)
