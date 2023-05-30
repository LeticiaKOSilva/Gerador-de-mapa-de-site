import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
from .views import extract_urls

def clusterize(links):
    links = extract_urls(links)
    # Pré-processamento dos links (remoção de prefixos, etc.)
    processed_links = [link.replace("https://www.ted.com/", "") for link in links]

    # Representação dos dados usando TF-IDF
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(processed_links)

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
        topics[labels[i]].append(link)
        print("obtido = ",link)

    # Imprimindo os links por tópicos
    for topic, links in topics.items():
        print(f"Tópico {topic+1}:")
        for link in links:
            print(link)
        print()
