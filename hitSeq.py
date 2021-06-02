# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 17:38:29 2021

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

def hitSeq(cursor, cursor1, cursor2, cursor3, cursor4):
    
    try:
        
        cursor1.execute("SELECT query_seq FROM db_query WHERE query_name = ''")
        query_seq = ''
        for r1 in cursor1:
            query_seq = r1.get('query_seq')
            cursor2.execute("SELECT * FROM gene")
            x = len(cursor2.fetchall())            
            for i in range(x):
                cursor3.execute("SELECT genome_id FROM gene WHERE gene_id = " + str(i+1))
                genome_ID = ''
                for r3 in cursor3:
                    genome_ID = r3.get('genome_id')
                cursor3.execute("SELECT name_v FROM virus WHERE genome_id = " + str(genome_ID))
                name_v = ''
                for r3 in cursor3:
                    name_v = r3.get('name_v')
                cursor4.execute("SELECT nt_seq FROM gene WHERE gene_id = " + str(i+1))
                hit_seq = ''
                for r4 in cursor4:
                    hit_seq = r4.get('nt_seq')
                b = min(len(query_seq), len(hit_seq))
                c = 0
                for a in range(b):
                    if (query_seq[a] == hit_seq[a]):
                        c += 1
                if (c != 0):
                    hit_index = (c/b) * 100
                else:
                    hit_index = 0
                if (hit_index >= 30):
                    sql = "INSERT INTO hitSeq (query_seq, hit_index, hit_seq, name_v, gene_id) VALUES ('" + query_seq + "'," + str(hit_index) + ",'" + hit_seq + "','" + name_v + "'," + str(i+1) + ")" 
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
cursor4 = conection.cursor()

hitSeq(cursor, cursor1, cursor2, cursor3, cursor4)

conection.close()