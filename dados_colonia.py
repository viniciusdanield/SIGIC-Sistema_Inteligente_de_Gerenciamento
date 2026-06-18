# DICIONÁRIO CONTENDO INFORMAÇÕES SOBRE OS MÓDULOS:


modulos = {
"Habitação": {
    "consumo": ,
    "prioridade": ,
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