from sanic.response import json
from sanic import Blueprint

admin = Blueprint('api_admin', url_prefix='/admin')


@admin.route('/')
async def bp_root(request):
    b = admin
    a = request
    return json({'my': 'admin'})
