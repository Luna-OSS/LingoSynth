"""Production runner."""

import waitress

from lingosynth.app import app

if __name__ == '__main__':
    waitress.serve(
        app,
        host='0.0.0.0',
        port=5001,
        threads=4,
        asyncore_use_poll=True,
        asyncore_loop_timeout=1,
)
