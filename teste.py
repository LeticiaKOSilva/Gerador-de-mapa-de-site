from mapGenerator.link_functions import get_links
from mapGenerator.clusterization import clusterize
linksList = get_links('facebook.com')

#for link in linksList:
#     print(link)

clusterize(linksList)
