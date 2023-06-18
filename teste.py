from mapGenerator.link_functions import get_links
from mapGenerator.clusterization import clusterize
linksList = get_links('barbacenaonline.com.br')

# for link in linksList:
#     print(link)

clusterize(linksList)
