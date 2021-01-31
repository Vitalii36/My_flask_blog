from flask import Blueprint

bp = Blueprint('main', __name__, template_folder='templates', url_prefix='/<lang_code>')

from app.main import routes
