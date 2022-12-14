# -*- coding: utf-8 -*-
"""Task05.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16PltqMyOgfpKfe7IlV4oZCOnN1_EOwhW

**Task 05: Reading and writing ontologies**
"""

!pip install rdflib 
!pip install owlrl
github_storage = "https://raw.githubusercontent.com/AndreaCimminoArriaga/LinkedData/main/rdfslib/"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal,RDFS
g = Graph()
g.namespace_manager.bind('vcard-rdf',Namespace("http://www.w3.org/2001/vcard-rdf/3.0/"),override=False)
g.parse(github_storage+"/resources/example4.rdf", format="xml")

"""Ahora podemos obtener algunas de las triples de RDFS (el modelo, no los datos)"""

print("Show al the RDFS Class of the model")
for s,p,o in g.triples((None, None, RDFS.Class)):
  print(s,p,o)

print("\n\nShow al the properties where RDFS range is defined in the model")
for s,p,o in g.triples((None, RDFS.range, None)):
  print(s,p,o)

print("\n\nShow al the subClassOf reltaions of the model")
for s,p,o in g.triples((None, RDFS.subClassOf, None)):
  print(s,p,o)

"""Se muestra ahora todo el grafo, las instancias y las tripletas RDFS"""

for s,p,o in g:
  print(s,p,o)