import asyncio
from sanic import Sanic
from sanic.response import json
from sanic.log import logger
from sanic.response import text
import config
from api import api
from view.test import bp
from util.dbmanager import init_db


app = Sanic('erp')
app.blueprint(api)
app.blueprint(bp)
app.static('/static', './static')


# @app.route('/')
# async def test(request):
#     logger.info('Here is your log')
#     print(config.DEBUG)
#     return text('Hello World!')
#
#
# @app.middleware('request')
# async def print_on_request(request):
#     print("I print when a request is received by the server")
    
    
# @app.middleware('response')
# async def halt_response(request, response):
#     return text('I halted the response')


@app.listener('before_server_start')
async def setup_db(app, loop):
    await init_db()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=config.DEBUG, access_log=config.ACCESS_LOG)

