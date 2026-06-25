from algoritmos import (
    dijkstra,
    bfs,
    dfs,
    prever_consumo,
    reconstruir_caminho,
    consumo_total,
    simular_falha,
    consultar_modulo
)
from dados_colonia import (
    modulos,
    grafo
)


#coleta de dados para busca pelo usuário 

def executar_rota():

    origem = input("Digite o módulo de origem: ")
    destino = input("Digite o módulo de destino: ")

    if origem not in grafo:
        print("Módulo de origem inválido.")
        return

    if destino not in grafo:
        print("Módulo de destino inválido.")
        return

    distancias, anteriores = dijkstra(
        grafo,
        origem
    )

    caminho = reconstruir_caminho(
        anteriores,
        destino
    )

    print("\nMelhor rota:")

    for modulo in caminho:
        print(modulo)

    print(
        "\nCusto total:",
        distancias[destino]
    )

#menu
while True:
    print("\nMenu:")
    print("1. Mostrar módulos")
    print("2. Executar BFS")
    print("3. Executar DFS")
    print("4. Calcular melhor rota")
    print("5. Consumo total")
    print("6. Simular falha")
    print("7. Consultar módulo")
    print("8. Prever consumo")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
       print("\nMÓDULOS DA COLÔNIA:\n")
       for modulo in modulos:
           print("-", modulo)
    elif opcao == "2":
        print("\nExecutando BFS")
        inicio = input("Digite o módulo de origem: ")
        bfs(grafo, inicio)
    elif opcao == "3":
        print("\nExecutando DFS")
        inicio = input("Digite o módulo de origem: ")
        dfs(grafo, inicio)
    elif opcao == "4":
        executar_rota()
    elif opcao == "5":
        total = consumo_total(modulos)
        print("\nConsumo total de energia:", total)
    elif opcao == "6":
        modulo = input(
            "Digite o módulo que apresentou falha: "
        )
        simular_falha(
            modulos,
            modulo
        )
    elif opcao == "7":
        modulo = input("Digite o nome do módulo: ")
        consultar_modulo(
            modulos,
            modulo
        )
    elif opcao == "8":
        quantidade = int(
            input("Quantidade de módulos: ") 
        )
        consumo = prever_consumo(
            quantidade
        )
        print(
            f"\nPrevisão de consumo de energia: {consumo} kW"
        )
    elif opcao == "0":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
