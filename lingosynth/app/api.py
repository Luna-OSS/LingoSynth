import time
import flask

def register(app: flask.Flask):
    @app.route('/api/rephrase', methods=['GET', 'POST'])
    @app.rate_limiter.limit('2 per second')
    def api_rephrase():
        text = flask.request.args.get('text') or flask.request.json.get('text')

        time.sleep(3)
        raise

        return flask.jsonify(
            {
                'text': 'Done.'
            }
        )
