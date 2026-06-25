import heapq
from collections import deque
from dados_colonia import (modulos, grafo, matriz_adjacencia)


# Algoritmo de Dijkstra

def dijkstra(grafo, inicio):

    distancias = {
        no: float('inf') 
        for no in grafo
    }
    anteriores = {}

    distancias[inicio] = 0

    fila = [(0, inicio)]

    while fila:
        dist_atual, atual = heapq.heappop(fila)

        for vizinho, peso in grafo[atual]:
            nova_dist = dist_atual + peso

            if nova_dist < distancias[vizinho]:
                distancias[vizinho] = nova_dist
                anteriores[vizinho] = atual
                heapq.heappush(fila, (nova_dist, vizinho))

    return distancias, anteriores

def reconstruir_caminho(anteriores, destino):
    caminho = []
    atual = destino

    while atual in anteriores:
        caminho.append(atual)
        atual = anteriores[atual]

    caminho.append(atual)  # Adiciona o nó inicial
    caminho.reverse()  # Inverte a lista para obter o caminho correto
    return caminho

# BFS

def bfs(grafo, inicio):
    visitados = set()
    fila = deque([inicio])

    while fila:
        atual = fila.popleft()
        if atual not in visitados:
            print(atual)
            visitados.add(atual)

            for vizinho, _ in grafo[atual]:
                fila.append(vizinho)

# DFS

def dfs(grafo, atual, visitados=None):
    if visitados is None:
        visitados = set()

    print(atual)
    visitados.add(atual)

    for vizinho, _ in grafo[atual]:
        if vizinho not in visitados:
            dfs(grafo, vizinho, visitados)

# Função para ordenar os módulos por prioridade
def prioridade_modulos(modulos):
    return sorted(modulos.items(), key=lambda x: x[1]["prioridade"], reverse=True)

# Função para calcular o consumo total de energia dos módulos
def consumo_total(modulos):
    return sum(m["consumo"] for m in modulos.values())