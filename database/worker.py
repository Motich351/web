from sqlalchemy import Column,Integer,Text, CHAR,ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base


class Worker(Base):
    __tablename__ = 'worker'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    fullname = Column(CHAR)
    jobrank = Column(CHAR)
    salary = Column(Integer, nullable=False)
    phone = Column(Integer, nullable=False)
    passport = Column(Integer, nullable=False)
    shop_id = Column(ForeignKey('shop.id'), nullable=True)

    shop = relationship('Shop')


    def __str__(self):
        return f"Работник {self.id}: {self.fullname}; профессия: {self.jobrank}; {self.phone}; {self.point}"

    def __repr__(self):
        return str(self)