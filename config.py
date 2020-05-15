class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////mnt/hdd1/workspace/www/blog/blog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    CKEDITOR_PKG_TYPE = 'basic'
    UPLOAD_FOLDER = './uploads'


class ProductionConfig(Config):
    ENV = 'production'
    # SECRET_KEY セキュリティの観点からSECRET_KEYは起動時に設定すること


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    SECRET_KEY = 'dev'