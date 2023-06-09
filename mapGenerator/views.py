from django.shortcuts import render
from .link_functions import get_links
from .clusterization import clusterize
import json
def index(request):
    TEMPLATE_NAME = 'mapGenerator/site.html'
    return render(request,TEMPLATE_NAME)


def resultPage(request, url=''):
    TEMPLATE_NAME = 'mapGenerator/result.html'
    clusters = clusterize(get_links(url))
    clusters_json = json.dumps(clusters)
    # print(clusters_json)
    return render(request,TEMPLATE_NAME,{'clusters_json' : clusters_json,})  
