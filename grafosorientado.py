# ALUNOS: FELIPE R. S. BARBOSA, JOAQUIM A. D. VIANA, LARISSA P. S. GARCIA
# MATRICULA: 202320070005     , 202320080005       , 202320070010
# PROBLEMA 3 DO TRABALHO DE GRAFOS

# defaultdict é uma variante do dicionário padrão, mas permite definir um valor padrão para chaves ausentes. Isso é usado para criar a estrutura do grafo, em que cada vértice é representado por uma chave e possui uma lista de arestas adjacentes.

# heapq fornece implementações eficientes de estruturas de dados de fila de prioridade.

from collections import defaultdict
import heapq

class Grafo:
    def __init__(self, vertices): # Construtor da classe Grafo.
        self.V = vertices
        self.grafo = defaultdict(list)

    def adicionarArco(self, origem, destino, peso):
        self.grafo[origem].append((destino, peso))
        # self.grafo[destino].append((origem, peso)) removido visto que trata-se um grafo orientado.

    def removerArco(self, origem, destino):
        for i, (v, _) in enumerate(self.grafo[origem]):
            if v == destino:
                self.grafo[origem].pop(i)

    def contarVerticesAlcancaveis(self, v, visitado):
        count = 1
        visitado[v] = True
        for i, _ in self.grafo[v]: # o _ ignora o segundo elemento da tupla (peso)
            if not visitado[i]:
                count += self.contarVerticesAlcancaveis(i, visitado)
        return count

    def arcoProximoValido(self, u, v):
        if len(self.grafo[u]) == 1:
            return True
        else:
            visitado = [False] * self.V
            count1 = self.contarVerticesAlcancaveis(u, visitado)

            self.removerArco(u, v)
            visitado = [False] * self.V
            count2 = self.contarVerticesAlcancaveis(u, visitado)

            self.adicionarArco(u, v, 0)

            return False if count1 > count2 else True

    # Verifica se um caminho euleriano existe no grafo.
    def encontrarCaminhoEuleriano(self):
        grau_entrada = [0] * self.V # lista usada para armazenar o grau de entrada de cada vértice do grafo.
        grau_saida = [0] * self.V # usada para armazenar o grau de saída de cada vértice do grafo.

        for i in range(self.V): # Percorrer todos os arcos do grafo e calcula os graus de entrada e saída de cada vértice.
            for v, _ in self.grafo[i]:
                grau_saida[i] += 1
                grau_entrada[v] += 1

        for i in range(self.V):
            if grau_entrada[i] != grau_saida[i]: # verifica se existe algum vértice em que o grau de entrada é diferente do grau de saída.
                # Se essa condição for verdadeira, significa que não há caminho euleriano no grafo, pois há vértices com uma diferença entre as arestas que entram e saem. Nesse caso, o método retorna uma lista vazia [] indicando a inexistência de um caminho euleriano.
                return []

        caminho = [] # armazena o caminho euleriano encontrado encontrado.
        u = 0
        self.imprimirCaminhoEulerianoUtil(u, caminho)
        return caminho # retorna um array de caminho

    # Método responsável por construir o caminho euleriano a partir do vértice de partida
    def imprimirCaminhoEulerianoUtil(self, u, caminho):
        for v, peso in self.grafo[u]:
            if self.arcoProximoValido(u, v):
                caminho.append((u, v, peso))
                self.removerArco(u, v)
                self.imprimirCaminhoEulerianoUtil(v, caminho)

    # Algoritmo de Dijkstra usando uma fila de prioridade (heap).
    def menorDistancia(self, origem):
        distancias = [float('inf')] * self.V
        distancias[origem] = 0
        anterior = {} # Dicionário para armazenar o vértice anterior no caminho mais curto
        heap = [(0, origem)]

        while heap:
            distancia, vertice = heapq.heappop(heap)

            if distancia > distancias[vertice]:
                continue

            for adjacente, peso in self.grafo[vertice]:
                nova_distancia = distancia + peso

                if nova_distancia < distancias[adjacente]:
                    distancias[adjacente] = nova_distancia
                    anterior[adjacente] = vertice # Atualiza o vértice anterior
                    heapq.heappush(heap, (nova_distancia, adjacente))

        caminho = []
        for v in range(self.V):
            if v != origem:
                path = []
                while v != origem:
                    path.insert(0, (anterior[v], v, self.obterPesoArco(anterior[v], v)))
                    v = anterior[v]
                caminho.extend(path)

        return distancias, caminho # Retorna um array com as menores distancias e um dict que contem os vértices anteriores do caminho mínimo.

    def obterPesoArco(self, origem, destino):
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
print("Dígrafo - 1 ----------------------------------------")
# Instanciando o Grafo G1 da Figura do PROBLEMA 3 com vértices de grau par.
g1 = Grafo(7)
g1.adicionarArco(0, 1, 5) # Origem, Destino, Peso
g1.adicionarArco(0, 2, 3)
g1.adicionarArco(1, 2, 3)
g1.adicionarArco(1, 3, 5)
g1.adicionarArco(1, 5, 1)
g1.adicionarArco(2, 4, 5)
g1.adicionarArco(2, 5, 7)
g1.adicionarArco(3, 4, 3)
g1.adicionarArco(3, 5, 3)
g1.adicionarArco(3, 6, 5)
g1.adicionarArco(4, 5, 11)
g1.adicionarArco(4, 6, 7)

g1.imprimirGrafo()

caminho_euleriano = g1.encontrarCaminhoEuleriano()
if caminho_euleriano:
    print("Caminho Euleriano:")
    for u, v, peso in caminho_euleriano:
        print("%d -> %d (Peso: %d)" % (u, v, peso))
else:
    print("Não há caminho euleriano no grafo.")

print("Menor distância até o vértice de origem:")

distancias, caminho_mais_curto = g1.menorDistancia(0)
if caminho_mais_curto:
    print("Caminho mais curto:")
    for u, v, peso in caminho_mais_curto:
        print("%d -> %d (Peso: %d)" % (u, v, peso))
else:
    print("Não há caminho mais curto para o vértice de origem.")

print("")
print("Dígrafo - 2 ----------------------------------------")
# Instanciando o Grafo G2 da Figura do PROBLEMA 3 com vértices de grau ímpar.
g2 = Grafo(4)
g2.adicionarArco(0, 1, 1) # Origem, Destino, Peso
g2.adicionarArco(0, 2, 2)
g2.adicionarArco(2, 1, 3)
g2.adicionarArco(2, 3, 4)

g2.imprimirGrafo()

caminho_euleriano = g2.encontrarCaminhoEuleriano()
if caminho_euleriano:
    print("Caminho Euleriano:")
    for u, v, peso in caminho_euleriano:
        print("%d -> %d (Peso: %d)" % (u, v, peso))
else:
    print("Não há caminho euleriano no grafo.")

print("Menor distância até o vértice de origem:")

distancias, caminho_mais_curto = g2.menorDistancia(0)
if caminho_mais_curto:
    print("Caminho mais curto:")
    for u, v, peso in caminho_mais_curto:
        print("%d -> %d (Peso: %d)" % (u, v, peso))
else:
    print("Não há caminho mais curto para o vértice de origem.")
