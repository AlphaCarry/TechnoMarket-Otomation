from flask import Blueprint

from blueprints.genelbp import genel_bp
from dp import tmarketmodeli, urunmodeli, siparismodeli, urunalismodeli, urunsatismodeli, urunkategorimodeli, \
    urunyorumumodeli, urunozelliklerimodeli

v1_bp = Blueprint('v1_bp', __name__)
v1_bp.register_blueprint(genel_bp(tmarketmodeli, 'eticaret_bp'), url_prefix='/tmarket')
v1_bp.register_blueprint(genel_bp(urunmodeli, 'urunmodeli_bp'), url_prefix='/urun')
v1_bp.register_blueprint(genel_bp(siparismodeli, 'siparismodeli_bp'), url_prefix='/siparis')
v1_bp.register_blueprint(genel_bp(urunalismodeli, 'urunalismodeli_bp'), url_prefix='/alis')
v1_bp.register_blueprint(genel_bp(urunsatismodeli, 'urunsatismodeli'), url_prefix='/satis')
v1_bp.register_blueprint(genel_bp(urunkategorimodeli, 'urunkategorimodeli_bp'), url_prefix='/kategori')
v1_bp.register_blueprint(genel_bp(urunyorumumodeli, 'urunyorumumodeli_bp'), url_prefix='/yorum')
v1_bp.register_blueprint(genel_bp(urunozelliklerimodeli, 'urunozelliklerimodeli_bp'), url_prefix='/özellik')
api_bp = Blueprint('api_bp', __name__)
api_bp.register_blueprint(v1_bp, url_prefix='v1')
