from sqlalchemy import Column, String, Integer, Date
from .db import Base


class Food(Base):
    __tablename__ = 'Food'

    name = Column(String, primary_key=True)
    number = Column(Integer)
    ex_date = Column(Date, index=True)
    
    def __init__(self, name, number, ex_date):
        self.name = name        
        self.number = number
        self.ex_date = ex_date

    def __repr__(self):
        return "Food(name={}, number={}, ex_date={})".format(self.name, self.number, self.ex_date)