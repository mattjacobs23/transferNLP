from flask import Flask
from .routes import generator

def create_app(config_file='settings.py'):

    # __name__ is global variable, here would be generator.py
    # front end on Flask is using a templating engine, static files (images, videos)
    # need to specify a static path within flask, where our files will live
    app = Flask(__name__, static_url_path="/tmp", static_folder="tmp")

    # configure our app. pass in config_file which has out settings
    app.config.from_pyfile(config_file)

    # register our blueprint
    #routes file will contain routes we will hit, and contains our blueprint
    # gives organization to our entire application
    # call our blueprint generator
    app.register_blueprint(generator)
    return app
