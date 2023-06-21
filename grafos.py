# ALUNOS: FELIPE R. S. BARBOSA, JOAQUIM A. D. VIANA, LARISSA P. S. GARCIA
# MATRICULA: 202320070005     , 202320080005       , 202320070010
# PROBLEMA 2 DO TRABALHO DE GRAFOS

# defaultdict é uma variante do dicionário padrão, mas permite definir um valor padrão para chaves ausentes. Isso é usado para criar a estrutura do grafo, em que cada vértice é representado por uma chave e possui uma lista de arestas adjacentes.

# heapq fornece implementações eficientes de estruturas de dados de fila de prioridade.

from collections import defaultdict 
import heapq

class Grafo:
    def __init__(self, vertices): # construtor da classe grafo
        self.V = vertices # Atribuindo o valor do parâmetro vertices à variável de instância "V" da classe
        self.grafo = defaultdict(list) # grafo inicializando como um objeto do tipo defaultdict com uma lista vazia como valor padrão.

    # adiciona uma aresta do ponto de origem ao destino com o peso da aresta
    def adicionarAresta(self, origem, destino, peso):
        self.grafo[origem].append((destino, peso))
        self.grafo[destino].append((origem, peso))

    def removerAresta(self, origem, destino):
        # enumerate para obter tanto o índice i quanto o valor (v, _) em cada iteração
        # (v, _) representa uma tupla contendo o vértice adjacente v e o peso associado à aresta, mas o peso não será usado nesse caso.
        for i, (v, _) in enumerate(self.grafo[origem]):
            if v == destino: # verifica se v é igual ao vértice de destino que desejamos remover
                self.grafo[origem].pop(i) # remove a aresta encontrada
        for i, (u, _) in enumerate(self.grafo[destino]): # itera sobre a lista de adj do vértice de destino.
            if u == origem: # verifica se o vértice adjacente u é igual ao vértice de origem
                self.grafo[destino].pop(i)

    def contarVerticesAlcancaveis(self, v, visitado):
        count = 1 # conta o nº de vértices
        visitado[v] = True
        for i, _ in self.grafo[v]: # o _ ignora o segundo elemento da tupla (peso)
            if not visitado[i]: # verifica se não foi visitado
                count += self.contarVerticesAlcancaveis(i, visitado)
        return count # retorna o nº de vértices alcançáveis a partir de v

    def arestaProximaValida(self, u, v):
        if len(self.grafo[u]) == 1: # verifica se o vértice u possui apenas uma aresta adjacente
            return True
        else:
            visitado = [False] * self.V # inicializa com False para cada vértice no grafo
            count1 = self.contarVerticesAlcancaveis(u, visitado)

            self.removerAresta(u, v)
            visitado = [False] * self.V
            count2 = self.contarVerticesAlcancaveis(u, visitado)

            self.adicionarAresta(u, v, 0)

            return False if count1 > count2 else True # Se count1 for maior que count2, significa que após a remoção da aresta entre u e v, há menos vértices alcançáveis a partir de u.

    def encontrarCaminhoEuleriano(self):
        grau_impar = []
        for i in range(self.V):
            if len(self.grafo[i]) % 2 != 0:
                grau_impar.append(i)

        if len(grau_impar) == 0 or len(grau_impar) == 2: # verifica se possui 0 v impar ou exatamente 2
            caminho = []
            if len(grau_impar) == 0:
                u = 0
            else:
                u = grau_impar[0]
            self.imprimirCaminhoEulerianoUtil(u, caminho)
            return caminho

        return []

    # Algoritmo recursivo que constrói o caminho euleriano.
    def imprimirCaminhoEulerianoUtil(self, u, caminho):
        for v, peso in self.grafo[u]: # itera sobre cada elemento da lista de adjacência do vértice u
            if self.arestaProximaValida(u, v): # se for valida executa o bloco.
                caminho.append((u, v, peso))
                self.removerAresta(u, v)
                self.imprimirCaminhoEulerianoUtil(v, caminho)


    def menorDistancia(self, origem):
        distancias = [float('inf')] * self.V # elementos inicializados com infinito
        distancias[origem] = 0 # define vertice de partida como 0
        anterior = {}  # Dicionário para armazenar o vértice anterior no caminho mais curto
        heap = [(0, origem)] # cria fila de prioridade, inicializado com uma tupla contendo a distância (0) e o vértice de origem

        while heap: # Enquanto houver vértice, faça.
            distancia, vertice = heapq.heappop(heap)

            if distancia > distancias[vertice]: # verifica se a distância atual é maior
                continue

            for adjacente, peso in self.grafo[vertice]: # itera sobre cada vértice adjacente ao vértice atual, juntamente com o peso da aresta que os conecta.
                nova_distancia = distancia + peso

                if nova_distancia < distancias[adjacente]:
                    distancias[adjacente] = nova_distancia # atualiza a distância registrada para o vértice adjacente
                    anterior[adjacente] = vertice  # Atualiza o vértice anterior
                    heapq.heappush(heap, (nova_distancia, adjacente)) # atualiza a distância registrada para o vértice adjacente

        caminho = self.construirCaminho(origem, anterior)
        return distancias, caminho # Retorna um array com as menores distancias e um dict que contem os vértices anteriores do caminho mínimo. 

    # Constrói o caminho mais curto a partir do dicionário de vértices
    def construirCaminho(self, origem, anterior):
        caminho = [] # armazena as arestas que compõem o caminho mínimo
        for vertice in range(self.V): # itera sob todos os vértices do grafo
            if vertice == origem:
                continue
            atual = vertice
            while atual != origem:
                caminho.append((anterior[atual], atual, self.pesoAresta(anterior[atual], atual))) # adiciona uma tupla à lista caminho, essa tupla representa uma aresta no caminho mínimo.
                atual = anterior[atual]
        return caminho[::-1]  # Inverte o caminho para garantir a ordem correta do v de origem até o destino

    
    def pesoAresta(self, origem, destino):
        for v, peso in self.grafo[origem]:
            if v == destino: # verifica se o vértice v é igual ao destino. Se for o caso, significa que encontramos a aresta que liga a origem ao destino. Nesse caso, o método retorna o peso dessa aresta. Se o loop terminar sem encontrar a aresta entre a origem e o destino, o método não encontra o peso e, portanto, não há uma aresta direta entre os dois vértices. Isso pode acontecer se não houver uma aresta que liga a origem e o destino no grafo.
                return peso # Retorna o peso de uma aresta entre dois vértices.
            
    # Imprime a lista de adjacências do grafo
    def imprimirGrafo(self):
        for vertice in range(self.V):
            print("Lista de adjacência do vértice", vertice)
            for aresta in self.grafo[vertice]:
                destino, peso = aresta
                print(" ->", destino, "[Peso:", peso, "]")

print("")
print("Grafo - 1 ----------------------------------------")
# Instanciando o Grafo G1 da Figura do PROBLEMA 2 com vértices de grau par.
g1 = Grafo(7)

g1.adicionarAresta(0, 1, 5) # Origem, Destino, Peso
g1.adicionarAresta(0, 2, 3)
g1.adicionarAresta(1, 2, 3)
g1.adicionarAresta(1, 3, 5)
g1.adicionarAresta(1, 5, 1)
g1.adicionarAresta(2, 4, 5)
g1.adicionarAresta(2, 5, 7)
g1.adicionarAresta(3, 4, 3)
g1.adicionarAresta(3, 5, 3)
g1.adicionarAresta(3, 6, 5)
g1.adicionarAresta(4, 5, 11)
g1.adicionarAresta(4, 6, 7)

g1.imprimirGrafo()

distancias, caminho_euleriano = g1.menorDistancia(0) # caminho_euleriano armazena o caminho obtido a partir do método "imprimirCaminhoEulerianoUtil".
if caminho_euleriano:
    print("Caminho Euleriano:")
    for u, v, peso in caminho_euleriano:
        print("%d-%d (Peso: %d)" % (u, v, peso))
else:
    print("Não há caminho euleriano no grafo.")

print("Menor distância até o vértice de origem:")
print(distancias)

print("")
print("Grafo - 2 ----------------------------------------")
# Instanciando o Grafo G2 da Figura do PROBLEMA 2 com grau ímpar.
g2 = Grafo(4)
g2.adicionarAresta(0, 1, 1) # Origem, Destino, Peso
g2.adicionarAresta(0, 2, 2)
g2.adicionarAresta(1, 2, 3)
g2.adicionarAresta(2, 3, 4)

g2.imprimirGrafo()

distancias, caminho_euleriano = g2.menorDistancia(0)
if caminho_euleriano:
    print("Caminho Euleriano:")
    for u, v, peso in caminho_euleriano:
        print("%d-%d (Peso: %d)" % (u, v, peso))
else:
    print("Não há caminho euleriano no grafo.")

print("Menor distância até o vértice de origem:")
print(distancias)