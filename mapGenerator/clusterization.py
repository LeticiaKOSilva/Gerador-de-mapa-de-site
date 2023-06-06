from .models import Link
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
from .link_functions import remove_url_prefix
from sklearn.metrics import silhouette_score
from .text_html_functions import *
from string import punctuation


def clusterize(links: list[Link]):
#   
    links = list(filter(lambda text: text.url.strip(), links))

    contents = [normalize_content_for_cluterize(link.conteudo) for link in links]
    
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(contents)

    X = normalize(X)

    # Testar diferentes números de clusters
    range_clusters = range(2, 12)
    silhouette_scores = []

    for num_clusters in range_clusters:
        kmeans = KMeans(n_clusters=num_clusters, n_init=10)
        kmeans.fit(X)
        labels = kmeans.labels_
        score = silhouette_score(X, labels)
        silhouette_scores.append(score)

    best_num_clusters = range_clusters[silhouette_scores.index(max(silhouette_scores))]

    kmeans = KMeans(n_clusters=best_num_clusters, n_init=10)
    kmeans.fit(X)

    labels = kmeans.labels_

    topics = {i: [] for i in range(best_num_clusters)}

    for i, link in enumerate(links):
        titulo = link.title if link.title.strip() != '' else link.url
        topics[labels[i]].append(titulo)
    
    return topics
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