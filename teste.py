import mapGenerator.link_functions as lf
from mapGenerator.clusterization import clusterize
import asyncio
linksList = lf.get_links('https://www.ifsudestemg.edu.br/barbacena')

# for link in linksList:
#     print(link)

asyncio.run(clusterize(linksList))

