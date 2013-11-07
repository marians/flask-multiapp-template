
from webapps.one import app
from webapps import util


@app.route('/')
def foo():
    return util.foo()
