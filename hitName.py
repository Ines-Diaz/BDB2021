# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 00:34:31 2021

@author: inesd
"""

import pymysql.cursors

conection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',                             
                             db='VirologyDatabase',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
print ("connect successful!!")

def hitName(cursor, cursor1, cursor2, cursor3):
    
    try:
        
        cursor1.execute("SELECT query_name FROM db_query WHERE query_seq = ''")
        query_name = ''
        for r1 in cursor1:
            query_name = r1.get('query_name')
            cursor2.execute("SELECT * FROM virus")
            x = len(cursor2.fetchall())            
            for i in range(x):
                cursor3.execute("SELECT name_v FROM virus WHERE virus_id = " + str(i+1))
                name_v = ''
                for r3 in cursor3:
                    name_v = r3.get('name_v')                
                if (name_v == query_name):
                    sql = "INSERT INTO hitName (query_name, virus_id) VALUES ('" + query_name + "'," + str(i+1) + ")"
                    print(sql)
                    cursor.execute(sql)        
                    conection.commit()
                    
    except:
        
        print("Query error ...")
            
    return cursor

cursor = conection.cursor()
cursor1 = conection.cursor()
cursor2 = conection.cursor()
cursor3 = conection.cursor()

hitName(cursor, cursor1, cursor2, cursor3)


conection.close()