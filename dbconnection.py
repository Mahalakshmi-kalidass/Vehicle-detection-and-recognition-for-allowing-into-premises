import mysql.connector
from mysql.connector import Error

def write_to_db(sql,val):
	try:
		connection = mysql.connector.connect(host='localhost',database='project',user='balaji',password='password')
		if connection.is_connected():
			db_Info = connection.get_server_info()
			print("Connected to MySQL Server version ",db_Info)
			cursor = connection.cursor()
			'''cursor.execute(sql)
			result = cursor.fetchall()
			print(result)'''
			cursor.execute(sql,val)
			connection.commit()
			print(cursor.rowcount, "record inserted.")
			#record = cursor.fetchone()
			'''for x in result:
  				print(x)'''
        		
	except Error as e:
    		print("Error while connecting to MySQL", e)
	finally:
    		if connection.is_connected():
        		cursor.close()
        		connection.close()
        		print("MySQL connection is closed")
def select_from_db(sql,val):
	
	try:
		connection = mysql.connector.connect(host='localhost',database='project',user='balaji',password='password')
		if connection.is_connected():
			db_Info = connection.get_server_info()
			print("Connected to MySQL Server version ",db_Info)
			cursor = connection.cursor()
			cursor.execute(sql,(val,))
			result = cursor.fetchall()
			print(result)
      		
	except Error as e:
    		print("Error while connecting to MySQL", e)
	finally:
    		if connection.is_connected():
        		cursor.close()
        		connection.close()
        		print("MySQL connection is closed")
	

#sql='select * from VEHICLE_DETAILS'
#write_to_db(sql)
