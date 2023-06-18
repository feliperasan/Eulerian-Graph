# ALUNOS: FELIPE R. S. BARBOSA, JOAQUIM A. D. VIANA, LARISSA P. S. GARCIA
# MATRICULA: 202320070005     , 202320080005       , 202320070010
# ATIVIDADE 3 DO TRABALHO DE GRAFOS

from collections import defaultdict
import heapq

class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = defaultdict(list)

    def adicionarAresta(self, origem, destino, peso):
        self.grafo[origem].append((destino, peso))

    def removerAresta(self, origem, destino):
        for i, (v, _) in enumerate(self.grafo[origem]):
            if v == destino:
                self.grafo[origem].pop(i)

    def contarVerticesAlcancaveis(self, v, visitado):
        count = 1
        visitado[v] = True
        for i, _ in self.grafo[v]:
            if not visitado[i]:
                count += self.contarVerticesAlcancaveis(i, visitado)
        return count

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

    def encontrarCaminhoEuleriano(self):
        grau_entrada = [0] * self.V
        grau_saida = [0] * self.V

        for i in range(self.V):
            for v, _ in self.grafo[i]:
                grau_saida[i] += 1
                grau_entrada[v] += 1

        for i in range(self.V):
            if grau_entrada[i] != grau_saida[i]:
                return []

        caminho = []
        u = 0
        self.imprimirCaminhoEulerianoUtil(u, caminho)
        return caminho

    def imprimirCaminhoEulerianoUtil(self, u, caminho):
        for v, peso in self.grafo[u]:
            if self.arestaProximaValida(u, v):
                caminho.append((u, v, peso))
                self.removerAresta(u, v)
                self.imprimirCaminhoEulerianoUtil(v, caminho)

    def menorDistancia(self, origem):
        distancias = [float('inf')] * self.V
        distancias[origem] = 0
        anterior = {}
        heap = [(0, origem)]

        while heap:
            distancia, vertice = heapq.heappop(heap)

            if distancia > distancias[vertice]:
                continue

            for adjacente, peso in self.grafo[vertice]:
                nova_distancia = distancia + peso

                if nova_distancia < distancias[adjacente]:
                    distancias[adjacente] = nova_distancia
                    anterior[adjacente] = vertice
                    heapq.heappush(heap, (nova_distancia, adjacente))

        caminho = []
        for v in range(self.V):
            if v != origem:
                path = []
                while v != origem:
                    path.insert(0, (anterior[v], v, self.obterPesoAresta(anterior[v], v)))
                    v = anterior[v]
                caminho.extend(path)

        return distancias, caminho

    def obterPesoAresta(self, origem, destino):
        for v, peso in self.grafo[origem]:
            if v == destino:
                return peso

    def imprimirGrafo(self):
        for vertice in range(self.V):
            print("Lista de adjacência do vértice", vertice)
            for aresta in self.grafo[vertice]:
                destino, peso = aresta
                print(" ->", destino, "[Peso:", peso, "]")


print("Grafo - 1")
g1 = Grafo(7)
g1.adicionarAresta(0, 1, 5)
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

g2 = Grafo(4)
g2.adicionarAresta(0, 1, 1)
g2.adicionarAresta(0, 2, 2)
g2.adicionarAresta(2, 1, 3)
g2.adicionarAresta(2, 3, 4)

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
