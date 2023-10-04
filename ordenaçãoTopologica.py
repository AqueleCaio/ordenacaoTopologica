
def ordenacaoTopologicaKahn(listaAdj):
    # Inicialize o grau de entrada de todos os vértices como 0
    grauEntrada = [0] * len(listaAdj)

    # Atualize o grau de entrada de todos os vértices
    for i in range(len(listaAdj)):
        for j in listaAdj[i]:
            grauEntrada[j] += 1

    # Crie uma fila e adicione todos os vértices com grau de entrada 0
    fila = [i for i in range(len(grauEntrada)) if grauEntrada[i] == 0]

    # Inicialize a lista de ordenação topológica
    ordenacaoTopologica = []

    # Enquanto a fila não estiver vazia
    while fila:
        # Remova um vértice da fila
        v = fila.pop(0)

        # Adicione o vértice à lista de ordenação topológica
        ordenacaoTopologica.append(v)

        # Para cada vértice adjacente ao vértice removido
        for i in listaAdj[v]:
            # Reduza o grau de entrada do vértice adjacente em 1
            grauEntrada[i] -= 1

            # Se o grau de entrada do vértice adjacente se tornar 0, adicione-o à fila
            if grauEntrada[i] == 0:
                fila.append(i)

    # Se a lista de ordenação topológica contém todos os vértices, retorne a lista
    if len(ordenacaoTopologica) == len(listaAdj):
        print(ordenacaoTopologica) 

    # Caso contrário, o grafo não é um DAG
    print("NÃO DAG") 

    
    