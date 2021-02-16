 
import pandas as pd

data = pd.read_csv('productiondeaudeloneaparregion.csv', delimiter=';')

annee = [2001,2002,2003,2004,2005,2006,2010,2011,2014,2015]

file = open('test.txt', 'a') 

for index, row in data.iterrows():
    print(row[10])
    region = row[0]
    region = region.replace(" ", "_")
    i = 1
    for an in annee:
        chaine = '\n<owl:NamedIndividual rdf:about="http://www.semanticweb.org/abou/pnpdo/ProductionEau#'+ region + str(an)+ str(i) +'">\n\t<rdf:type rdf:resource="http://www.semanticweb.org/abou/pnpdo/ProductionEau#Quantité"/>\n\t<aPourAnnee rdf:resource="http://www.semanticweb.org/abou/pnpdo/ProductionEau#'+str(an)+'"/>\n\t<aPourRegion rdf:resource="http://www.semanticweb.org/abou/pnpdo/ProductionEau#'+ region +'"/>\n\t<quantiteEau rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">'+ str(row[i]) +'</quantiteEau>\n</owl:NamedIndividual>\n'
        file.write(chaine)
        i = i+1
   

file.close()
    