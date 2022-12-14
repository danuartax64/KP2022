from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'rama'

    from .views import views
    from .auth import auth
    from .auth2 import auth2
    from .auth3 import auth3



    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth,url_prefix='/')
    app.register_blueprint(auth2,url_prefix='/')
    app.register_blueprint(auth3,url_prefix='/')

    return app