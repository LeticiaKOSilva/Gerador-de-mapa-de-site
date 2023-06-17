from tokenize import String
import requests
from bs4 import BeautifulSoup
from collections import defaultdict
from .models import Link
##
#
def get_links(url): #
    # Padroniza a URL.
    print(url)
    url = standardize_url(url)
    print(url)

    # Cria a requisição.
    response = create_request(url)

    if not response: 
        return None

    # Extrai os links da página.
    links = create_links_list(url, BeautifulSoup(response.content, 'html.parser'))

    if not links: 
        return None

    return links
# get_links()

def create_request(url, ssl_cert=True): #
    """
    Cria uma requisição e retorna a resposta.
    Tenta criar uma requisição efetuando a verificação dos certificados SSL, 
    caso não consiga cria ignorando a verificação.
    """
    try:
        return requests.get(url)
    except (requests.exceptions.SSLError):
        return requests.get(url, verify=False)
    except (requests.exceptions.ConnectionError): # Tratamento caso a página não exista.
        return None
    except (requests.exceptions.MissingSchema): # Caso a url esteja em formato inválido
        return None
    except (requests.exceptions.InvalidSchema): # Caso a url esteja em formato inválido
        return None
#


# Extrai os links da página.
def create_links_list(url: String, soup: BeautifulSoup): #
    links = []
    for link_tag in soup.find_all('a'):
        link_href = link_tag.get('href')
        
        if(link_href):
            treated_link = treatLink(url,link_href)
       
            if link_href:
                links.append(
                   Link(link_tag.text, treated_link, "") #get_content(treated_link))
                )
      
    return links
#

## Padroniza a URL recebida pela API.
def standardize_url(url: String): #
    if not url.startswith("https://") and not url.startswith("http://"):
        url = "https://" + url  # Adiciona "https://" por padrão

    parsed_url = url.split("//")
    domain = parsed_url[1] if len(parsed_url) > 1 else parsed_url[0]

    if not domain.startswith("www."):
        url = url.replace(domain, "www." + domain)

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

def extract_urls(links: list[Link]):
    urls = []
    for link in links:
        urls.append(link.url)
    return urls

def get_content(url: String):
    """
    Recebe uma url e retorna todo o HTML contido nela 
    ou String vazia caso a requisição não seja bem sucedida
    """
    response = create_request(url)
    if(response is None):
        return ""
    return response.text

def remove_url_prefix(url: str):
    """
    Remove a parte inicial de uma url e retorna a url sem esse 
    inicio ou string vazia caso não consiga realizar o split
    Ex: url = https://github.com/login/, return url = login/
    
    """
    parts = url.split('.com')
    return parts[1] if len(parts) > 1 else ""
#

def get_links_sorted_by_occurrence(url: str):
    '''
    Obtém uma lista de links ordenados pela sua 
    ocorrência na página em ordem decrescente.
    '''
    return sort_links_by_occurrence(get_links(url))

def sort_links_by_occurrence(links):
    '''
    Ordena uma lista de links baseando-se no número de ocorrências na própria lista.
    '''
    dictionary = defaultdict(int)
    
    # Contagem das ocorrências dos links
    for link in links:
        dictionary[link] += 1
    
    # Ordenação decrescente por contagem de ocorrência
    links_count = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    
    return links_count