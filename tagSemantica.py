import requests
from bs4 import BeautifulSoup
import re

def extrair_links(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Não foi possível acessar a página {url}. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')

    grupos_por_tag = []

    for link in links:
        href = link.get('href')
        if href and not href.startswith('#') and re.search(r'\.com', href):
            link_text = link.text.strip()
            if not link_text:
                link_text = "Sem Título"
            parent_tag = link.parent.name

            encontrado = False
            for grupo in grupos_por_tag:
                if grupo['tag'] == parent_tag:
                    grupo['links'].append({'link': href, 'texto': link_text})
                    encontrado = True
                    break

            if not encontrado:
                grupos_por_tag.append({'tag': parent_tag, 'links': [{'link': href, 'texto': link_text}]})

    for grupo in grupos_por_tag:
        print(f"Tag semântica: {grupo['tag']}")
        for link in grupo['links']:
            print(f"Link: {link['link']}")
            print(f"Texto do link: {link['texto']}")
        print("-" * 50)

url = "https://www.beecrowd.com.br/judge/en/login?redirect=%2Fen%2Fproblems%2Fview%2F2115"
extrair_links(url)

#Sites testados
#https://www.youtube.com/
#https://www.ifsudestemg.edu.br/barbacena
#https://www.ifsudestemg.edu.br