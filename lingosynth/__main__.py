import app

app.app.run(
    host='0.0.0.0',
    port=5001,
    debug=True,
    use_evalex=False,
    threaded=True,
)
