# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 17:08:18 2021

@author: inesd
"""

import random
import pymysql.cursors

conection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',                             
                             db='VirologyDatabase',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
print ("connect successful!!")

moleculeType = ["DNA", "RNA"] 
nDNA = ["A","C","G","T"]
nRNA = ["A","C","G","U"]
names_v = ["Adenovirus","Arbovirus (encephalitis)", "Arenaviridae","Baculoviridae",
           "LCM-Lassa viral complexes", "Tacaribe viral complexes", "Cytomegalovirus", 
           "Flavivirus amaril (Yellow fever)", "Flu A","H1N2 for pigs and humans",
           "H2N2 (Asian flu)", "H3N2 (Hong Kong Flu 1968)", "H5N1 (07-08 pandemic)", 
           "H7N7", "Hantaan", "Hepatitis A virus", "Herpes simplex", "Herpes simplex Type 1", 
           "Herpes simplex Type 2", "Human Herpesvirus 7", "Human Herpesvirus 8 (VHH-8)", 
           "Herpesvirus simiae (B virus)", "Herpesvirus varicella-zoster", 
           "Megavirus chilensis", "Mixovirus Parotiditis (Mumps)", "Papillomaviridae (Papillomas)", 
           "Papovavirus (Human Papilloma)", "Paramyxoviridae", "Parotiditis (Mumps)", 
           "Canine Parvovirus", "Human Parvovirus (B 19)", "Picornaviridae", 
           "Poliovirus (Poliomyelitis)", "Poxvirus", "Rinovirus", "Rotavirus", "SARS", 
           "SARS COV-2","Variola virus (Smallpox)", "VIH", "Belgrade Virus", "Bhanja Virus",
           "BK & JC Virus", "Bunyamwera Virus", "Coxsackie Virus", "Epstein-Barr Virus", 
           "Hemorrhagic conjunctivitis virus (AHC)", 
           "Lymphocytic choriomeningitis virus (other strains)", 
           "Lymphocytic choriomeningitis virus (neurotropic strains)", 
           "California encephalitis virus", "Newcastle disease virus", "Influenza virus type A", 
           "Influenza virus type B", "Influenza virus type C",  
           "Hepatitis A virus (human enterovirus type 72)", "Parainfluenza virus type 1", 
           "Varicella Zoster Virus (Varicella)", "Mumps virus", "Adeno-associated virus", 
           "Aichi virus", "Australian bat lyssavirus", "Fatal encephalitis", "Banna virus", 
           "Barmah forest virus", "Bunyamwera virus", "Bunyavirus La Crosse", 
           "Bunyavirus snowshoe hare", "Cercopithecine herpesvirus", "Chandipura virus", 
           "Chikungunya virus", "Cosavirus A", "Cowpox virus", "Coxsackievirus", 
           "Crimean-Congo hemorrhagic fever virus", "Dengue virus", "Dhori virus", "Dugbe virus", 
           "Duvenhage virus", "Eastern equine encephalitis virus", "Ebolavirus", "Echovirus", 
           "European bat lyssavirus", "Hantaan virus", "Hendra virus", "Hepatitis E virus", 
           "Hepatitis B virus", "Hepatitis C virus", "Hepatitis Delta virus", "Horsepox virus", 
           "Human adenovirus", "Human astrovirus", "Human coronavirus", "Human cytomegalovirus", 
           "Human enterovirus", "Japanese encephalitis virus", "Lagos bat virus", 
           "Louping ill virus", "Mayaro virus", "Norwalk virus", "Sagiyama virus"]

def db_query_seq(cursor, moleculeType, nDNA, nRNA):
    
    try:
        
        molType = random.choice(moleculeType) 
        if (molType == "DNA"):
            seq = random.choice(nDNA)
            b = random.randint(300,600)
            for j in range(b):
                seq += random.choice(nDNA)
            sql = "INSERT INTO db_query (query_seq, query_name, query_message) VALUES ('" + seq + "','','DNA Sequence query')"    
            print(sql)        
            cursor.execute(sql) 
            conection.commit()  
        elif (molType == "RNA"):
            seq = random.choice(nRNA)
            b = random.randint(300,600)
            for j in range(b):
                seq += random.choice(nRNA)
            sql = "INSERT INTO db_query (query_seq, query_name, query_message) VALUES ('" + seq + "','','RNA Sequence query')"    
            print(sql)        
            cursor.execute(sql) 
            conection.commit()
    
    except:
        
        print("Query error ...")
            
    return cursor
        
    
def db_query_name(cursor, names_v):
    
    try:
        
        sql = "INSERT INTO db_query (query_seq, query_name, query_message) VALUES ('','" + random.choice(names_v) + "','Virus name query')"    
        print(sql)            
        cursor.execute(sql)        
        conection.commit() 
        
    except:
        
        print("Query error ...")
            
    return cursor
    

cursor = conection.cursor()

for i in range(50):
    a = random.randint(0,1)
    if (a == 0):
        db_query_seq(cursor, moleculeType, nDNA, nRNA)
    elif (a == 1):
        db_query_name(cursor, names_v)        

    
conection.close()
    
