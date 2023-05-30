from tokenize import String
import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse, HttpRequest
from .models import Link
##
#
def get_links(url): #

    url = standardize_url(url)

    # Realiza o web scraping da página
    response = create_request(url)

    # Extrai os links da página
    links = create_links_list(url, BeautifulSoup(response.content, 'html.parser'))
    
    if not links: 
        return None
    
    return links
# get_links()


# Cria uma requisição e retorna a resposta.
# Tenta criar uma requisição efetuando a verificação dos certificados SSL, 
# caso não consiga cria ignorando a verificação.
def create_request(url, ssl_cert=True): #
    try:
        return requests.get(url)
    except (requests.exceptions.SSLError):
        return requests.get(url, verify=False)
#


# Extrai os links da página.
def create_links_list(url: String, soup: BeautifulSoup): #
    links = []
    for link_tag in soup.find_all('a'):
        link_href = link_tag.get('href')
        
        if link_href:
            links.append(
                Link(link_tag.text,treatLink(url,link_href))
            )

    return links
#

## Padroniza a URL recebida pela API.
def standardize_url(url: String): #
    # A url deve iniciar com 'https://' ou 'http://'
    if (not url.startswith("https://") and not url.startswith("http://")):
        return f"https://{url}"

    return url
#


## Trata o link de referência local da página. (ex.: '/favoritos')
# Retorna um link válido. (ex.: 'https://seusite.com/favoritos')
def treatLink(url_page: String, link: String): #
    if link.startswith("/"):
        return f"{url_page}{link}"
    if link.startswith("#"):
        return url_page
    
    return link
#

def extract_urls(links):
    urls = []
    for link in links:
        urls.append(link.url)
    return urls


