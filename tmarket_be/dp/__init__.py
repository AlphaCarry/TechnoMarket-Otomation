from flask_sqlalchemy import SQLAlchemy
from .model import *
from dp.model.temelverisinifi import temelverisinifi



db=SQLAlchemy(model_class=temelverisinifi)


def tmarketmodeli():
    return None