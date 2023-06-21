import mapGenerator.link_functions as lf
from mapGenerator.clusterization import clusterize
linksList = lf.get_links('barbacenaonline.com.br')

for link in linksList:
    print(link)

clusterize(linksList)

