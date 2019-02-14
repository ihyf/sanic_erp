from sanic.response import json
from sanic import Blueprint

static = Blueprint('api_static', url_prefix='/static')


@static.route('/')
async def bp_root(request):
    b = static
    a = request
    return json({'static': 'static'})
