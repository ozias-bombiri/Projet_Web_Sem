#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 17:11:18 2021

@author: ozias
"""
#Pandas pour importer les données depuis le fichier csv
import pandas as pd

#Lecture desdonnées du fichier data.csv
df = pd.read_csv('csv_files/nombredabonnesenelectriciteparregion.csv', delimiter=';')

fichier_rdf = open("rdf_files/nbaer.txt", "a")

df_X = df.iloc[:, :].values

###  http://www.semanticweb.org/ozias/pnpdo/NbAbonElecRegion#BTNord2016
:BTNord2016 rdf:type owl:NamedIndividual ,
                     :BasseTension ,
                     :Tension ;
            :aPourAnnee <http://www.semanticweb.org/ozias/pnpdo/NbAbonElecRegion#2016> ;
            :aPourRegion :Nord ;
            :labelTypeTension "Basse Tension"^^rdfs:Literal ;
            :nombreAbonnes 23805 ;
            rdfs:label "BTNord2016"@fr .

for i in range(0, df_X.shape[0], 1) :
    var_name = 'BT'+df_X[i,0] +''+ str(df_X[i,1])
    var_comment = '\n\n###  http://www.semanticweb.org/ozias/pnpdo/NbAbonElecRegion#'+ var_name
    var_obj_nba = '\n:'+ var_name +' rdf:type owl:NamedIndividual , \n \t\t:BasseTension, \n \t\t:Tension ;'
    var_obj_type = '\n\t:labelTypeTension "Basse Tension"^^rdfs:Literal ;'

    var_aPourAnnee = '\n\t:aPourAnnee <http://www.semanticweb.org/ozias/pnpdo/NbAbonElecRegion#'+str(df_X[i, 1])+'> ;'
    var_aPourRegion = '\n\t:aPourRegion :'+ df_X[i, 0] +' ;'

    var_nombreAbonnes = '\n\t:nombreAbonnes '+ str(df_X[i, 2]) +' ;'
    var_label = '\n\t rdfs:label "'+ var_name +'"@fr .'
    
    fichier_rdf.write(var_comment)
    fichier_rdf.write(var_obj_nba)
    fichier_rdf.write(var_aPourAnnee)
    fichier_rdf.write(var_aPourRegion)
    fichier_rdf.write(var_obj_type)
    fichier_rdf.write(var_nombreAbonnes)
    fichier_rdf.write(var_label)
    
    var_name = 'HT'+df_X[i,0] +''+ str(df_X[i,1])
    var_comment = '\n\n###  http://www.semanticweb.org/ozias/pnpdo/NbAbonElecRegion#'+ var_name
    var_obj_nba = '\n:'+ var_name +' rdf:type owl:NamedIndividual , \n \t\t:HauteTension, \n \t\t:Tension ;'
    var_obj_type = '\n\t:labelTypeTension "Haute Tension"^^rdfs:Literal ;'
    var_nombreAbonnes = '\n\t:nombreAbonnes '+ str(df_X[i, 3]) +' ;'
    var_label = '\n\t rdfs:label "'+ var_name +'"@fr .'
    
    fichier_rdf.write(var_comment)
    fichier_rdf.write(var_obj_nba)
    fichier_rdf.write(var_aPourAnnee)
    fichier_rdf.write(var_aPourRegion)
    fichier_rdf.write(var_obj_type)
    fichier_rdf.write(var_nombreAbonnes)
    fichier_rdf.write(var_label)
    
    
    var_name = 'FDE'+df_X[i,0] +''+ str(df_X[i,1])
    var_comment = '\n\n###  http://www.semanticweb.org/ozias/pnpdo/NbAbonElecRegion#'+ var_name
    var_obj_nba = '\n:'+ var_name +' rdf:type owl:NamedIndividual , \n \t\t:AlimentationFDE, \n \t\t:Tension ;'
    var_obj_type = '\n\t:labelTypeTension "Alimentés par FDE"^^rdfs:Literal ;'
    var_nombreAbonnes = '\n\t:nombreAbonnes '+ str(df_X[i, 4]) +' ;'
    var_label = '\n\t rdfs:label "'+ var_name +'"@fr .'
    
    fichier_rdf.write(var_comment)
    fichier_rdf.write(var_obj_nba)
    fichier_rdf.write(var_aPourAnnee)
    fichier_rdf.write(var_aPourRegion)
    fichier_rdf.write(var_obj_type)
    fichier_rdf.write(var_nombreAbonnes)
    fichier_rdf.write(var_label)


      
fichier_rdf.close()
