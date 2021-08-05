# 1. Construa uma classe Digrafo para representar o grafo orientado utilizando a matriz de adjacência.

class Digrafo:
    def __init__(self, V):
        self.V = V+1
        self.A = 0
        self.adj = [[0] * self.V for i in range(self.V)]

    def insere(self, u, w):
        self.adj[u][w] = 1  #(u, w)
        self.A += 1

    def remove(self, u, w):
        self.adj[u][w] = 0
        self.A -= 1  

    def mostra(self):
        for i in range(1, self.V):
            print('{}: '.format(i), end='')
            for j in range(1, self.V):
                if self.adj[i][j]:
                    print('{} '.format(j), end='')
            print()
    
    def calculaGrauSaida(self, v):
        grau = 0
        for i in range(self.V):
            if self.adj[v][i] == 1:
                grau += 1
        return grau
      
            
    def calculaGrauEntradas(self, v):
        grau = 0
        for i in range(self.V):
            if self.adj[i][v] == 1:
                grau += 1
        return grau
        
        


def main():
  grafo = Digrafo(4)
  arestas = {(1,2), (2,2), (1,3), (2,4), (3,2), (4,3)}

  for aresta in arestas:
    grafo.insere(aresta[0], aresta[1])

  print("Arestas:")
  grafo.mostra()
  print('Graude de entrada de 2: ' + str(grafo.calculaGrauEntradas(2)))
  print('Graude de saída de 2: ' + str(grafo.calculaGrauSaida(2)))
  


main()

