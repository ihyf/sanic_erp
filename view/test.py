from sanic import Blueprint
from util.tools import mako
from sanic.response import json

bp = Blueprint('test', url_prefix='/')


@bp.route('/')
@mako.template('index.html')
async def index(request):
    return {}
