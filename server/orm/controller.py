from .db import init_db, db_session
from .models import PRODUCT_TB
from datetime import datetime

def create_table():
    try:
        init_db()
        return 'success'
    except Exception as err:
        print("Error Log: [{}]".format(err))
        return 'fail'

# def register_user(id):
#     try:
#         table = USERS_TB(id = id)
#         db_session.add(table)
#         db_session.commit()
#         return 'success'
#     except Exception as err:
#         print("Error Log: [{}]".format(err))
#         return 'fail'

def show_data(id):
    try:
        queries = db_session.query(PRODUCT_TB).filter(PRODUCT_TB.id == id)
        entry = [dict(id = q.id, p_name=q.p_name, number=q.p_number, ex_date=q.p_ex_date) for q in queries]
        return entry
    except Exception as err:
        print('Error Log: [{}]'.format(err))
        return 'fail'

def find_data(id, p_name):
    try:
        queries = db_session.query(PRODUCT_TB).filter(PRODUCT_TB.id == id).filter(PRODUCT_TB.p_name == p_name)
        entry = [dict(id=q.id, p_name=q.p_name, p_number=q.p_number, p_ex_date=q.p_ex_date) for q in queries]
        if len(entry) == 0:
            return False
        return True
    except Exception as err:
        print('Error Log: [{}]'.format(err))
        return 'fail'

def find_lated(id):
    try:
        today = datetime.today().strftime("%Y-%m-%d")
        queries = db_session.query(PRODUCT_TB).filter(PRODUCT_TB.id == id).filter(PRODUCT_TB.p_ex_date <= today)
        entry = [dict(id=q.id, p_name=q.p_name, p_number=q.p_number, p_ex_date=q.p_ex_date) for q in queries]
        return entry
    except Exception as err:
        print('Error Log: [{}]'.format(err))
        return 'fail'   

def insert_data(id, p_name, p_number, p_ex_date):    
    try:
        f = PRODUCT_TB(id = id, p_name = p_name, p_number = p_number, p_ex_date = p_ex_date)
        db_session.add(f)
        db_session.commit()
        return 'success'
    except Exception as err:
        print('Error Log: [{}]'.format(err))
        return 'fail'

def update_data(id, p_name, p_number):
    try:
        db_session.query(PRODUCT_TB).filter(PRODUCT_TB.id == id).filter(PRODUCT_TB.p_name == p_name).update({PRODUCT_TB.p_number : p_number})
        db_session.commit()
        delete_data(id, "check")
        return 'success'
    except Exception as err:
        print("Error Log : [{}]".format(err))
        return 'fail'

def delete_data(id, opt):
    try:        
        if opt == "check":
            db_session.query(PRODUCT_TB).filter(PRODUCT_TB.p_number == 0).delete()
        else:
            update_data(id, opt, 0)            
        db_session.commit()
        return 'success'
    except Exception as err:
        print("Error Log : [{}]".format(err))
        return 'fail'
    