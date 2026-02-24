from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base
from backend.app.models.session import DBBaseModel


class Valentine(DBBaseModel):
    __tablename__ = "valentine"
    __table_args__ = {'extend_existing': True}  # Добавьте это


    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(1000), nullable=False)
    recipient_email = Column(String(321), nullable=False)
    author_email = Column(String(321), nullable=False)
    dispatch_date = Column(DateTime, nullable=False)
    is_public = Column(Boolean, nullable=False, default=False) 