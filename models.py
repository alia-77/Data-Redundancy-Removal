from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from database import Base

class Record(Base):

    __tablename__ = "records"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    email = Column(
        String,
        nullable=False
    )

    phone = Column(
        String,
        nullable=False
    )

    address = Column(
        String,
        nullable=False
    )