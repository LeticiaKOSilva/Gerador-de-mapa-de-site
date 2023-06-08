import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def extrair_links_e_textos(url):
    # Faz a requisição HTTP para obter o conteúdo da página
    response = requests.get(url, verify=False)  # Adicionei o parâmetro verify=False para ignorar a verificação de certificado
    conteudo = response.content

    # Cria um objeto BeautifulSoup para fazer a análise do HTML
    soup = BeautifulSoup(conteudo, 'html.parser')

    # Encontra todas as tags <a> que contêm links
    tags_a = soup.find_all('a')

    # Itera sobre as tags encontradas e extrai os links e textos
    for tag in tags_a:
        if tag.has_attr('href'):
            link = tag['href']
            texto = tag.text
            print(f"Link: {link}")
            print(f"Texto: {texto}")
            print()

# Exemplo de uso
url = 'https://www.ifsudestemg.edu.br/barbacena'
extrair_links_e_textos(url)

