#include <stdio.h>
#include <stdlib.h>

typedef struct No {
  int dest;
  int peso;
  struct No* prox;
} No;

typedef struct Grafo {
  int v;
  No** adjList;
} Grafo;

// Cria um Nó
No* criarNo(int dest, int peso) {
  No* novoNo = (No*)malloc(sizeof(No));
  novoNo -> dest = dest;
  novoNo -> peso = peso;
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
void adicionarAresta(Grafo* grafo, int origem, int dest, int peso) {
  // Adiciona uma aresta do vertice de origem para o destino
  No* novoNo = criarNo(dest, peso);
  novoNo -> prox = grafo -> adjList[origem];
  grafo -> adjList[origem] = novoNo;

  // Adiciona uma aresta do vertice de destino para a origem
  novoNo = criarNo(origem, peso);
  novoNo -> prox = grafo -> adjList[dest];
  grafo -> adjList[dest] = novoNo;
}

// Imprime o grafo
void printGrafo(Grafo* grafo) {
  for (int i = 0; i < grafo -> v; i++) {
    No* temp = grafo -> adjList[i];
    printf("Lista de adjacencia do vertice %d\n", i);
    while (temp) {
      printf(" -> %d [Peso: %d]", temp -> dest, temp -> peso);
      temp = temp -> prox;
    }

    printf("\n");
  }
}


int main() {
  int v = 5;
  Grafo* grafo = criarGrafo(v);

  // Grafo, Origim, destino, peso da aresta
  adicionarAresta(grafo, 0, 1, 2);
  adicionarAresta(grafo, 0, 4, 5);
  adicionarAresta(grafo, 1, 2, 3);
  adicionarAresta(grafo, 1, 3, 1);
  adicionarAresta(grafo, 1, 4, 4);
  adicionarAresta(grafo, 2, 3, 7);
  adicionarAresta(grafo, 3, 4, 6);

  printGrafo(grafo);


  return 0;
}
