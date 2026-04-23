from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base


class Launch(Base):
    __tablename__ = "launches"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    date_utc = Column(String, nullable=False)
    success = Column(Boolean, nullable=True)