from .db import init_db, db_session
from .models import Food
from datetime import datetime

def create_table():
    try:
        init_db()
        return 'success to create table'
    except Exception as err:
        return "Error Log: [{}]".format(err)

def show_data():
    queries = db_session.query(Food)
    entry = [dict(name=q.name, number=q.number, ex_date=q.ex_date) for q in queries]
    return entry

def find_data(name):
    try:
        queries = db_session.query(Food).filter(Food.name == name)
        entry = [dict(name=q.name, number=q.number, ex_date=q.ex_date) for q in queries]
        if len(entry) == 0:
            return True
        return False
    except Exception as err:
        return 'Error Log: [{}]'.format(err)

def find_lated():
    today = datetime.today().strftime("%Y-%m-%d")
    queries = db_session.query(Food).filter(Food.ex_date <= today)
    entry = [dict(name=q.name, number=q.number, ex_date=q.ex_date) for q in queries]
    return entry

def insert_data(name, number, ex_date):    
    try:
        f = Food(name = name, number = number, ex_date = ex_date)
        db_session.add(f)
        db_session.commit()
        return 'add success'
    except Exception as err:
        return 'Error Log: [{}]'.format(err)

def update_data(name, number):
    try:
        db_session.query(Food).filter(Food.name == name).update({Food.number : Food.number + number})
        db_session.commit()
        delete_data("check")
        return 'success'
    except Exception as err:
        return "Error Log : [{}]".format(err)

def delete_data(opt):
    try:        
        if opt == "check":
            db_session.query(Food).filter(Food.number == 0).delete()
        else:
            db_session.query(Food).filter(Food.name == opt).delete()
        db_session.commit()
        return 
    except Exception as err:
        return "Error Log: [{}]".format(err)
    