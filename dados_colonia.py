import heapq
from collections import deque
# DICIONÁRIO CONTENDO INFORMAÇÕES SOBRE OS MÓDULOS:

modulos = {
"Habitação": {
    "consumo": (20,),
    "prioridade": 5,
    "armazenamento": 100,
    "comunicacao":"Alta",
    "status": "Ativo", 
    },

"Centro de Controle": {
    "consumo": (30,),
    "prioridade": 5,
    "armazenamento": 50,
    "comunicacao": "Muito Alta",
    "status": "Ativo", 
    },

"Armazenamento de energia": {
    "consumo": (10,),
    "prioridade": 5,
    "armazenamento": 500,
    "comunicacao": "Média",
    "status": "Ativo", 
    },

"Agricultura": {
    "consumo": (15,),
    "prioridade": 3,
    "armazenamento": 200,
    "comunicacao": "Baixa",
    "status": "Ativo", 
    },

"Laboratório científico": {
    "consumo": (18,),
    "prioridade": 3,
    "armazenamento": 80,
    "comunicacao": "Alta",
    "status": "Ativo", 
    },

"Comunicação": {
    "consumo": (12,),
    "prioridade": 4,
    "armazenamento": 60,
    "comunicacao": "Muito Alta",
    "status": "Ativo", 
    },

"Suporte Médico": {
    "consumo": (25,),
    "prioridade": 5,
    "armazenamento": 120,
    "comunicacao": "Alta",
    "status": "Ativo", 
    },

"Produção de oxigênio": {
    "consumo": (35,),
    "prioridade": 5,
    "armazenamento": 300,
    "comunicacao": "Alta",
    "status": "Ativo", 
    }
}

# GRAFO DA COLÔNIA 
# Cada conexão representa um peso, o preso representa : distância / custo energético / tempo

grafo = {
    "Habitação": [ 
    ("Centro de Controle", 5),
    ("Suporte Médico", 3) 
     ],

    "Centro de Controle": [
     ("Habitação", 5), 
     ("Comunicação", 4), 
     ("Armazenamento de Energia", 6), 
     ("Laboratório Científico", 7) 
        ], 

    "Armazenamento de Energia": [ 
    ("Centro de Controle", 6), 
     ("Produção de Oxigênio", 4), 
     ("Agricultura", 5) 
        ], 

    "Agricultura": [ 
    ("Armazenamento de Energia", 5), 
     ("Laboratório Científico", 4) 
        ], 

    "Laboratório Científico": [
    ("Agricultura", 4), 
     ("Comunicação", 3), 
     ("Centro de Controle", 7) 
        ], 

    "Comunicação": [ 
    ("Centro de Controle", 4), 
    ("Laboratório Científico", 3) 
        ], 

    "Suporte Médico": [ 
    ("Habitação", 3), 
     ("Produção de Oxigênio", 2) 
        ],

    "Produção de Oxigênio": [ 
    ("Armazenamento de Energia", 4), 
    ("Suporte Médico", 2) 
        ] 
    }

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