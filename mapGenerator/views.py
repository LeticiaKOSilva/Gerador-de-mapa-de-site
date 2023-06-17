from django.shortcuts import render
from .link_functions import get_links
# from .clusterization import clusterize
from django.http import JsonResponse

# import xml.etree.ElementTree as ET
import json

def index(request):
    TEMPLATE_NAME = 'mapGenerator/index.html'
    return render(request,TEMPLATE_NAME)


def result(request, url=''):
    if request.method == 'POST':
        # Retrieve the JSON data from the request
        json_data = json.loads(request.body)

        # Access the JSON data
        url = json_data.get('url')

        # Get the links
        links = get_links(url)

        # Convert links to a list of dictionaries
        if links is not None:
            links_data = [link.to_dict() for link in links]
            valid = True
        else:
            links_data = None
            valid = False
        print(valid)
        # Prepare the response
        response_data = {
            'valid': valid,
            'links': links_data
        }

        return JsonResponse(response_data)

    # Handle other HTTP methods or invalid requests
    return JsonResponse({'error': 'Invalid request'}, status=400)


def download_xml(request):
    '''
    Função responsável por gerar um arquivo XML com o mapa do site.
    '''
    if request.method == 'POST':
        # Retrieve the JSON data from the request
        json_data = json.loads(request.body)

        # Access the JSON data
        teste = json_data.get('url')
        print(teste)

        # Process the JSON data
        # ...

        # Prepare the response
        response_data = {
            'message': 'Data received and processed successfully!',
            # ...
        }

        return JsonResponse(response_data)

    # Handle other HTTP methods or invalid requests
    return JsonResponse({'error': 'Invalid request'}, status=400)