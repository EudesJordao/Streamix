from sqlalchemy import Column, Integer, String
from database import Base

class Usuario(Base):
    __tablename__ = "contas"

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String)
    email = Column(String, unique=True, index=True)
    user = Column(String)
    password_hash = Column(String)