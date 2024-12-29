from flask import Blueprint, request, abort
from sqlalchemy import select, inspect

from blueprints.verisorgulama import sorgula
from dp import db


def genel_bp(dp_sinifi: type, bp_adi: str = 'genel_bp'):
    bp = Blueprint(bp_adi, __name__)

    @bp.route('/', methods=['GET'])
    @bp.route('', methods=['GET'])
    @bp.route('/sayfa/<int:sayfa>', methods=['GET'])
    @bp.route('/sayfa/<int:sayfa>/<int:kayit_sayisi>', methods=['GET'])
    def index(sayfa: int = 1, kayit_sayisi: int = 10):
        sorgu = select(dp_sinifi)

        sorgu = sorgula(sorgu, dp_sinifi, sayfa - 1, kayit_sayisi)
        cevap = db.session.scalars(sorgu).all()
        return [dp.to_dict() for dp in cevap]

    @bp.route('/', methods=['POST'])
    @bp.route('', methods=['POST'])
    def ekle():
        dp = dp_sinifi()
        sutunlar = [col.key for col in inspect(dp_sinifi).mapper.column_attrs]
        for sutun in request.json:
            if sutun in sutunlar:
                setattr(dp, sutun, request.json[sutun])
            else:
                return abort(400)

        db.session.add(dp)
        db.session.commit()
        return dp.to_dict()

    @bp.route('/<int:id>', methods=['GET'])
    def getir(id: int):
        sorgu = select(dp_sinifi).where(dp_sinifi.id == id)
        cevap = db.session.scalars(sorgu).one()
        return cevap.to_dict()

    @bp.route('/<int:id>', methods=['PUT', 'PATCH'])
    def duzenle(id: int):
        sorgu = select(dp_sinifi).where(dp_sinifi.id == id)
        dp = dp_sinifi()

        sutunlar = [col.key for col in inspect(dp_sinifi).mapper.column_attrs]
        for sutun in request.json:
            if sutun in sutunlar:
                setattr(dp, sutun, request.json[sutun])
            else:
                return abort(400)
        db.session.commit()
        return dp.to_dict()

    @bp.route('/<int:id>', methods=['DELETE'])
    def sil(id: int):
        sorgu = select(dp_sinifi).where(dp_sinifi.id == id)
        dp = db.session.scalars(sorgu).one()

        db.session.delete(dp)
        db.session.commit()
        return {'silinen': dp.to_dict()}

    return bp
