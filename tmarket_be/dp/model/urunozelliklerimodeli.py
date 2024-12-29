from dp.model.temelverisinifi import temelverisinifi
from sqlalchemy.orm import mapped_column , Mapped



class urunozelliklerimodeli(temelverisinifi):
    __tablename__='urunozellikleri'

    urun: Mapped[str] = mapped_column(nullable=False,unique=True)
    deger: Mapped[str] = mapped_column(nullable=False)
    ozellik:  Mapped[float]=mapped_column(nullable=False)