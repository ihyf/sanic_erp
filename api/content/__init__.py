from sanic import Blueprint
from .admin import admin
from .static import static

content = Blueprint.group(static, admin, url_prefix='/content')
