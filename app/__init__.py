from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import main
    from .health import health

    app.register_blueprint(main)
    app.register_blueprint(health)

    return app
