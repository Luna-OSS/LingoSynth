import flask

def register(app: flask.Flask):
    @app.route('/')
    def index():
        return flask.render_template('index.html')
