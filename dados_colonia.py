# DICIONÁRIO CONTENDO INFORMAÇÕES SOBRE OS MÓDULOS:

modulos = {
"Habitação": {
    "consumo": 20,
    "prioridade": 5,
    "armazenamento": 100,
    "comunicacao":"Alta",
    "status": "Ativo", 
    },

"Centro de Controle": {
    "consumo": 30,
    "prioridade": 5,
    "armazenamento": 50,
    "comunicacao": "Muito Alta",
    "status": "Ativo", 
    },

"Armazenamento de Energia": {
    "consumo": 10,
    "prioridade": 5,
    "armazenamento": 500,
    "comunicacao": "Média",
    "status": "Ativo", 
    },

"Agricultura": {
    "consumo": 15,
    "prioridade": 3,
    "armazenamento": 200,
    "comunicacao": "Baixa",
    "status": "Ativo", 
    },

"Laboratório Científico": {
    "consumo": 18,
    "prioridade": 3,
    "armazenamento": 80,
    "comunicacao": "Alta",
    "status": "Ativo", 
    },

"Comunicação": {
    "consumo": 12,
    "prioridade": 4,
    "armazenamento": 60,
    "comunicacao": "Muito Alta",
    "status": "Ativo", 
    },

"Suporte Médico": {
    "consumo": 25,
    "prioridade": 5,
    "armazenamento": 120,
    "comunicacao": "Alta",
    "status": "Ativo", 
    },

"Produção de Oxigênio": {
    "consumo": 35,
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

# Matriz de adjacência do grafo

nome_modulos = [
    "Habitação",
    "Centro de Controle",
    "Armazenamento de Energia",
    "Agricultura",
    "Laboratório Científico",
    "Comunicação",
    "Suporte Médico",
    "Produção de Oxigênio"
]

# Matriz de adjacência representando as conexões entre os módulos

matriz_adjacencia = [
    [0, 5, 0, 0, 0, 0, 3, 0],  # Habitação
    [5, 0, 6, 0, 7, 4, 0, 0],  # Centro de Controle
    [0, 6, 0, 5, 0, 0, 0, 4],  # Armazenamento de Energia
    [0, 0, 5, 0, 4, 0, 0, 0],  # Agricultura
    [0, 7, 0, 4, 0, 3, 0, 0],  # Laboratório Científico
    [0, 4, 0, 0, 3, 0, 0, 0],  # Comunicação
    [3, 0, 0, 0, 0, 0, 0, 2],   # Suporte Médico
    [0, 0, 4, 0, 0, 0, 2, 0]    # Produção de Oxigênio
    ]


# Representação da matriz 

def mostrar_matriz():
    print("\nMatriz de Adjacência\n")
    for linha in matriz_adjacencia:
        print(linha)

mostrar_matriz() 

