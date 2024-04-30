#Primeira Funçao: Cria matriz quadrada de espaços
def cria_mapa(N):

    mapa = []

    for i in range(N):
        
        linha = []

        for j in range(N):
            
            linha.append(' ')

        mapa.append(linha)

    return mapa
