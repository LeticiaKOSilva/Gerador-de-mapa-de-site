from django.shortcuts import render
from .link_functions import get_links
from .clusterization import clusterize
from django.http import HttpResponse

import xml.etree.ElementTree as ET
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


def download_xml(request, url=''):
    '''
    Função responsável por gerar um arquivo XML com o mapa do site.
    '''
    root = ET.Element("root")
    child = ET.SubElement(root, "child")
    child.text = "Conteúdo do XML"
    tree = ET.ElementTree(root)

    response = HttpResponse(content_type='application/xml')
    response['Content-Disposition'] = 'attachment; filename="arquivo.xml"'

    # Salva o arquivo XML na resposta (response)
    tree.write(response, encoding='utf-8', xml_declaration=True)

    return response