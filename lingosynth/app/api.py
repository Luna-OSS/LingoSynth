import flask
import time

from . import ai, prompts

def register(app: flask.Flask):
    @app.route('/api/rephrase', methods=['GET', 'POST'])
    @app.rate_limiter.limit('2 per second')
    def api_rephrase():
        text = flask.request.args.get('text') or flask.request.json.get('text')

        messages = prompts.MESSAGES
        messages.append({
            'role': 'user',
            'content': text
        })


        try:
            generated = ai.generate(messages)
        except Exception:
            return flask.Response('Sorry, an error has occurred!', status=500)

        return flask.jsonify(
            {
                'text': generated
            }
        )
