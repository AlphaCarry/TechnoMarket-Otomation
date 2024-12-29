from dp.model.temelverisinifi import temelverisinifi
from sqlalchemy.orm import mapped_column , Mapped
from datetime import date
from sqlalchemy import ForeignKey

class urunsatismodeli(temelverisinifi):
    __tablename__='satis_hareketleri'

    tarih: Mapped[date] = mapped_column(default=date.today())
    urun_id: Mapped[int] = mapped_column(ForeignKey('urun.id'))
    adet: Mapped[float] = mapped_column(nullable=False)
    birimfiyati: Mapped[float] = mapped_column(nullable=False)