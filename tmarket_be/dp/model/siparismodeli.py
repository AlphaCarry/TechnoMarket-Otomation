from dp.model.temelverisinifi import temelverisinifi
from sqlalchemy.orm import mapped_column , Mapped



class siparismodeli(temelverisinifi):
    __tablename__='siparis'

    tarih: Mapped[str] = mapped_column(nullable=False)
    firma: Mapped[str] = mapped_column(nullable=False)
    musteri: Mapped[str] = mapped_column(nullable=False)