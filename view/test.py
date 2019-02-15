from sanic import Blueprint
from sanic.response import json

bp = Blueprint('test', url_prefix='/')


@bp.route('/')
async def bp_root(request):
    b = bp
    a = request
    return json({'my': 'test'})
