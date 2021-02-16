#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 16:57:30 2021

@author: ozias
"""
#Pandas pour importer les données depuis le fichier csv
import pandas as pd

#Lecture desdonnées du fichier data.csv
df = pd.read_csv('csv_files/energiejeu8.csv', delimiter=';')

fichier_rdf = open("rdf_files/nbaer.txt", "a")

df_X = df.iloc[:, :].values
annees = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]

for i in range(0, df_X.shape[0],1) :
    for j in range(1, len(annees)+1, 1):
        var_name = df_X[i,0].replace(' ', '') +''+str(annees[j-1])        
        var_comment = '\n \n###  http://www.semanticweb.org/ozias/pnpdo/PuisanceEngRegion#'+ var_name +''
        var_obj_nba = '\n:'+ var_name +' rdf:type owl:NamedIndividual ,\n \t               :Puissance ;'    
        var_aPourAnnee = '\n\t:aPourAnnee <http://www.semanticweb.org/ozias/pnpdo/PuisanceEngRegion#'+ str(annees[j-1]) +'> ;'
        var_aPourRegion = '\n\t:aPourRegion :<http://www.semanticweb.org/ozias/pnpdo/PuisanceEngRegion#'+ df_X[i, 0].replace(' ', '') + ' ;'

        var_puissance_en_mw = '\n\t:PuissanceEnMW '+ str(df_X[i, j]) +' ;'
        var_label = '\n\t rdfs:label "'+ var_name +'"@fr .'
    
        fichier_rdf.write(var_comment)
        fichier_rdf.write(var_obj_nba)
        fichier_rdf.write(var_aPourAnnee)
        fichier_rdf.write(var_aPourRegion)
        fichier_rdf.write(var_puissance_en_mw)
        fichier_rdf.write(var_label)
      
fichier_rdf.close()