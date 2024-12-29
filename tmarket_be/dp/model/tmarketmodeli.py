from dp.model.temelverisinifi import temelverisinifi
from sqlalchemy.orm import mapped_column , Mapped



class tmarketmodeli(temelverisinifi):
    __tablename__='tmarket'

    adi: Mapped[str] = mapped_column(nullable=False)
    adres: Mapped[str] = mapped_column(nullable=False)
    telefon: Mapped[str] = mapped_column(nullable=False)

    def to_dict(self):
        pass

