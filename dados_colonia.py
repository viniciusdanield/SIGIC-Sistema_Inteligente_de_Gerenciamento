import heapq
from collections import deque
# DICIONÁRIO CONTENDO INFORMAÇÕES SOBRE OS MÓDULOS:

modulos = {
"Habitação": {
    "consumo": (20,),
    "prioridade":  ,
    "armazenamento": ,
    "comunicacao": ,
    "status": , 
},

"Centro de Controle": {
    "consumo": ,
    "prioridade": ,
    "armazenamento": ,
    "comunicacao": ,
    "status": , 
},

"Armazenamento de energia": {
    "consumo": ,
    "prioridade": ,
    "armazenamento": ,
    "comunicacao": ,
    "status": , 
},

"Agricultura": {
    "consumo": ,
    "prioridade": ,
    "armazenamento": ,
    "comunicacao": ,
    "status": , 
},

"Laboratório científico": {
    "consumo": ,
    "prioridade": ,
    "armazenamento": ,
    "comunicacao": ,
    "status": , 
},

"Comunicação": {
    "consumo": ,
    "prioridade": ,
    "armazenamento": ,
    "comunicacao": ,
    "status": , 
},

"Suporte Médico": {
    "consumo": ,
    "prioridade": ,
    "armazenamento": ,
    "comunicacao": ,
    "status": , 
},

"Produção de oxigênio": {
    "consumo": ,
    "prioridade": ,
    "armazenamento": ,
    "comunicacao": ,
    "status": , 
},
}

# GRAFO DA COLÔNIA 
# Cada conexão representa um peso, o preso representa : distância / custo energético / tempo

grafo = {
    "Habitação": 
    [ ("Centro de Controle", ), 
    ("Suporte Médico", ) ], 

    "Centro de Controle": 
    [ ("Habitação", ), 
     ("Comunicação", ), 
     ("Armazenamento de Energia", ), 
     ("Laboratório Científico", ) ], 

    "Armazenamento de Energia": 
    [ ("Centro de Controle", ), 
     ("Produção de Oxigênio", ), 
     ("Agricultura", ) ], 

    "Agricultura": 
    [ ("Armazenamento de Energia", ), 
     ("Laboratório Científico", ) ], 

    "Laboratório Científico": 
    [ ("Agricultura", ), 
     ("Comunicação", ), 
     ("Centro de Controle", ) ], 

    "Comunicação": 
    [ ("Centro de Controle", ), 
    ("Laboratório Científico", ) ], 

    "Suporte Médico": 
    [ ("Habitação", ), 
     ("Produção de Oxigênio", ) ],

    "Produção de Oxigênio": 
    [ ("Armazenamento de Energia", ), 
    ("Suporte Médico", ) ] }

print("TESTANDO")

# Algoritmo de Dijkstra

def dijkstra(grafo, inicio):
    distancias = {no: float('inf') for no in grafo}
    distancias[inicio] = 0
    fila = [(0, inicio)]

    while fila:
        dist_atual, atual = heapq.heappop(fila)

        for vizinho, peso in grafo[atual]:
            nova_dist = dist_atual + peso

            if nova_dist < distancias[vizinho]:
                distancias[vizinho] = nova_dist
                heapq.heappush(fila, (nova_dist, vizinho))

    return distancias

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