from dp.model.temelverisinifi import temelverisinifi
from sqlalchemy.orm import mapped_column , Mapped



class urunyorumumodeli(temelverisinifi):
    __tablename__='urunyorumu'

    siparis: Mapped[str] = mapped_column(nullable=False,unique=True)
    urun: Mapped[str] = mapped_column(nullable=False)
    yorum:  Mapped[float]=mapped_column(nullable=False)
    puan: Mapped[str]=mapped_column(nullable=False)