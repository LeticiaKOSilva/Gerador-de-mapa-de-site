from mapGenerator.views import get_links
from mapGenerator.clusterization import clusterize
linksList = get_links('youtube.com')

clusterize(linksList)

