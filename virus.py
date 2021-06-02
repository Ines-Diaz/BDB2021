# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 20:47:29 2021

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

print("connect successful!!")

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
virus_type_DNA = ["Single-Stranded DNA", "Double-Stranded DNA"]
virus_type_RNA = ["Double-Stranded RNA", "Positive Single-Stranded RNA", 
                  "Negative Single-Stranded RNA", "Retrotrascript Single-Stranded RNA"]
shape = ["Helical", "Icosahedral", "Envelope", "Complex"]
genome_ID = random.sample(range(100), 100) 
taxonomy_ID = random.sample(range(100), 100) 

def listVirus(cursor, names_v, genome_ID, taxonomy_ID, virus_type_DNA, virus_type_RNA, shape):
    
    try: 
        
        for i in range(100):
            
            if (genome_ID[i] == 0):
                genome_ID[i] = 100
            if (taxonomy_ID[i] == 0):
                taxonomy_ID[i] = 100
                
            cursor.execute("SELECT molecule_type FROM genome WHERE genome_id = " + str(genome_ID[i]))
            molType = ''
            for r in cursor:
                molType = r.get('molecule_type')  
            if (molType == "DNA"):
                sql = "INSERT INTO virus (name_v, genome_id, taxonomy_id, virus_type, shape, year_origin) VALUES ('" + names_v[i] + "'," + str(genome_ID[i]) + "," + str(taxonomy_ID[i]) + ",'" + random.choice(virus_type_DNA) + "','" + random.choice(shape) + "'," + str(random.randint(1980,2021)) + ")"
            elif (molType == "RNA"):
                sql = "INSERT INTO virus (name_v, genome_id, taxonomy_id, virus_type, shape, year_origin) VALUES ('" + names_v[i] + "'," + str(genome_ID[i]) + "," + str(taxonomy_ID[i]) + ",'" + random.choice(virus_type_RNA) + "','" + random.choice(shape) + "'," + str(random.randint(1980,2021)) + ")" 
            print(sql)
            cursor.execute(sql)
            connection.commit()

    except:

        print("Query error ...")

    return cursor


cursor = connection.cursor()

listVirus(cursor, names_v, genome_ID, taxonomy_ID, virus_type_DNA, virus_type_RNA, shape)

connection.close()