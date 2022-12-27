from flask import Flask

def create_app():
    global app
    app = Flask(__name__)
    app.secret_key= 'SK2020'
    from .auth import akses
    # from .routeb import router
    from .playvid import playvid
    app.register_blueprint(akses, url_prefix='/')
    # app.register_blueprint(router, url_prefix='/')
    app.register_blueprint(playvid, url_prefix='/')
    from .database_cctv import database
    app.register_blueprint(database, url_prefix='/')
    from .list_user import db_user
    app.register_blueprint(db_user, url_prefix='/')
    return app