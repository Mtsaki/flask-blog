import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_fontawesome import FontAwesome
from flask_login import LoginManager

from werkzeug.utils import import_string

from blog import database
from blog.views import show, auth, post
from blog.models.dao import user

def create_app(configmodule):
    # Webアプリケーション生成
    app = Flask(__name__, instance_relative_config=True)

    Bootstrap(app)
    FontAwesome(app)
    CKEditor(app)
    login_manager = LoginManager(app)

    # config設定
    app.config.from_object(__name__ + '.' + configmodule)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # DB初期化
    database.init_db(app)

    # コールバック
    @login_manager.user_loader
    def load_user(email):
        return user.load_user(email)

    # View設定
    app.register_blueprint(show.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(post.bp)

    return app

    
