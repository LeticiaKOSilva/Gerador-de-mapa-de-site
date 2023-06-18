import matplotlib.pyplot as plt
from .models import Link
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
from sklearn.metrics import silhouette_score
from .text_html_functions import *
from string import punctuation

def get_best_silhouette_score(X,start_range,end_range):
    range_clusters = range(start_range, end_range)
    silhouette_scores = []

    for num_clusters in range_clusters:
        kmeans = KMeans(n_clusters=num_clusters, n_init=10)
        kmeans.fit(X)
        labels = kmeans.labels_
        score = silhouette_score(X, labels)
        silhouette_scores.append(score)
    return range_clusters[silhouette_scores.index(max(silhouette_scores))]

def clusterize(links: list[Link]):
#   
    MIN_CLUSTERS = 2
    MAX_CLUSTERS = 12

    # Filtrar links vazios
    links = list(filter(lambda text: text.url.strip(), links))

    # Normalizar conteúdo dos links
    contents = [normalize_content_for_cluterize(link.conteudo) for link in links]

    # Vetorizar os dados usando TF-IDF
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(contents)

    # Normalizar os dados
    X = normalize(X)

    # Encontrar o melhor número de clusters usando a pontuação de silhueta
    best_num_clusters = None
    best_silhouette_score = -1
    for num_clusters in range(MIN_CLUSTERS, MAX_CLUSTERS+1):
        kmeans = KMeans(n_clusters=num_clusters, n_init=10)
        kmeans.fit(X)
        labels = kmeans.labels_
        silhouette_avg = silhouette_score(X, labels)
        if silhouette_avg > best_silhouette_score:
            best_silhouette_score = silhouette_avg
            best_num_clusters = num_clusters

    # Executar o KMeans com o melhor número de clusters
    kmeans = KMeans(n_clusters=best_num_clusters, n_init=10)
    kmeans.fit(X)
    labels = kmeans.labels_

   
    pca = PCA(n_components=2)
    reduced_X = pca.fit_transform(X.toarray())

    # Obter as coordenadas dos pontos dos clusters
    cluster_points = {i: [] for i in range(best_num_clusters)}
    for i, point in enumerate(reduced_X):
        cluster_points[labels[i]].append(point)

    # Plotar os pontos dos clusters
    colors = colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'purple', 'orange', 'gray', 'pink', 'brown', 'teal', 'navy', 'olive']
    for cluster_label, points in cluster_points.items():
        x = [point[0] for point in points]
        y = [point[1] for point in points]
        plt.scatter(x, y, c=colors[cluster_label], label=f'Cluster {cluster_label+1}')

    all_points = [x,y]

    
    plt.xlabel('Componente Principal 1')
    plt.ylabel('Componente Principal 2')
    plt.title('Clusters no Plano Cartesiano')
    plt.show()

    # Retornar os tópicos dos clusters
    topics = {i: [] for i in range(best_num_clusters)}
    for i, link in enumerate(links):
        titulo = link.title if link.title.strip() != '' else link.url
        topics[labels[i]].append(titulo)

    return topics,all_points
    # Imprimindo os links por tópicos
    # for topic, links in topics.items():
    #     print(f"Tópico {topic+1}:")
    #     for link in links:
    #         print(link)
    #     print()
#
def normalize_content_for_cluterize(content: str):
    soup = BeautifulSoup(content,"html.parser")

    title_tags = get_all_tag_names(soup)
    
    #print(title_tags)
    normalized_text = " ".join(title_tags)
    #print(normalized_text)
    if(normalized_text.strip() == ""):
        return ""

    return normalized_text

def remove_punctuation(text: str):
    translate_table = str.maketrans("", "", punctuation)
    
    # Aplica a tradução para remover as pontuações
    text_without_punctuation = text.translate(translate_table)
    
    return text_without_punctuation