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

            # Adicionei um valor arbitrário de peso 0
            self.adicionarAresta(u, v, 0)

            return False if count1 > count2 else True

    # Algoritmo de Fleury
    def imprimirCicloEulerianoUtil(self, u):
        for v, peso in self.grafo[u]:
            if self.arestaProximaValida(u, v):
                print("%d-%d (Peso: %d)" % (u, v, peso))
                self.removerAresta(u, v)
                self.imprimirCicloEulerianoUtil(v)

    # Condição de Euler
    def imprimirCicloEuleriano(self):
        grau_impar = []
        for i in range(self.V):
            if len(self.grafo[i]) % 2 != 0:
                grau_impar.append(i)

        if len(grau_impar) == 0:
            print("Há um ciclo Euleriano.")
        elif len(grau_impar) == 2:
            print("Há um ciclo Euleriano Aberto.")
        else:
            print("Não há um ciclo Euleriano.")

    def imprimirGrafo(self):
        for vertice in range(self.V):
            print("Lista de adjacência do vértice", vertice)
            for aresta in self.grafo[vertice]:
                destino, peso = aresta
                print(" ->", destino, "[Peso:", peso, "]")

    # Grafo de Dijkstra utilizando heap
    def menorDistancia(self, origem):
        distancias = [float('inf')] * self.V
        distancias[origem] = 0
        
        heap = [(0, origem)]
        
        while heap:
            distancia, vertice = heapq.heappop(heap)
            
            if distancia > distancias[vertice]:
                continue
            
            for adjacente, peso in self.grafo[vertice]:
                nova_distancia = distancia + peso
                
                if nova_distancia < distancias[adjacente]:
                    distancias[adjacente] = nova_distancia
                    heapq.heappush(heap, (nova_distancia, adjacente))
        
        return distancias

print("")
print("Grafo - 1 ----------------------------------------")
g1 = Grafo(7)
g1.adicionarAresta(0, 1, 5)
g1.adicionarAresta(0, 2, 3)
# g1.adicionarAresta(1, 2, 3)
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
g1.imprimirCicloEuleriano()

print("Menor distância até o vértice de origem:")
print(g1.menorDistancia(0))