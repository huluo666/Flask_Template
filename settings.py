import os


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "123456"
    DATABASE_URL = 'sqlite://:memory:'
    # 项目路径
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # 静态文件夹路径
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
    # 文件上传目录
    UPLOAD_DIR = os.path.join(STATIC_DIR, 'upload')

    pass

# 生产环境
class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'
    ENV = "production"
    pass

# 开发环境
class DevelopmentConfig(Config):
    DEBUG = True
    ENV = "development"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/python_template'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True  # 打开调试模式
    pass

# 测试环境
class TestingConfig(Config):
    TESTING = True
    pass


if __name__ == '__main__':
    print(Config.UPLOAD_DIR)
