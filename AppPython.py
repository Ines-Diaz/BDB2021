# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 20:10:21 2021

@author: inesd
"""

import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',                             
                             db='VirologyDatabase',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
print ("connect successful!!")


def insertnewgenome (connection, molecule_type, descript):
    cursor = connection.cursor()
    cursorT = connection.cursor()
    text = "INSERT INTO genome (molecule_type, descript) VALUES ('" + molecule_type + "','" + descript + "')"
    cursor.execute(text)
    connection.commit()
    cursorT.execute('SELECT * FROM genome')
    print()
    print('Row inserted in genome table successfully.')
    print()
    for resultado in cursorT:
        print(resultado)
    cursor.close()
    cursorT.close()
    
def insertnewgene (connection, genome_id, nt_seq, descript):
    cursor = connection.cursor()
    cursorT = connection.cursor()
    text = "INSERT INTO gene (genome_id, nt_seq, descript) VALUES (" + genome_id + ",'" + nt_seq + "','" + descript + "')"
    cursor.execute(text)
    connection.commit()
    cursorT.execute('SELECT * FROM gene')
    print()
    print('Row inserted in gene table successfully.')
    print()
    for resultado in cursorT:
        print(resultado)
    cursor.close()
    cursorT.close()
    
def insertnewtaxonomy (connection, family, order_v, class_v, phylum, kingdom, realm):
    cursor = connection.cursor()
    cursorT = connection.cursor()
    text = "INSERT INTO taxonomy (family, order_v, class, phylum, kingdom, realm) VALUES ('" + family + "','" + order_v + "','" + class_v + "','" + phylum + "','" + kingdom + "','" + realm + "')"
    cursor.execute(text)
    connection.commit()
    cursorT.execute('SELECT * FROM taxonomy')
    print()
    print('Row inserted in taxonomy table successfully.')
    print()
    for resultado in cursorT:
        print(resultado)
    cursor.close()
    cursorT.close()

def insertnewvirus (connection, name_v, genome_id, taxonomy_id, virus_type, shape, year_origin):
    cursor = connection.cursor()
    cursorT = connection.cursor()
    text = "INSERT INTO virus (name_v, genome_id, taxonomy_id, virus_type, shape, year_origin) VALUES ('" + name_v + "'," + genome_id + "," + taxonomy_id + ",'" + virus_type + "','" + shape + "'," + year_origin + ")"
    cursor.execute(text)
    connection.commit()
    cursorT.execute('SELECT * FROM virus')
    print()
    print('Row inserted in virus table successfully.')
    print()
    for resultado in cursorT:
        print(resultado)
    cursor.close()
    cursorT.close()
    
def insertnewdb_query (connection, query_seq, query_name, query_message):
    cursor = connection.cursor()
    cursorT = connection.cursor()
    text = "INSERT INTO db_query (query_seq, query_name, query_message) VALUES ('" + query_seq + "','" + query_name + "','" + query_message + "')"
    cursor.execute(text)
    connection.commit()
    cursorT.execute('SELECT * FROM db_query')
    print()
    print('Row inserted in db_query table successfully.')
    print()
    for resultado in cursorT:
        print(resultado)
    cursor.close()
    cursorT.close()
    
def insertnewhitSeq (connection, query_seq, hit_index, hit_seq,	name_v,	gene_id):
    cursor = connection.cursor()
    cursorT = connection.cursor()
    text = "INSERT INTO hitSeq (query_seq, hit_index, hit_seq,	name_v,	gene_id) VALUES ('" + query_seq + "'," + hit_index + ",'" + hit_seq + "','" + name_v + "'," + gene_id + ")"
    cursor.execute(text)
    connection.commit()
    cursorT.execute('SELECT * FROM hitSeq')
    print()
    print('Row inserted in hitSeq table successfully.')
    print()
    for resultado in cursorT:
        print(resultado)
    cursor.close()
    cursorT.close()
    
def insertnewhitName (connection, query_name, virus_id):
    cursor = connection.cursor()
    cursorT = connection.cursor()
    text = "INSERT INTO hitName (query_name, virus_id) VALUES ('" + query_name + "'," + virus_id + ")"
    cursor.execute(text)
    connection.commit()
    cursorT.execute('SELECT * FROM hitName')
    print()
    print('Row inserted in hitName table successfully.')
    print()
    for resultado in cursorT:
        print(resultado)
    cursor.close()
    cursorT.close()
    
    
def relation1(connection, gene_id):
    cursor = connection.cursor()
    cursorT = connection.cursor()
    cursor.execute('SELECT genome_id FROM gene WHERE gene_id = ' + gene_id)
    for resultado in cursor:
        genome_id = str(resultado.get('genome_id'))
    cursorT.execute('SELECT * FROM genome WHERE genome_id = ' + genome_id)
    print()
    for resultado in cursorT:
        print(resultado)
    cursor.close()
    cursorT.close()    
    
def relation2(connection, virus_id): 
    cursor = connection.cursor()
    cursorT = connection.cursor()
    cursor.execute('SELECT taxonomy_id FROM virus WHERE virus_id = ' + virus_id)
    for resultado in cursor:
        taxonomy_id = str(resultado.get('taxonomy_id'))
    cursorT.execute('SELECT * FROM taxonomy WHERE taxonomy_id = ' + taxonomy_id)
    print()
    for resultado in cursorT:
        print(resultado)
    cursor.close()
    cursorT.close()

def relation3(connection, virus_id): 
    cursor = connection.cursor()
    cursorT = connection.cursor()
    cursor.execute('SELECT genome_id FROM virus WHERE virus_id = ' + virus_id)
    for resultado in cursor:
        genome_id = str(resultado.get('genome_id'))
    cursorT.execute('SELECT * FROM genome WHERE genome_id = ' + genome_id)
    print()
    for resultado in cursorT:
        print(resultado)
    cursor.close()
    cursorT.close()    
    
def relation4(connection, hit_id):  
    cursor = connection.cursor()
    cursorT = connection.cursor()
    cursor.execute('SELECT query_seq FROM hitSeq WHERE hit_id = ' + hit_id)
    for resultado in cursor:
        query_seq = str(resultado.get('query_seq'))
    cursorT.execute('SELECT query_id, query_seq, query_message FROM db_query WHERE query_seq = "' + query_seq + '"')
    print()
    for resultado in cursorT:
        print(resultado)
    cursor.close()
    cursorT.close()

def relation5(connection, hit_id): 
    cursor = connection.cursor()
    cursorT = connection.cursor()
    cursor.execute('SELECT name_v FROM hitSeq WHERE hit_id = ' + hit_id)
    for resultado in cursor:
        name_v = str(resultado.get('name_v'))
    cursorT.execute('SELECT * FROM virus WHERE name_v = "' + name_v + '"')
    print()
    for resultado in cursorT:
        print(resultado)
    cursor.close()
    cursorT.close()    
    
def relation6(connection, hit_id):     
    cursor = connection.cursor()
    cursorT = connection.cursor()
    cursor.execute('SELECT gene_id FROM hitSeq WHERE hit_id = ' + hit_id)
    for resultado in cursor:
        gene_id = str(resultado.get('gene_id'))
    cursorT.execute('SELECT * FROM gene WHERE gene_id = ' + gene_id)
    print()
    for resultado in cursorT:
        print(resultado)
    cursor.close()
    cursorT.close()    
    
def relation7(connection, hit_id):     
    cursor = connection.cursor()
    cursorT = connection.cursor()
    cursor.execute('SELECT query_name FROM hitName WHERE hit_id = ' + hit_id)
    for resultado in cursor:
        query_name = str(resultado.get('query_name'))
    cursorT.execute('SELECT query_id, query_name, query_message FROM db_query WHERE query_name = "' + query_name + '"')
    print()
    for resultado in cursorT:
        print(resultado)
    cursor.close()
    cursorT.close()    
    
def relation8(connection, hit_id):     
    cursor = connection.cursor()
    cursorT = connection.cursor()
    cursor.execute('SELECT virus_id FROM hitName WHERE hit_id = ' + hit_id)
    for resultado in cursor:
        virus_id = str(resultado.get('virus_id'))
    cursorT.execute('SELECT * FROM virus WHERE virus_id = ' + virus_id)
    print()
    for resultado in cursorT:
        print(resultado)
    cursor.close()
    cursorT.close()    
    
   
def query1(connection, shape):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM virus WHERE shape = "' + shape + '"')
    print()
    for result in cursor:
        print(result)
    cursor.close() 
    
def query2(connection, year_origin):
    cursor = connection.cursor()
    cursor.execute('SELECT virus_id, name_v, year_origin FROM virus WHERE year_origin >= ' + str(year_origin) + ' ORDER BY year_origin')
    print()
    for result in cursor:
        print(result)
    cursor.close()
   
def query3(connection, length_name_v):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM hitSeq WHERE length(name_v) >= ' + str(length_name_v))
    print()
    for result in cursor:
        print(result)
    cursor.close()
   
def query4(connection, virus_type):
    cursor = connection.cursor()
    cursor.execute('SELECT virus_id, name_v, virus_type FROM virus WHERE INSTR(virus_type,"' + virus_type + '") > 0 ORDER BY virus_type')
    print()
    for result in cursor:
        print(result)
    cursor.close()
 
def query5(connection, sequence):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM gene WHERE INSTR(nt_seq,"' + sequence + '") > 0')
    print()
    for result in cursor:
        print(result)
    cursor.close()
    
def query6(connection, tax_class):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM taxonomy WHERE class = "' + tax_class + '"')
    print()
    for result in cursor:
        print(result)
    cursor.close()
    
def query7(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT g.gene_id, g.genome_id, g.nt_seq, G.molecule_type FROM gene g JOIN genome G WHERE g.genome_id = G.genome_id')
    print()
    for result in cursor:
        print(result)
    cursor.close()
    
def query8(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT v.virus_id, v.name_v, t.family, t.order_v, t.class, t.phylum, t.kingdom, t.realm FROM virus v JOIN taxonomy t WHERE v.taxonomy_id = t.taxonomy_id ORDER BY realm')
    print()
    for result in cursor:
        print(result)
    cursor.close()

def query9(connection, odd_even):
    cursor = connection.cursor()
    cursor.execute('SELECT v.virus_id, v.name_v, v.virus_type, g.molecule_type FROM virus v JOIN genome g WHERE v.genome_id = g.genome_id AND v.virus_id%2 = ' + str(odd_even))
    print()
    for result in cursor:
        print(result)
    cursor.close()
    
def query10(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT hs.hit_id, hs.name_v, hs.hit_index, hs.query_seq, db.query_seq FROM hitSeq hs JOIN db_query db WHERE hs.query_seq = db.query_seq')
    print()
    for result in cursor:
        print(result)
    cursor.close()
     
def query11(connection, virus_type):
    cursor = connection.cursor()
    cursor.execute('SELECT v.name_v, g.molecule_type, v.virus_type, v.shape FROM virus v JOIN genome g WHERE INSTR(v.virus_type,"' + virus_type + '") > 0 AND g.genome_id = v.genome_id')
    print()
    for result in cursor:
        print(result)
    cursor.close()
    
def query12(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT hn.query_name, hn.virus_id, v.virus_type, v.shape FROM hitName hn JOIN virus v WHERE hn.virus_id = v.virus_id')
    print()
    for result in cursor:
        print(result)
    cursor.close()

def query13(connection, realm):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM virus WHERE taxonomy_id IN (SELECT taxonomy_id FROM taxonomy WHERE realm = "' + realm + '")')
    print()
    for result in cursor:
        print(result)
    cursor.close()

def query14(connection, molecule_type):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM gene WHERE genome_id IN (SELECT genome_id FROM genome WHERE molecule_type = "' + molecule_type + '")')
    print()
    for result in cursor:
        print(result)
    cursor.close()

def query15(connection, length_nt_seq_1, length_nt_seq_2):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM hitSeq WHERE gene_id IN (SELECT gene_id FROM gene WHERE length(nt_seq) >= ' + str(length_nt_seq_1) + ' AND length(nt_seq) <= ' + str(length_nt_seq_2) + ')')
    print()
    for result in cursor:
        print(result)
    cursor.close()

def query16(connection, name_v):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM taxonomy WHERE taxonomy_id = (SELECT t.taxonomy_id FROM taxonomy t JOIN virus v WHERE t.taxonomy_id = v.taxonomy_id AND v.name_v = "' + name_v + '")')
    print()
    for result in cursor:
        print(result)
    cursor.close()

def query17(connection, shape):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM genome WHERE genome_id IN (SELECT v.genome_id FROM virus v JOIN genome g WHERE g.genome_id = v.genome_id AND v.shape = "' + shape + '") ORDER BY genome_id')
    print()
    for result in cursor:
        print(result)
    cursor.close()
 
def query18(connection, sequence):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM genome WHERE genome_id IN (SELECT G.genome_id FROM genome G JOIN gene g WHERE G.genome_id = g.genome_id AND INSTR(g.nt_seq,"' + sequence + '") > 0)')
    print()
    for result in cursor:
        print(result)
    cursor.close()
    
def query19(connection, odd_even):
    cursor = connection.cursor()
    cursor.execute('SELECT genome_id, COUNT(*) "Total Genes" FROM gene WHERE genome_id%2 = ' + str(odd_even) + ' GROUP BY genome_id')
    print()
    for result in cursor:
        print(result)
    cursor.close()

def query20(connection, family):
    cursor = connection.cursor()
    cursor.execute('SELECT v.virus_id, v.name_v, v.virus_type, v.shape, v.year_origin, t.family FROM virus v JOIN (SELECT taxonomy_id, family FROM taxonomy WHERE family = "' + family + '") AS t ON v.taxonomy_id = t.taxonomy_id ORDER BY v.virus_id')
    print()
    for result in cursor:
        print(result)
    cursor.close()
    
    
print()
print('1. Insert data.')
print('2. Relate data.')
print('3. Query data.')
print('4. Exit the program.')

mainoption = int(input('What would you like to do? '))
print()

while mainoption != 4:
    
    if mainoption == 1:
        
        print('Available tables:')
        print('1. genome')
        print('2. gene')
        print('3. taxonomy')
        print('4. virus')
        print('5. db_query')
        print('6. hitSeq')
        print('7. hitName')
        print('8. Do not insert more data in the tables.')
        
        insertoption = int(input('In which table do you want to insert data? '))
        print()
        
        while insertoption != 8:
            
            if insertoption == 1:
                
                molecule_type = input('Molecule type: ')
                descript = input('Description: ')
                
                insertnewgenome(connection, molecule_type, descript)
                
            elif insertoption == 2:
                
                genome_id = input('Genome ID: ')
                nt_seq = input('Nucleotide sequence: ')
                descript = input('Description: ')
                
                insertnewgene(connection, genome_id, nt_seq, descript)
                
            elif insertoption == 3:
                
                family = input('Family: ')
                order_v = input('Order: ')
                class_v = input('Class: ')
                phylum = input('Phylum: ')
                kingdom = input('Kingdom: ')
                realm = input('Realm: ')    
                
                insertnewtaxonomy(connection, family, order_v, class_v, phylum, kingdom, realm)               
                
            elif insertoption == 4:
                
                name_v = input('Virus name: ')
                genome_id = input('Genome ID: ')
                taxonomy_id = input('Taxonomy ID: ')
                virus_type = input('Virus type: ')
                shape = input('Shape: ')
                year_origin = input('Origin year: ')
                
                insertnewvirus(connection, name_v, genome_id, taxonomy_id, virus_type, shape, year_origin)
            
            elif insertoption == 5:
                
                option = input('Is it a sequence query (sq) or a name query (nq)? Write sq or nq: ')
                if option == 'sq':
                    query_seq = input('Query sequence: ')
                    query_name = ''
                    query_message = input('Query message: ')
                    insertnewdb_query(connection, query_seq, query_name, query_message)
                elif option == 'nq':
                    query_seq = ''
                    query_name = input('Query name: ')
                    query_message = input('Query message: ')
                    insertnewdb_query(connection, query_seq, query_name, query_message)
                else:
                    print('Error, option not recognized.')
                    
                
            elif insertoption == 6:
                
                query_seq = input('Query sequence: ')
                hit_index = input('Hit index: ')
                hit_seq = input('Hit sequence: ')
                name_v = input('Virus Name: ')	
                gene_id = input('Gene ID: ')
                
                insertnewhitSeq(connection, query_seq, hit_index, hit_seq, name_v, gene_id)
                
            elif insertoption == 7:
                
                query_name = input('Query name: ')
                virus_id = input('Virus ID: ')
                
                insertnewhitName(connection, query_name, virus_id)
                
            else:
                print('Error, option not recognized.')
            
            print()
            print('Available tables:')
            print('1. genome')
            print('2. gene')
            print('3. taxonomy')
            print('4. virus')
            print('5. db_query')
            print('6. hitSeq')
            print('7. hitName')
            print('8. Do not insert more data in the tables.')
            
            insertoption = int(input('In which table do you want to insert data? '))
            print()
            

    elif mainoption == 2:
        
        print('Available relations:')
        print('1. Given the gene_id of a gene, show the information corresponding to the genome of that gene.')
        print('2. Given the virus_id of a virus, show the information corresponding to the taxonomy of that virus.')
        print('3. Given the virus_id of a virus, show the information corresponding to the genome of that virus')
        print('4. Given the hit_id of a sequence hit, show the information corresponding to the query characteristics of that sequence hit.')
        print('5. Given the hit_id of a sequence hit, show the information corresponding to the virus to which the sequence corresponds.')
        print('6. Given the hit_id of a sequence hit, show the information corresponding to the gene to which the sequence corresponds.')
        print('7. Given the hit_id of a name hit, show the information corresponding to the query characteristics of that name hit.')        
        print('8. Given the hit_id of a name hit, show the information corresponding to the virus to which the name corresponds.')
        print('9. Do not show more relations.')
        
        relateoption = int(input('What relation would you like to make? '))
        print()
        
        while relateoption != 9:
            
            if relateoption == 1:
                
                gene_id = input('Gene ID: ')  
                relation1(connection, gene_id)            
            
            elif relateoption == 2:
                
                virus_id = input('Virus ID: ')  
                relation2(connection, virus_id)
                
            elif relateoption == 3:
                
                virus_id = input('Virus ID: ')  
                relation3(connection, virus_id)
                
            elif relateoption == 4:
                
                hit_id = input('Hit ID: ')  
                relation4(connection, hit_id)
                
            elif relateoption == 5:
            
                hit_id = input('Hit ID: ')  
                relation5(connection, hit_id)
                
            elif relateoption == 6:
                
                hit_id = input('Hit ID: ')  
                relation6(connection, hit_id)
                
            elif relateoption == 7:
                
                hit_id = input('Hit ID: ')  
                relation7(connection, hit_id)
                
            elif relateoption == 8:
                
                hit_id = input('Hit ID: ')  
                relation8(connection, hit_id)
            
            else:
                print('Error, option not recognized.')
        
            print()
            print('Available relations:')
            print('1. Given the gene_id of a gene, show the information corresponding to the genome of that gene.')
            print('2. Given the virus_id of a virus, show the information corresponding to the taxonomy of that virus.')
            print('3. Given the virus_id of a virus, show the information corresponding to the genome of that virus')
            print('4. Given the hit_id of a sequence hit, show the information corresponding to the query characteristics of that sequence hit.')
            print('5. Given the hit_id of a sequence hit, show the information corresponding to the virus to which the sequence corresponds.')
            print('6. Given the hit_id of a sequence hit, show the information corresponding to the gene to which the sequence corresponds.')
            print('7. Given the hit_id of a name hit, show the information corresponding to the query characteristics of that name hit.')        
            print('8. Given the hit_id of a name hit, show the information corresponding to the virus to which the name corresponds.')
            print('9. Do not show more relations.')
            
            relateoption = int(input('What relation would you like to make? '))
            print()
                
        
    elif mainoption == 3:
        
        print('Available queries: ')
        print('1.  Return all virus with a specific shape')
        print('2.  Return all virus registered from a specific year of origin')
        print('3.  Return virus whose names have a specific character length from hit sequences')
        print('4.  Return viruses from specific types')
        print('5.  Return genes with specific partial/total nucleotide sequence')
        print('6.  Return virus taxonomy from a specific class')
        print('7.  Return gene molecule type')
        print('8.  Return taxonomy of each virus')
        print('9.  Return molecule type of viruses with odd/even identifier')
        print('10. Return if a hit sequences matches a query sequence completely')
        print('11. Return viruses and genomes from a specific virus type')
        print('12. Return if a specific virus has already been searched by name')
        print('13. Return viruses from a specific realm')
        print('14. Return genes from a specific molecule type')
        print('15. Return sequences from a hit gene of a specific length')
        print('16. Return virus taxonomy from a specific virus name')
        print('17. Return genomes containing a specific virus shape')
        print('18. Return genomes containing a specific nucleotide sequence')
        print('19. Return the amount of odd/even identifier genomes')
        print('20. Return viruses that belong to a specific family')
        print('21. Do not make any more queries')
        
        queryoption = int(input('What query would you like to perform? '))  
        print()
        
        while queryoption != 21:
            
            if queryoption == 1:
                
                shape = str(input('Choose a shape parameter:\n{Helical, Icosahedral, Envelope, Complex}: '))
                query1(connection, shape) 
                
            elif queryoption == 2:
                
                year_origin = int(input('Choose year of origin:\n{1980-2021}: '))
                query2(connection, year_origin)
                
            elif queryoption == 3:
                
                length_name_v = int(input('Specify name length (in characters): '))
                query3(connection, length_name_v)
                
            elif queryoption == 4:
                
                virus_type = str(input('Enter virus type:\n{DNA, RNA}: '))
                query4(connection, virus_type)
                
            elif queryoption == 5:
                
                sequence = str(input('Enter specific genetic sequence (using A, C, G, T or U): '))
                query5(connection, sequence)
                
            elif queryoption == 6:
                
                tax_class = str(input('Select specific taxonomy class:\n{Megaviricetes, Pokkesviricetes, Tectiliviricetes, Pisoniviricetes, Stelpaviricetes, Alsuviricetes, Insthoviricetes}: '))
                query6(connection, tax_class)
                
            elif queryoption == 7:
                
                query7(connection)
                
            elif queryoption == 8:
                
                query8(connection)
                
            elif queryoption == 9:
                
                odd_even = int(input('Select odd (0) or even (1): '))
                query9(connection, odd_even)
                
            elif queryoption == 10:
                
                query10(connection)
                
            elif queryoption == 11:
                
                virus_type = str(input('Enter virus type:\n{DNA, RNA}: '))
                query11(connection, virus_type)
                
            elif queryoption == 12:
                
                query12(connection)
                
            elif queryoption == 13:
                
                realm = str(input('Introduce taxonomy realm:\n{Duplodnaviria, Varidnaviria, Pokkesviricetes, Riboviria, Monodnaviria}: '))
                query13(connection, realm)
                
            elif queryoption == 14:
                
                molecule_type = str(input('Select molecule type (DNA or RNA): '))
                query14(connection, molecule_type)
                
            elif queryoption == 15:
                
                print('Enter genetic sequence length:')
                length_nt_seq_1 = int(input('Minimum length: '))
                length_nt_seq_2 = int(input('Maximum length: '))
                query15(connection, length_nt_seq_1, length_nt_seq_2)
                
            elif queryoption == 16:
                
                name_v = str(input('POSSIBLE VIRUS NAMES:\n{Adenovirus,Arbovirus (encephalitis), Arenaviridae,Baculoviridae, LCM-Lassa viral complexes, Tacaribe viral complexes, Cytomegalovirus, Flavivirus amaril (Yellow fever), Flu A,H1N2 for pigs and humans, H2N2 (Asian flu), H3N2 (Hong Kong Flu 1968), H5N1 (07-08 pandemic), H7N7, Hantaan, Hepatitis A virus, Herpes simplex, Herpes simplex Type 1, Herpes simplex Type 2, Human Herpesvirus 7, Human Herpesvirus 8 (VHH-8), Herpesvirus simiae (B virus), Herpesvirus varicella-zoster, Megavirus chilensis, Mixovirus Parotiditis (Mumps), Papillomaviridae (Papillomas), Papovavirus (Human Papilloma), Paramyxoviridae, Parotiditis (Mumps), Canine Parvovirus, Human Parvovirus (B 19), Picornaviridae, Poliovirus (Poliomyelitis), Poxvirus, Rinovirus, Rotavirus, SARS, SARS COV-2,Variola virus (Smallpox), VIH, Belgrade Virus, Bhanja Virus, BK & JC Virus, Bunyamwera Virus, Coxsackie Virus, Epstein-Barr Virus, Hemorrhagic conjunctivitis virus (AHC), Lymphocytic choriomeningitis virus (other strains), Lymphocytic choriomeningitis virus (neurotropic strains), California encephalitis virus, Newcastle disease virus, Influenza virus type A, Influenza virus type B, Influenza virus type C,  Hepatitis A virus (human enterovirus type 72), Parainfluenza virus type 1, Varicella Zoster Virus (Varicella), Mumps virus, Adeno-associated virus, Aichi virus, Australian bat lyssavirus, Fatal encephalitis, Banna virus, Barmah forest virus, Bunyamwera virus, Bunyavirus La Crosse, Bunyavirus snowshoe hare, Cercopithecine herpesvirus, Chandipura virus, Chikungunya virus, Cosavirus A, Cowpox virus, Coxsackievirus, Crimean-Congo hemorrhagic fever virus, Dengue virus, Dhori virus, Dugbe virus, Duvenhage virus, Eastern equine encephalitis virus, Ebolavirus, Echovirus, European bat lyssavirus, Hantaan virus, Hendra virus, Hepatitis E virus, Hepatitis B virus, Hepatitis C virus, Hepatitis Delta virus, Horsepox virus, Human adenovirus, Human astrovirus, Human coronavirus, Human cytomegalovirus, Human enterovirus, Japanese encephalitis virus, Lagos bat virus, Louping ill virus, Mayaro virus,Norwalk virus, Sagiyama virus}\nSelect virus name: '))
                query16(connection, name_v)
                
            elif queryoption == 17:
                
                shape = str(input('Choose a shape parameter:\n{Helical, Icosahedral, Envelope, Complex}: '))
                query17(connection, shape)
                
            elif queryoption == 18:
                
                sequence = str(input('Enter specific genetic sequence (using A, C, G, T or U): '))
                query18(connection, sequence)

            elif queryoption == 19:
                
                odd_even = int(input('Select odd (0) or even (1): '))
                query19(connection, odd_even)
                
            elif queryoption == 20:
                
                family = str(input('POSSIBLE FAMILY NAMES:\n{Alloherpesviridae, Herpesviridae, Malacoherpesviridae, Ackermannviridae, Autographiviridae, Chaseviridae, Demerecviridae, Drexlerviridae, Herelleviridae, Myoviridae, Podoviridae, Siphoviridae, Mimiviridae, Phycodnaviridae, Pandoraviridae, Ascoviridae, Iridoviridae, Marseilleviridae, Pithoviridae, Mininucleoviridae, Asfarviridae, Poxviridae, Medusaviridae, Lavidaviridae, Adenoviridae, Corticoviridae, Tectiviridae, Turriviridae, Finnlakeviridae, Autolykiviridae, Sphaerolipoviridae, Portogloboviridae}\nSelect taxonomic family: '))
                query20(connection, family)
                
            else:                
                print('Error, option not recognized.')
                
            print()
            print('Available queries: ')
            print('1.  Return all virus with a specific shape')
            print('2.  Return all virus registered from a specific year of origin')
            print('3.  Return virus whose names have a specific character length from hit sequences')
            print('4.  Return viruses from specific types')
            print('5.  Return genes with specific partial/total nucleotide sequence')
            print('6.  Return virus taxonomy from a specific class')
            print('7.  Return gene molecule type')
            print('8.  Return taxonomy of each virus')
            print('9.  Return molecule type of viruses with odd/even identifier')
            print('10. Return if a hit sequences matches a query sequence completely')
            print('11. Return viruses and genomes from a specific virus type')
            print('12. Return if a specific virus has already been searched by name')
            print('13. Return viruses from a specific realm')
            print('14. Return genes from a specific molecule type')
            print('15. Return sequences from a hit gene of a specific length')
            print('16. Return virus taxonomy from a specific virus name')
            print('17. Return genomes containing a specific virus shape')
            print('18. Return genomes containing a specific nucleotide sequence')
            print('19. Return the amount of odd/even identifier genomes')
            print('20. Return viruses that belong to a specific family')
            print('21. Do not make any more queries')
            
            queryoption = int(input('What query would you like to perform? '))  
            print()
                
        
    else:
        print('Error, option not recognized.')
        
        
    print()
    print('1. Insert data.')
    print('2. Relate data.')
    print('3. Query data.')
    print('4. Exit the program.')

    mainoption = int(input('What would you like to do? '))
    print()  
        
connection.close()
