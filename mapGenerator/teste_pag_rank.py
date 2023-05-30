from mapGenerator.networkXErrorException import NetworkXError
import networkx as nx

"""Créditos da função https://www.geeksforgeeks.org/page-rank-algorithm-implementation/"""
def pagerank(G, alpha=0.85, personalization=None,
			max_iter=100, tol=1.0e-6, nstart=None, weight='weight',
			dangling=None):
	"""Retorna o PageRank dos nós no grafo.

O PageRank calcula uma classificação dos nós no grafo G com base na estrutura dos links de entrada.
Foi originalmente projetado como um algoritmo para classificar páginas da web.

Parâmetros
G: grafo
Um grafo NetworkX. Grafos não direcionados serão convertidos em um grafo direcionado com duas arestas direcionadas 
para cada aresta não direcionada.


alpha: float, opcional
Parâmetro de amortecimento para o PageRank, padrão=0.85.

personalization: dict, opcional
O "vetor de personalização" consistindo em um dicionário com uma chave para cada nó do grafo e um valor de personalização
 não nulo para cada nó. Por padrão, é usada uma distribuição uniforme.

max_iter: inteiro, opcional
Número máximo de iterações no solucionador de autovalor do método de potência.

tol: float, opcional
Tolerância de erro usada para verificar a convergência no solucionador de método de potência.

nstart: dicionário, opcional
Valor inicial da iteração do PageRank para cada nó.

weight: chave, opcional
Chave dos dados da aresta a ser usada como peso. Se None, os pesos são definidos como 1.

dangling: dict, opcional
As arestas de saída a serem atribuídas a quaisquer nós "pendentes", ou seja, nós sem nenhuma aresta de saída.
A chave do dicionário é o nó para o qual a aresta de saída aponta e o valor do dicionário é o peso dessa aresta de saída. 
Por padrão, os nós pendentes recebem arestas de saída de acordo com o vetor de personalização (uniforme se não especificado). 
Isso deve ser selecionado para resultar em uma matriz de transição irreduzível (consulte as notas em google_matrix). 
É comum que o dicionário dangling seja o mesmo que o dicionário de personalização.

Retorna
pagerank: dicionário
Dicionário dos nós com o PageRank como valor.

Notas
O cálculo do autovetor é feito pelo método de iteração de potência e não há garantia de convergência. 
A iteração será interrompida após max_iter iterações ou quando uma tolerância de erro de number_of_nodes(G)*tol for atingida.

O algoritmo PageRank foi projetado para grafos direcionados, mas este algoritmo não verifica se o grafo de entrada é direcionado e 
será executado em grafos não direcionados, convertendo cada aresta do grafo direcionado em duas arestas.
"""
	if len(G) == 0:
		return {}

	if not G.is_directed():
		D = G.to_directed()
	else:
		D = G

	# Cria uma cópia na forma estocástica (à direita)
	W = nx.stochastic_graph(D, weight=weight)
	N = W.number_of_nodes()

	# Escolha o vetor inicial fixo se não for dado
	if nstart is None:
		x = dict.fromkeys(W, 1.0 / N)
	else:
		# Vetor nstart normalizado
		s = float(sum(nstart.values()))
		x = dict((k, v / s) for k, v in nstart.items())

	if personalization is None:

		# Atribuir vetor de personalização uniforme se não for fornecido
		p = dict.fromkeys(W, 1.0 / N)
	else:
		missing = set(G) - set(personalization)
		if missing:
			raise NetworkXError('Personalization dictionary '
								'must have a value for every node. '
								'Missing nodes %s' % missing)
		s = float(sum(personalization.values()))
		p = dict((k, v / s) for k, v in personalization.items())

	if dangling is None:

		# Use o vetor de personalização se o vetor oscilante não for especificado
		dangling_weights = p
	else:
		missing = set(G) - set(dangling)
		if missing:
			raise NetworkXError('Dangling node dictionary '
								'must have a value for every node. '
								'Missing nodes %s' % missing)
		s = float(sum(dangling.values()))
		dangling_weights = dict((k, v/s) for k, v in dangling.items())
	dangling_nodes = [n for n in W if W.out_degree(n, weight=weight) == 0.0]

	# power iteration: compõe até max_iter iterações
	for _ in range(max_iter):
		xlast = x
		x = dict.fromkeys(xlast.keys(), 0)
		danglesum = alpha * sum(xlast[n] for n in dangling_nodes)
		for n in x:

			# esta multiplicação de matriz parece estranha porque é
			# fazendo uma multiplicação à esquerda x^T=xlast^T*W
			for nbr in W[n]:
				x[nbr] += alpha * xlast[n] * W[n][nbr][weight]
			x[n] += danglesum * dangling_weights[n] + (1.0 - alpha) * p[n]

		# verifica convergência, norma l1
		err = sum([abs(x[n] - xlast[n]) for n in x])
		if err < N*tol:
			return x
	raise NetworkXError('pagerank: power iteration failed to converge '
						'in %d iterations.' % max_iter)

	