#include <stdio.h>
#include <stdlib.h>

typedef struct No {
  int dest;
  struct No* prox;
} No;

typedef struct Grafo {
  int v;
  No** adjList;
} Grafo;

// Cria um Nó
No* criarNo(int dest) {
  No* novoNo = (No*)malloc(sizeof(No));
  novoNo -> dest = dest;
  novoNo -> prox = NULL;
  return novoNo;
}

// Cria o Grafo com v vertices
Grafo* criarGrafo(int vertice) {
  Grafo* grafo = (Grafo*)malloc(sizeof(Grafo));
  grafo -> v = vertice;

  // Cria lista de adjacencia
  grafo -> adjList = (No**)malloc(vertice * sizeof(No*));

  // Inicializa todas as listas de adjacencia como vazias
  for(int i = 0; i < vertice; i++) {
    grafo -> adjList[i] = NULL;
  }

  return grafo;
}

// Adiciona Aresta não direcionada ao Grafo
void adicionarAresta(Grafo* grafo, int origem, int dest) {
  // Adiciona uma aresta do vertice de origem para o destino
  No* novoNo = criarNo(dest);
  novoNo -> prox = grafo -> adjList[origem];
  grafo -> adjList[origem] = novoNo;

  // Adiciona uma aresta do vertice de destino para a origem
  novoNo = criarNo(origem);
  novoNo -> prox = grafo -> adjList[dest];
  grafo -> adjList[dest] = novoNo;
}

// Imprime o grafo
void printGrafo(Grafo* grafo) {
  for (int i = 0; i < grafo -> v; i++) {
    No* temp = grafo -> adjList[i];
    printf("Lista de adjacencia do vertice %d\n", i);
    while (temp) {
      printf(" -> %d", temp -> dest);
      temp = temp -> prox;
    }

    printf("\n");
  }
}


int main() {
  int v = 5;
  Grafo* grafo = criarGrafo(v);

  adicionarAresta(grafo, 0, 1);
  adicionarAresta(grafo, 0, 4);
  adicionarAresta(grafo, 1, 2);
  adicionarAresta(grafo, 1, 3);
  adicionarAresta(grafo, 1, 4);
  adicionarAresta(grafo, 2, 3);
  adicionarAresta(grafo, 3, 4);

  printGrafo(grafo);


  return 0;
}
