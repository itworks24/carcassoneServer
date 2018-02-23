from eve import Eve
from flask import abort
app = Eve()

@app.route('/auth/', )
def hello_world():
    return 'Hello World!'

def pre_gameTiles_post_callback(request):
    abort(403)

@app.errorhandler(403)
def payme(e):
    return 'Pay me!', 403

#app.on_pre_POST_gameTiles += pre_gameTiles_post_callback

if __name__ == '__main__':
    app.run()