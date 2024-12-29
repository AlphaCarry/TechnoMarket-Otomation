from dp.model.temelverisinifi import temelverisinifi
from sqlalchemy.orm import mapped_column, Mapped, relationship


class urunmodeli(temelverisinifi):
    __tablename__='urun'

    urun_kodu: Mapped[str] = mapped_column(nullable=False,unique=True)
    urun_adi: Mapped[str] = mapped_column(nullable=False)
    fiyat:  Mapped[float]=mapped_column()
    acıklama: Mapped[str]=mapped_column(nullable=False)


alislar: Mapped[list['urunalismodeli']]=relationship()
satislar:Mapped[list['urunsatismodeli']]=relationship()
@property
def stokmiktar(self):
    return sum ([alis.miktar for alis in self.alislar])-sum([satis.miktar for satis in self.satislar])
