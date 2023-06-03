
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
from .link_functions import extract_urls
from .text_html_functions import *


def clusterize(links):
#
    urls = extract_urls(links)
    contents = [f'{link.url} {normalize_content_for_cluterize(link.conteudo)}' for link in links]
    # Pré-processamento dos links (remoção de prefixos, etc.)

    # Representação dos dados usando TF-IDF
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(contents)

    # Normalização dos vetores de recurso
    X = normalize(X)

    # Aplicação do algoritmo K-means
    k = 5  # número de clusters
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)

    # Obtendo os rótulos dos clusters
    labels = kmeans.labels_

    # Criando dicionário para armazenar os links por tópicos
    topics = {i: [] for i in range(k)}

    # Agrupando os links em seus respectivos tópicos
    for i, link in enumerate(links):
        topics[labels[i]].append(link.title)

    # Imprimindo os links por tópicos
    for topic, links in topics.items():
        print(f"Tópico {topic+1}:")
        for link in links:
            print(link)
        print()

def normalize_content_for_cluterize(content: str):
    soup = BeautifulSoup(content,"html.parser")

    title_tags = get_title_tags(soup)
    
    normalized_text = " "

    normalized_text.join(title_tags)
    if(normalized_text == " "):
        return ""

    return normalized_text