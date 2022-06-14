from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__) #전역변수 사용하지 않도록 수정
    app.config.from_object(config) #환경설정을  config 파일에서 가져와 set

    #ORM
    db.init_app(app)
    migrate.init_app(app,db)
    from . import models


    #blueprint
    from .views import main_views, question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)


    #필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] =format_datetime

    return app

'''
    뷰 추가하기 전
    @app.route('/')
    def hello_pybo():
        return 'Hello, Pybo!'
    return app
'''