# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 20:55:30 2021

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


family = ["Alloherpesviridae", "Herpesviridae", "Malacoherpesviridae", "Ackermannviridae",
          "Autographiviridae", "Chaseviridae", "Demerecviridae", "Drexlerviridae", 
          "Herelleviridae", "Myoviridae", "Podoviridae", "Siphoviridae", "Mimiviridae",
          "Phycodnaviridae", "Pandoraviridae", "Ascoviridae", "Iridoviridae", "Marseilleviridae",
          "Pithoviridae", "Mininucleoviridae", "Asfarviridae", "Poxviridae", "Medusaviridae",
          "Lavidaviridae", "Adenoviridae", "Corticoviridae", "Tectiviridae", "Turriviridae",
          "Finnlakeviridae", "Autolykiviridae", "Sphaerolipoviridae", "Portogloboviridae"]
order = ["Herpesvirales", "Caudovirales", "Algavirales", "Pimascovirales", "Ghabrivirales",
         "Mononegavirales", "Bunyavirales", "Articulavirales", "Nodamuvirales", "Tolivirales",
         "Hepelivirales", "Martellivirales", "Tymovirales", "Nidovirales", "Picornavirales",
         "Sobelivirales", "Durnavirales", "Ortervirales"]
class_v = ["Megaviricetes", "Pokkesviricetes", "Tectiliviricetes", "Pisoniviricetes", 
           "Stelpaviricetes", "Alsuviricetes", "Insthoviricetes"]
phylum = ["Nucleocytoviricota", "Preplasmaviricota", "Duplornaviricota", "Negarnaviricota",
          "Lenarviricota", "Kitrinoviricota", "Pisuviricota"]
kingdom = ["Heunggongvirae", "Bamfordvirae", "Helvetiavirae", "Orthornavirae", "Pararnavirae",
           "Loebvirae", "Sangervirae", "Trapavirae", "Shotokuvirae"] 
realm = ["Duplodnaviria", "Varidnaviria", "Pokkesviricetes", "Riboviria", "Monodnaviria"]

def taxonomy(cursor, family, order, class_v, phylum, kingdom, realm):
    
    try:  
        
        sql = "INSERT INTO taxonomy (family, order_v, class, phylum, kingdom, realm) VALUES ('" + random.choice(family) + "','" + random.choice(order) + "','" + random.choice(class_v) + "','" + random.choice(phylum) + "','" + random.choice(kingdom) + "','" + random.choice(realm) + "')"
        
        print(sql)
          
        cursor.execute(sql) 
        
        connection.commit()
        
    except:
        
        print("Query error ...")
            
    return cursor

cursor = connection.cursor()

for i in range(100): 
    
    taxonomy(cursor, family, order, class_v, phylum, kingdom, realm)
    
connection.close()



