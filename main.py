from mapGenerator.teste_pag_rank import *
from mapGenerator.views import *
import networkx as nx

class Rank:
    def __init__(self, url, pontuacao):
        self.url = url
        self.pontuacao = pontuacao

    def __str__(self):
        return f'{self.url} = {self.pontuacao}'


def get_rank(o : Rank):
    return o.pontuacao

if __name__ == '__main__':
        # Criando um grafo vazio
    grafo = nx.DiGraph()

    # Obtendo a lista de links de uma página
    links =  extract_urls(get_links('youtube.com'))  

    # Adicionando os nós ao grafo
    grafo.add_nodes_from(links)

    # Adicionando as arestas (links entre URLs)
    for link in links:
        links2 = get_links(link)
        if links2:
            arestas = extract_urls(links2)  # Obtém os links da página atual
            for aresta in arestas:
                grafo.add_edge(link, aresta)

    # Calculando o PageRank
    resultado = nx.pagerank(grafo)

    ranks = []

    # Imprimindo as pontuações PageRank
    for url, pontuacao in resultado.items():
        ranks.append(Rank(url,pontuacao))
        #print(f"URL: {url}, Pontuação PageRank: {pontuacao}")   
    
    ranks.sort(key=get_rank)
    for rank in ranks:
        print(rank)