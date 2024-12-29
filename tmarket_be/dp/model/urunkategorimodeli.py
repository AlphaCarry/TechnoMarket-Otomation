from dp.model.temelverisinifi import temelverisinifi
from sqlalchemy.orm import mapped_column , Mapped



class urunkategorimodeli(temelverisinifi):
    __tablename__='kategori'

    kategoriadi: Mapped[str] = mapped_column(nullable=False)