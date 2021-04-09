# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 11:47:20 2021

@author: inesd
"""

import random
import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',                             
                             db='VirologyDatabase',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
print ("connect successful!!")

moleculeType = ["DNA", "RNA"] 

def genome(cursor, moleculeType):
    
    try: 
    
        randomMolType = random.choice(moleculeType)
        
        if (randomMolType == "DNA"):
            sql = "INSERT INTO genome (molecule_type, descript) VALUES ('" + randomMolType + "','It is a set of DNA genes')"
        elif (randomMolType == "RNA"):
            sql = "INSERT INTO genome (molecule_type, descript) VALUES ('" + randomMolType + "','It is a set of RNA genes')"
            
        print(sql)
          
        cursor.execute(sql) 
        
        connection.commit()
        
    except:
        
        print("Query error ...")
            
    return cursor

nDNA = ["A","C","G","T"]
nRNA = ["A","C","G","U"]

def gene(cursor, nDNA, nRNA):
    
    try: 
    
        genome_ID = 1;
        cursor.execute("SELECT * FROM genome")   
        genome_total = len(cursor.fetchall())
        
        for genome_ID in range(genome_total+1):
            a = random.randint(2,6)
            for i in range(a):
                cursor.execute("SELECT molecule_type FROM genome WHERE genome_id = " + str(genome_ID))
                molType = ''
                for r in cursor:
                    molType = r.get('molecule_type')  
                if (molType == "DNA"):
                    seq = random.choice(nDNA)
                    b = random.randint(300,600)
                    for j in range(b):
                        seq += random.choice(nDNA)
                    sql = "INSERT INTO gene (genome_id, nt_seq, descript) VALUES (" + str(genome_ID) + ",'" + seq + "','It is a DNA fragment')"    
                    print(sql)        
                    cursor.execute(sql) 
                    connection.commit()  
                elif (molType == "RNA"):
                    seq = random.choice(nRNA)
                    b = random.randint(300,600)
                    for j in range(b):
                        seq += random.choice(nRNA)
                    sql = "INSERT INTO gene (genome_id, nt_seq, descript) VALUES (" + str(genome_ID) + ",'" + seq + "','It is a RNA fragment')"    
                    print(sql)        
                    cursor.execute(sql) 
                    connection.commit()
        
    except:
        
        print("Query error ...")
            
    return cursor


cursor = connection.cursor()

for i in range(100):
    genome(cursor, moleculeType)
    
gene(cursor, nDNA, nRNA)
    
connection.close()
    




