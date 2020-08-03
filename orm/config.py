db = {
    'user'     : 'root',		# 1)
    'password' : 'woung',		# 2)
    'host'     : 'localhost',	# 3)
    'port'     : 3306,			# 4)
    'database' : 'freego'		# 5)
}

DB_URL = "mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8".format(db['user'], db['password'], db['host'],db['port'],db['database'])