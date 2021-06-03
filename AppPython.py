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

# Posible variable shape a elegir valor entre {"Helical", "Icosahedral", "Envelope", "Complex"}    
def query1(conection):
    cursor = conection.cursor()
    cursor.execute('SELECT * FROM virus WHERE shape = "Helical"')
    for result in cursor:
        print(result)
    cursor.close() 
    
# Posible variable year_origin a elegir valor entre {1980-2021}
def query2(conection):
    cursor = conection.cursor()
    cursor.execute('SELECT virus_id, name_v, year_origin FROM virus WHERE year_origin >= 2010 ORDER BY year_origin')
    for result in cursor:
        print(result)
    cursor.close()

# Posible variable length_name_v    
def query3(conection):
    cursor = conection.cursor()
    cursor.execute('SELECT * FROM hitSeq WHERE length(name_v) >= 30')
    for result in cursor:
        print(result)
    cursor.close()

# Posible variable virus_type a elegir valor entre {"DNA","RNA"}    
def query4(conection):
    cursor = conection.cursor()
    cursor.execute('SELECT virus_id, name_v, virus_type FROM virus WHERE INSTR(virus_type,"DNA") > 0 ORDER BY virus_type')
    for result in cursor:
        print(result)
    cursor.close()
 
# Posible variable sequence a elegir un combinado de las letras {A, C, G, T}
def query5(conection):
    cursor = conection.cursor()
    cursor.execute('SELECT * FROM gene WHERE INSTR(nt_seq,"AGCUCAUG") > 0')
    for result in cursor:
        print(result)
    cursor.close()

# Posible variable class a elegir valor entre {"Megaviricetes", "Pokkesviricetes", "Tectiliviricetes", "Pisoniviricetes", "Stelpaviricetes", "Alsuviricetes", "Insthoviricetes"}    
def query6(conection):
    cursor = conection.cursor()
    cursor.execute('SELECT * FROM taxonomy WHERE class="Megaviricetes"')
    for result in cursor:
        print(result)
    cursor.close()
    
def query7(conection):
    cursor = conection.cursor()
    cursor.execute('SELECT g.gene_id, g.genome_id, g.nt_seq, G.molecule_type FROM gene g JOIN genome G WHERE g.genome_id = G.genome_id')
    for result in cursor:
        print(result)
    cursor.close()
    
def query8(conection):
    cursor = conection.cursor()
    cursor.execute('SELECT v.virus_id, v.name_v, t.family, t.order_v, t.class, t.phylum, t.kingdom, t.realm FROM virus v JOIN taxonomy t WHERE v.taxonomy_id = t.taxonomy_id ORDER BY realm')
    for result in cursor:
        print(result)
    cursor.close()

#Posible variable par_impar: si es par -> par_impar = 0; si es impar -> par_impar = 1
def query9(conection):
    cursor = conection.cursor()
    cursor.execute('SELECT v.virus_id, v.name_v, v.virus_type, g.molecule_type FROM virus v JOIN genome g WHERE v.genome_id = g.genome_id AND v.virus_id%2=0')
    for result in cursor:
        print(result)
    cursor.close()
    
def query10(conection):
    cursor = conection.cursor()
    cursor.execute('SELECT hs.hit_id, hs.name_v, hs.hit_index, hs.query_seq, db.query_seq FROM hitSeq hs JOIN db_query db WHERE hs.query_seq=db.query_seq')
    for result in cursor:
        print(result)
    cursor.close()

# Posible variable virus_type a elegir valor entre {"DNA","RNA"}     
def query11(conection):
    cursor = conection.cursor()
    cursor.execute('SELECT v.name_v, g.molecule_type, v.virus_type, v.shape FROM virus v JOIN genome g WHERE INSTR(v.virus_type,"DNA") > 0 AND g.genome_id = v.genome_id')
    for result in cursor:
        print(result)
    cursor.close()
    
def query12(conection):
    cursor = conection.cursor()
    cursor.execute('SELECT hn.query_name, hn.virus_id, v.virus_type, v.shape FROM hitName hn JOIN virus v WHERE hn.virus_id=v.virus_id')
    for result in cursor:
        print(result)
    cursor.close()

# Posible variable realm a elegir valor entre {"Duplodnaviria", "Varidnaviria", "Pokkesviricetes", "Riboviria", "Monodnaviria"}     
def query13(conection):
    cursor = conection.cursor()
    cursor.execute('SELECT * FROM virus WHERE taxonomy_id IN (SELECT taxonomy_id FROM taxonomy WHERE realm="Riboviria"')
    for result in cursor:
        print(result)
    cursor.close()

# Posible variable molecule_type a elegir valor entre {"DNA","RNA"}     
def query14(conection):
    cursor = conection.cursor()
    cursor.execute('SELECT * FROM gene WHERE genome_id IN (SELECT genome_id FROM genome WHERE molecule_type="RNA")')
    for result in cursor:
        print(result)
    cursor.close()

# Posible variable length_nt_seq  
def query15(conection):
    cursor = conection.cursor()
    cursor.execute('SELECT * FROM hitSeq WHERE gene_id IN (SELECT gene_id FROM gene WHERE length(nt_seq) >= 430 AND length(nt_seq) <= 460)')
    for result in cursor:
        print(result)
    cursor.close()

# Posible variable name_v a elegir valor entre {"Adenovirus","Arbovirus (encephalitis)", "Arenaviridae","Baculoviridae", "LCM-Lassa viral complexes", "Tacaribe viral complexes", "Cytomegalovirus",  
# "Flavivirus amaril (Yellow fever)", "Flu A","H1N2 for pigs and humans", "H2N2 (Asian flu)", "H3N2 (Hong Kong Flu 1968)", "H5N1 (07-08 pandemic)", "H7N7", "Hantaan", "Hepatitis A virus", 
# "Herpes simplex", "Herpes simplex Type 1", "Herpes simplex Type 2", "Human Herpesvirus 7", "Human Herpesvirus 8 (VHH-8)", "Herpesvirus simiae (B virus)", "Herpesvirus varicella-zoster", 
# "Megavirus chilensis", "Mixovirus Parotiditis (Mumps)", "Papillomaviridae (Papillomas)", "Papovavirus (Human Papilloma)", "Paramyxoviridae", "Parotiditis (Mumps)", "Canine Parvovirus", 
# "Human Parvovirus (B 19)", "Picornaviridae", "Poliovirus (Poliomyelitis)", "Poxvirus", "Rinovirus", "Rotavirus", "SARS", "SARS COV-2","Variola virus (Smallpox)", "VIH", "Belgrade Virus", 
# "Bhanja Virus", "BK & JC Virus", "Bunyamwera Virus", "Coxsackie Virus", "Epstein-Barr Virus", "Hemorrhagic conjunctivitis virus (AHC)", "Lymphocytic choriomeningitis virus (other strains)", 
# "Lymphocytic choriomeningitis virus (neurotropic strains)", "California encephalitis virus", "Newcastle disease virus", "Influenza virus type A", "Influenza virus type B", "Influenza virus type C",  
# "Hepatitis A virus (human enterovirus type 72)", "Parainfluenza virus type 1", "Varicella Zoster Virus (Varicella)", "Mumps virus", "Adeno-associated virus", "Aichi virus", "Australian bat lyssavirus",
# "Fatal encephalitis", "Banna virus", "Barmah forest virus", "Bunyamwera virus", "Bunyavirus La Crosse", "Bunyavirus snowshoe hare", "Cercopithecine herpesvirus", "Chandipura virus", "Chikungunya virus",
# "Cosavirus A", "Cowpox virus", "Coxsackievirus", "Crimean-Congo hemorrhagic fever virus", "Dengue virus", "Dhori virus", "Dugbe virus", "Duvenhage virus", "Eastern equine encephalitis virus",
# "Ebolavirus", "Echovirus", "European bat lyssavirus", "Hantaan virus", "Hendra virus", "Hepatitis E virus", "Hepatitis B virus", "Hepatitis C virus", "Hepatitis Delta virus", "Horsepox virus",
# "Human adenovirus", "Human astrovirus", "Human coronavirus", "Human cytomegalovirus", "Human enterovirus", "Japanese encephalitis virus", "Lagos bat virus", "Louping ill virus", "Mayaro virus",
# "Norwalk virus", "Sagiyama virus"}    
def query16(conection):
    cursor = conection.cursor()
    cursor.execute('SELECT * FROM taxonomy WHERE taxonomy_id = (SELECT t.taxonomy_id FROM taxonomy t JOIN virus v WHERE t.taxonomy_id = v.taxonomy_id AND v.name_v="Dengue virus")')
    for result in cursor:
        print(result)
    cursor.close()

# Posible variable shape a elegir valor entre {"Helical", "Icosahedral", "Envelope", "Complex"}    
def query17(conection):
    cursor = conection.cursor()
    cursor.execute('SELECT * FROM genome WHERE genome_id IN (SELECT v.genome_id FROM virus v JOIN genome g WHERE g.genome_id=v.genome_id AND v.shape="Helical") ORDER BY genome_id')
    for result in cursor:
        print(result)
    cursor.close()
 
# Posible variable sequence a elegir un combinado de las letras {A, C, G, T}
def query18(conection):
    cursor = conection.cursor()
    cursor.execute('SELECT * FROM genome WHERE genome_id IN (SELECT G.genome_id FROM genome G JOIN gene g WHERE G.genome_id = g.genome_id AND INSTR(g.nt_seq,"AGCUCAUG") > 0)')
    for result in cursor:
        print(result)
    cursor.close()
    
def query19(conection):
    cursor = conection.cursor()
    cursor.execute('SELECT genome_id, COUNT(*) "Total Genes" FROM gene WHERE genome_id%2=1 GROUP BY genome_id')
    for result in cursor:
        print(result)
    cursor.close()

# Posible variable family a elegir valor entre {"Alloherpesviridae", "Herpesviridae", "Malacoherpesviridae", "Ackermannviridae", "Autographiviridae", "Chaseviridae", "Demerecviridae", "Drexlerviridae", 
# "Herelleviridae", "Myoviridae", "Podoviridae", "Siphoviridae", "Mimiviridae", "Phycodnaviridae", "Pandoraviridae", "Ascoviridae", "Iridoviridae", "Marseilleviridae", "Pithoviridae", "Mininucleoviridae",
# "Asfarviridae", "Poxviridae", "Medusaviridae", "Lavidaviridae", "Adenoviridae", "Corticoviridae", "Tectiviridae", "Turriviridae", "Finnlakeviridae", "Autolykiviridae", "Sphaerolipoviridae", "Portogloboviridae"}     
def query20(conection):
    cursor = conection.cursor()
    cursor.execute('SELECT v.virus_id, v.name_v, v.virus_type, v.shape, v.year_origin, t.family FROM virus v JOIN (SELECT taxonomy_id, family FROM taxonomy WHERE family="Podoviridae") AS t ON v.taxonomy_id = t.taxonomy_id ORDER BY v.virus_id')
    for result in cursor:
        print(result)
    cursor.close()
    
print()
print('1. Insert data.')
# Aún por ver el punto 2...
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
                
                insertnewgenome(molecule_type, descript)
                
            elif insertoption == 2:
                
                genome_id = input('Genome ID: ')
                nt_seq = input('Nucleotide sequence: ')
                descript = input('Description: ')
                
                insertnewgene(genome_id, nt_seq, descript)
                
            elif insertoption == 3:
                
                family = input('Family: ')
                order_v = input('Order: ')
                class_v = input('Class: ')
                phylum = input('Phylum: ')
                kingdom = input('Kingdom: ')
                realm = input('Realm: ')    
                
                insertnewtaxonomy(family, order_v, class_v, phylum, kingdom, realm)               
                
            elif insertoption == 4:
                
                name_v = input('Virus name: ')
                genome_id = input('Genome ID: ')
                taxonomy_id = input('Taxonomy ID: ')
                virus_type = input('Virus type: ')
                shape = input('Shape: ')
                year_origin = input('Origin year: ')
                
                insertnewvirus(name_v, genome_id, taxonomy_id, virus_type, shape, year_origin)
            
            elif insertoption == 5:
                
                option = input('Is it a sequence query (sq) or a name query (nq)? Write sq or nq: ')
                if option == 'sq':
                    query_seq = input('Query sequence: ')
                    query_name = ''
                    query_message = input('Query message: ')
                    insertnewdb_query(query_seq, query_name, query_message)
                elif option == 'nq':
                    query_seq = ''
                    query_name = input('Query name: ')
                    query_message = input('Query message: ')
                    insertnewdb_query(query_seq, query_name, query_message)
                else:
                    print('Error, option not recognized.')
                    
                
            elif insertoption == 6:
                
                query_seq = input('Query sequence: ')
                hit_index = input('Hit index: ')
                hit_seq = input('Hit sequence: ')
                name_v = input('Virus Name: ')	
                gene_id = input('Gene ID: ')
                
                insertnewhitSeq(query_seq, hit_index, hit_seq, name_v, gene_id)
                
            elif insertoption == 7:
                
                query_name = input('Query name: ')
                virus_id = input('Virus ID: ')
                
                insertnewhitName(query_name, virus_id)
                
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
        
        print()
        
    elif mainoption == 3:
        
        print('Available queries: ')
        print('1. ')
        print('2. ')
        print('3. ')
        print('4. ')
        print('5. ')
        print('6. ')
        print('7. ')
        print('8. ')
        print('9. ')
        print('10. ')
        print('11. ')
        print('12. ')
        print('13. ')
        print('14. ')
        print('15. ')
        print('16. ')
        print('17. ')
        print('18. ')
        print('19. ')
        print('20. ')
        
        queryoption = int(input('What query do you want to make? '))  
        print()
        
        
conection.close()
           
