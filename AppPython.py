# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 20:10:21 2021

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

def insertnewgenome (molecule_type, descript):
    cursor = conection.cursor()
    cursorT = conection.cursor()
    text = "INSERT INTO genome (molecule_type, descript) VALUES ('" + molecule_type + "','" + descript + "')"
    cursor.execute(text)
    conection.commit()
    cursorT.execute('SELECT * FROM genome')
    print()
    print('Row inserted in genome table successfully.')
    print()
    for resultado in cursorT:
        print(resultado)
    cursor.close()
    cursorT.close()
    
def insertnewgene (genome_id, nt_seq, descript):
    cursor = conection.cursor()
    cursorT = conection.cursor()
    text = "INSERT INTO gene (genome_id, nt_seq, descript) VALUES (" + genome_id + ",'" + nt_seq + "','" + descript + "')"
    cursor.execute(text)
    conection.commit()
    cursorT.execute('SELECT * FROM gene')
    print()
    print('Row inserted in gene table successfully.')
    print()
    for resultado in cursorT:
        print(resultado)
    cursor.close()
    cursorT.close()
    
def insertnewtaxonomy (family, order_v, class_v, phylum, kingdom, realm):
    cursor = conection.cursor()
    cursorT = conection.cursor()
    text = "INSERT INTO taxonomy (family, order_v, class, phylum, kingdom, realm) VALUES ('" + family + "','" + order_v + "','" + class_v + "','" + phylum + "','" + kingdom + "','" + realm + "')"
    cursor.execute(text)
    conection.commit()
    cursorT.execute('SELECT * FROM taxonomy')
    print()
    print('Row inserted in taxonomy table successfully.')
    print()
    for resultado in cursorT:
        print(resultado)
    cursor.close()
    cursorT.close()

def insertnewvirus (name_v, genome_id, taxonomy_id, virus_type, shape, year_origin):
    cursor = conection.cursor()
    cursorT = conection.cursor()
    text = "INSERT INTO virus (name_v, genome_id, taxonomy_id, virus_type, shape, year_origin) VALUES ('" + name_v + "'," + genome_id + "," + taxonomy_id + ",'" + virus_type + "','" + shape + "'," + year_origin + ")"
    cursor.execute(text)
    conection.commit()
    cursorT.execute('SELECT * FROM virus')
    print()
    print('Row inserted in virus table successfully.')
    print()
    for resultado in cursorT:
        print(resultado)
    cursor.close()
    cursorT.close()
    
def insertnewdb_query (query_seq, query_name, query_message):
    cursor = conection.cursor()
    cursorT = conection.cursor()
    text = "INSERT INTO db_query (query_seq, query_name, query_message) VALUES ('" + query_seq + "','" + query_name + "','" + query_message + "')"
    cursor.execute(text)
    conection.commit()
    cursorT.execute('SELECT * FROM db_query')
    print()
    print('Row inserted in db_query table successfully.')
    print()
    for resultado in cursorT:
        print(resultado)
    cursor.close()
    cursorT.close()
    
def insertnewhitSeq (query_seq, hit_index, hit_seq,	name_v,	gene_id):
    cursor = conection.cursor()
    cursorT = conection.cursor()
    text = "INSERT INTO hitSeq (query_seq, hit_index, hit_seq,	name_v,	gene_id) VALUES ('" + query_seq + "'," + hit_index + ",'" + hit_seq + "','" + name_v + "'," + gene_id + ")"
    cursor.execute(text)
    conection.commit()
    cursorT.execute('SELECT * FROM hitSeq')
    print()
    print('Row inserted in hitSeq table successfully.')
    print()
    for resultado in cursorT:
        print(resultado)
    cursor.close()
    cursorT.close()
    
def insertnewhitName (query_name, virus_id):
    cursor = conection.cursor()
    cursorT = conection.cursor()
    text = "INSERT INTO hitName (query_name, virus_id) VALUES ('" + query_name + "'," + virus_id + ")"
    cursor.execute(text)
    conection.commit()
    cursorT.execute('SELECT * FROM hitName')
    print()
    print('Row inserted in hitName table successfully.')
    print()
    for resultado in cursorT:
        print(resultado)
    cursor.close()
    cursorT.close()