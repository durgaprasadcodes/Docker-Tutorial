from sqlalchemy import Column,String,Integer
from database import Base

class User(Base):
    __tablename__ = "dockerdb"
    id = Column(Integer,autoincrement=True,primary_key=True)
    name = Column(String(150),nullable=False)
    email = Column(String(200),unique=True,nullable=False)