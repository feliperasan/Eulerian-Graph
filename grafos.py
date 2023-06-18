# ALUNOS: FELIPE R. S. BARBOSA, JOAQUIM A. D. VIANA, LARISSA P. S. GARCIA
# MATRICULA: 202320070005     , 202320080005       , 202320070010
# ATIVIDADE 2 DO TRABALHO DE GRAFOS

from collections import defaultdict
import heapq

class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = defaultdict(list)

    def adicionarAresta(self, origem, destino, peso):
        self.grafo[origem].append((destino, peso))
        self.grafo[destino].append((origem, peso))

    def removerAresta(self, origem, destino):
        for i, (v, _) in enumerate(self.grafo[origem]):
            if v == destino:
                self.grafo[origem].pop(i)
        for i, (u, _) in enumerate(self.grafo[destino]):
            if u == origem:
                self.grafo[destino].pop(i)

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

    def imprimirCaminhoEulerianoUtil(self, u, caminho):
        for v, peso in self.grafo[u]:
            if self.arestaProximaValida(u, v):
                caminho.append((u, v, peso))
                self.removerAresta(u, v)
                self.imprimirCaminhoEulerianoUtil(v, caminho)

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
        return distancias, caminho

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
                return peso

    def imprimirGrafo(self):
        for vertice in range(self.V):
            print("Lista de adjacência do vértice", vertice)
            for aresta in self.grafo[vertice]:
                destino, peso = aresta
                print(" ->", destino, "[Peso:", peso, "]")

print("")
print("Grafo - 1 ----------------------------------------")
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

distancias, caminho_euleriano = g1.menorDistancia(0)
if caminho_euleriano:
    print("Caminho Euleriano:")
    for u, v, peso in caminho_euleriano:
        print("%d-%d (Peso: %d)" % (u, v, peso))
else:
    print("Não há caminho euleriano no grafo.")

print("Menor distância até o vértice de origem:")
print(distancias)


g2 = Grafo(4)
g2.adicionarAresta(0, 1, 1)
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