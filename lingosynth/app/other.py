import os
import flask

from dotenv import load_dotenv

load_dotenv()

def register(app: flask.Flask):
    @app.errorhandler(400)
    @app.errorhandler(403)
    @app.errorhandler(404)
    def error_handler(error):
        return flask.render_template('error.html', error=error), error.code

    @app.context_processor
    def inject_variables():
        return {
        }
