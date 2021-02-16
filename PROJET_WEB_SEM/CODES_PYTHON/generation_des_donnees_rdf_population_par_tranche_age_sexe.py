

import pandas as pd
df = pd.DataFrame()

nombreMascunin =''
nombreFeminin =''
annee=''
sexe=''
tranche=''
valeur1=0
valeur2=0
i = 0
data = pd.read_csv('populationpartrancheagesexe20082017.csv', delimiter=',')


file = open('test.txt', 'a') 
tab = []
for index, row in data.iterrows():
    print(row[0], row[1], row[2], row[3])
    tranche = row[0]
    tranche = tranche.replace(" ", "_")
    annee = str(row[1])
    sexeM = str(row[2])
    sexeF = str(row[3])
    masculin = '\n<owl:NamedIndividual rdf:about="http://www.semanticweb.org/abou/pnpdo/populationParTrancheAge#nombreMasculin_'+ str(i) +'">\n'+'\t<rdf:type rdf:resource="http://www.semanticweb.org/abou/pnpdo/populationParTrancheAge#NombreDePersonne"/>\n'+'\t<WebSem:aPourAnnee rdf:resource="http://www.semanticweb.org/abou/pnpdo/populationParTrancheAge#'+ annee +'"/>\n'+'\t<WebSem:aPourSexe rdf:resource="http://www.semanticweb.org/abou/pnpdo/populationParTrancheAge#Masculin"/>\n'+'\t<WebSem:aPourTranche rdf:resource="http://www.semanticweb.org/abou/pnpdo/populationParTrancheAge#'+ tranche +'"/>\n'+'\t<WebSem:nombrePersonne rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">'+ sexeM +'</WebSem:nombrePersonne>\n'+'</owl:NamedIndividual>'
    feminin = '\n<owl:NamedIndividual rdf:about="http://www.semanticweb.org/abou/pnpdo/populationParTrancheAge#nombreFeminin_'+ str(i) +'">\n'+'\t<rdf:type rdf:resource="http://www.semanticweb.org/abou/pnpdo/populationParTrancheAge#NombreDePersonne"/>\n'+'\t<WebSem:aPourAnnee rdf:resource="http://www.semanticweb.org/abou/pnpdo/populationParTrancheAge#'+ annee +'"/>\n'+'\t<WebSem:aPourSexe rdf:resource="http://www.semanticweb.org/abou/pnpdo/populationParTrancheAge#Feminin"/>\n'+'\t<WebSem:aPourTranche rdf:resource="http://www.semanticweb.org/abou/pnpdo/populationParTrancheAge#'+ tranche +'"/>\n'+'\t<WebSem:nombrePersonne rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">'+ sexeF +'</WebSem:nombrePersonne>\n'+'</owl:NamedIndividual>'
    i = i+1
    file.write(masculin)
    file.write(feminin)
    
file.close()
