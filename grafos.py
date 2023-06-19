# ALUNOS: FELIPE R. S. BARBOSA, JOAQUIM A. D. VIANA, LARISSA P. S. GARCIA
# MATRICULA: 202320070005     , 202320080005       , 202320070010
# PROBLEMA 2 DO TRABALHO DE GRAFOS

# defaultdict é uma variante do dicionário padrão, mas permite definir um valor padrão para chaves ausentes. Isso é usado para criar a estrutura do grafo, em que cada vértice é representado por uma chave e possui uma lista de arestas adjacentes.

# heapq fornece implementações eficientes de estruturas de dados de fila de prioridade.

from collections import defaultdict 
import heapq

class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = defaultdict(list)

    # Recebe a origem, destino e peso de uma aresta e adiciona essa informação tanto na lista de adjacências do vértice de origem quanto na lista do vértice de destino. Tem complexidade O(1).
    def adicionarAresta(self, origem, destino, peso):
        self.grafo[origem].append((destino, peso))
        self.grafo[destino].append((origem, peso))

    # Remove uma aresta do grafo, percorrendo as listas de adjacências do vértice de origem e destino e removendo a aresta correspondente. Tem Complexidade O(1).
    def removerAresta(self, origem, destino):
        for i, (v, _) in enumerate(self.grafo[origem]):
            if v == destino:
                self.grafo[origem].pop(i)
        for i, (u, _) in enumerate(self.grafo[destino]):
            if u == origem:
                self.grafo[destino].pop(i)

    #  Função auxiliar que conta o número de vértices alcançáveis a partir de um determinado vértice. Utiliza-se uma recursividade para percorrer o grafo e marca os vértices visitados para evitar loops infinitos. Tem Complexidade O(V + E).
    def contarVerticesAlcancaveis(self, v, visitado):
        count = 1
        visitado[v] = True
        for i, _ in self.grafo[v]:
            if not visitado[i]:
                count += self.contarVerticesAlcancaveis(i, visitado)
        return count

    # Verifica se uma aresta entre dois vértices é a próxima aresta válida em um caminho euleriano. Ela realiza uma comparação entre a quantidade de vértices alcançáveis antes e depois de remover a aresta. Tem Complexidade O(V + E).
    def arestaProximaValida(self, u, v):
        if len(self.grafo[u]) == 1:
            return True
        else:
            visitado = [False] * self.V
            count1 = self.contarVerticesAlcancaveis(u, visitado)

            self.removerAresta(u, v)
            visitado = [False] * self.V
            count2 = self.contarVerticesAlcancaveis(u, visitado)

            self.adicionarAresta(u, v, 0)

            return False if count1 > count2 else True

    # Verifica se um caminho euleriano existe no grafo. A Função começa verificando se há vértices com grau ímpar no grafo. Se houver no máximo 2 vértices com grau ímpar, então um caminho euleriano é possível.
    # Se o caminho euleriano for possível, a função chama a função imprimirCaminhoEulerianoUtil para construir o caminho. Tem Complexidade O(V + E).
    def encontrarCaminhoEuleriano(self):
        grau_impar = []
        for i in range(self.V):
            if len(self.grafo[i]) % 2 != 0:
                grau_impar.append(i)

        if len(grau_impar) == 0 or len(grau_impar) == 2:
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
        for v, peso in self.grafo[u]:
            if self.arestaProximaValida(u, v):
                caminho.append((u, v, peso))
                self.removerAresta(u, v)
                self.imprimirCaminhoEulerianoUtil(v, caminho)

    # implementa o algoritmo de Dijkstra para encontrar a menor distância entre um vértice de origem e todos os outros vértices. Ela utiliza uma fila de prioridade (implementada como um heap) para selecionar o vértice com a menor distância. Tem Complexidade O((V + E) log V).
    def menorDistancia(self, origem):
        distancias = [float('inf')] * self.V
        distancias[origem] = 0
        anterior = {}  # Dicionário para armazenar o vértice anterior no caminho mais curto
        heap = [(0, origem)]

        while heap:
            distancia, vertice = heapq.heappop(heap)

            if distancia > distancias[vertice]:
                continue

            for adjacente, peso in self.grafo[vertice]:
                nova_distancia = distancia + peso

                if nova_distancia < distancias[adjacente]:
                    distancias[adjacente] = nova_distancia
                    anterior[adjacente] = vertice  # Atualiza o vértice anterior
                    heapq.heappush(heap, (nova_distancia, adjacente))

        caminho = self.construirCaminho(origem, anterior)
        return distancias, caminho # Retorna um array com as menores distancias e um dict que contem os vértices anteriores do caminho mínimo. 

    # Constrói o caminho mais curto a partir do dicionário de vértices
    def construirCaminho(self, origem, anterior):
        caminho = []
        for vertice in range(self.V):
            if vertice == origem:
                continue
            atual = vertice
            while atual != origem:
                caminho.append((anterior[atual], atual, self.pesoAresta(anterior[atual], atual)))
                atual = anterior[atual]
        return caminho[::-1]  # Inverte o caminho

    
    def pesoAresta(self, origem, destino):
        for v, peso in self.grafo[origem]:
            if v == destino:
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

distancias, caminho_euleriano = g1.menorDistancia(0)
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