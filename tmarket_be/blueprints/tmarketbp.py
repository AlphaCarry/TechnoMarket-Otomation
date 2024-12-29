from flask import Blueprint, request
from sqlalchemy import select
from dp import tmarketmodeli, db

tmarketbp = Blueprint('tmarketbp', __name__)


@tmarketbp.route('/', methods=['GET'])
@tmarketbp.route('', methods=['GET'])
def index():
    sorgu = select(tmarketmodeli)
    cevap = db.session.scalars(sorgu).all()

    return [tmarket.to_dict() for tmarket in cevap]


@tmarketbp.route('/', methods=['POST'])
@tmarketbp.route('', methods=['POST'])
def ekle():
    tmarket = tmarketmodeli()

    tmarket.adi = request.json('adi')
    tmarket.adres = request.json('adres')
    tmarket.telefon = request.json('telefon')
    db.session.add(tmarket)
    db.session.commit()
    return tmarket.to_dict()


@tmarketbp.route('/<int:,id>', methods=['GET'])
def getir(id: int):
    sorgu = select(tmarketmodeli).where(tmarketmodeli.id == id)
    cevap = db.session.scalars(sorgu).one()
    return cevap.to_dict()


@tmarketbp.route('/<int:id>', methods=['PUT', 'PATCH'])
def duzenle(id: int):
    sorgu = select(tmarketmodeli).where(tmarketmodeli.id == id)
    tmarket = tmarketmodeli()

    tmarket.adi = request.json('adi')
    tmarket.adres = request.json('adres')
    tmarket.telefon = request.json('telefon')
    db.session.commit()
    return tmarket.to_dict()


@tmarketbp.route('/<int:id>', methods=['DELETE'])
def sil(id: int):
    sorgu = select(tmarketmodeli).where(tmarketmodeli.id == id)
    tmarket = db.session.scalars(sorgu).one()

    db.session.delete(tmarket)
    db.session.commit()
    return {'silinen': tmarket.to_dict()}
