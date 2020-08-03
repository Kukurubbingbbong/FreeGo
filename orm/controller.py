from .db import init_db, db_session
from .models import Food
from datetime import datetime

def create_table():
    try:
        init_db()
        return 'success'
    except Exception as err:
        print("Error Log: [{}]".format(err))
        return 'fail'

def show_data():
    try:
        queries = db_session.query(Food)
        entry = [dict(name=q.name, number=q.number, ex_date=q.ex_date) for q in queries]
        return entry
    except Exception as err:
        print('Error Log: [{}]'.format(err))
        return 'fail'

def find_data(name):
    try:
        queries = db_session.query(Food).filter(Food.name == name)
        entry = [dict(name=q.name, number=q.number, ex_date=q.ex_date) for q in queries]
        if len(entry) == 0:
            return False
        return True
    except Exception as err:
        print('Error Log: [{}]'.format(err))
        return 'fail'

def find_lated():
    try:
        today = datetime.today().strftime("%Y-%m-%d")
        queries = db_session.query(Food).filter(Food.ex_date <= today)
        entry = [dict(name=q.name, number=q.number, ex_date=q.ex_date) for q in queries]
        return entry
    except Exception as err:
        print('Error Log: [{}]'.format(err))
        return 'fail'   

def insert_data(name, number, ex_date):    
    try:
        f = Food(name = name, number = number, ex_date = ex_date)
        db_session.add(f)
        db_session.commit()
        return 'success'
    except Exception as err:
        print('Error Log: [{}]'.format(err))
        return 'fail'

def update_data(name, number):
    try:
        db_session.query(Food).filter(Food.name == name).update({Food.number : Food.number + number})
        db_session.commit()
        delete_data("check")
        return 'success'
    except Exception as err:
        print("Error Log : [{}]".format(err))
        return 'fail'

def delete_data(opt):
    try:        
        if opt == "check":
            db_session.query(Food).filter(Food.number == 0).delete()
        else:
            db_session.query(Food).filter(Food.name == opt).delete()
        db_session.commit()
        return 'success'
    except Exception as err:
        print("Error Log : [{}]".format(err))
        return 'fail'
    