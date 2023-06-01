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

// Cria um Nó com peso
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

void fleury(Grafo* grafo, int vInicial) {
  // marca os vertices visitados
  int* visitado = (int*)calloc(grafo -> v, sizeof(int));

  printf("Caminho de Fleury:\n");

  int atual = vInicial;
  printf("%d", atual);

  while () {
    
  }
}


int main() {
  int v = 6;
  Grafo* grafo = criarGrafo(v);

  // Grafo, Origim, destino, peso da aresta
  adicionarAresta(grafo, 0, 1, 5);
  adicionarAresta(grafo, 0, 2, 3);
  adicionarAresta(grafo, 1, 2, 3);
  adicionarAresta(grafo, 1, 3, 5);
  adicionarAresta(grafo, 1, 5, 1);
  adicionarAresta(grafo, 2, 4, 5);
  adicionarAresta(grafo, 2, 5, 7);
  adicionarAresta(grafo, 3, 4, 3);
  adicionarAresta(grafo, 3, 5, 3);
  adicionarAresta(grafo, 3, 6, 5);
  adicionarAresta(grafo, 4, 5, 11);
  adicionarAresta(grafo, 4, 6, 7);

  printGrafo(grafo);


  return 0;
}
