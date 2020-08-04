from sqlalchemy import Column, String, Integer, Date, ForeignKey
from .db import Base

# class USERS_TB(Base):
#     __tablename__ = 'USERS_TB'

#     id = Column(String(30), primary_key=True)

#     def __init__(self, id):
#         self.id = id

#     def __repr__(self):
#         return "USERS_TB(id={})".format(self.id)


class PRODUCT_TB(Base):
    __tablename__ = 'PRODUCT_TB'

    id = Column(String(30), primary_key=True)
    p_name = Column(String(50), primary_key=True)
    p_number = Column(Integer)
    p_ex_date = Column(Date, index=True)
    
    def __init__(self, id, p_name, p_number, p_ex_date):
        self.id = id
        self.p_name = p_name        
        self.p_number = p_number
        self.p_ex_date = p_ex_date

    def __repr__(self):
        return "Food( id={}, p_name={}, p_number={}, p_ex_date={})".format(self.idx, self.id, self.p_name, self.p_number, self.p_ex_date)