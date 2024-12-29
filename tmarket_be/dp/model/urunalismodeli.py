
from sqlalchemy.orm import Mapped,mapped_column
from datetime import date
from sqlalchemy import ForeignKey
from dp.model.temelverisinifi import temelverisinifi
class urunalismodeli(temelverisinifi):
    __tablename__='alis_hareketleri'

    tarih: Mapped[date] = mapped_column(default=date.today())
    urun_id: Mapped[int] = mapped_column(ForeignKey('urun.id'))
    adet: Mapped[float] = mapped_column(nullable=False)
    birimfiyati: Mapped[float] = mapped_column(nullable=False)