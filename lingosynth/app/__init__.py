"""Flask app for the backend of the project."""

import flask
import authlib
import flask_cors
import flask_limiter

from . import api, views, other
from authlib.integrations.flask_client import OAuth


app = flask.Flask(__name__)
oauth = OAuth(app)

limiter = flask_limiter.Limiter(
    flask_limiter.util.get_remote_address,
    app=app,
    default_limits=['60 per minute', '2 per second'],
    storage_uri='memory://',
    strategy='fixed-window'
)

flask_cors.CORS(app, resources={r'/api/*': {'origins': '*'}})

app.rate_limiter = limiter

api.register(app)
views.register(app)
other.register(app)
