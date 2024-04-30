#Primeira Funçao: Cria matriz quadrada de espaços
def cria_mapa(N):

    mapa = []

    for i in range(N):
        
        linha = []

        for j in range(N):
            
            linha.append(' ')

        mapa.append(linha)

    return mapa

#Segunda Funçao: Navio pode ser alocado na posição?
def posicao_suporta(mapa, blocos, linha, coluna, orientacao):
    n = len(mapa)  

    if orientacao == 'v':  
        
        if linha + blocos > n:
            return False
        
        for i in range(blocos):
            if mapa[linha + i][coluna] != ' ':
                return False

    elif orientacao == 'h':  
        if coluna + blocos > n:
            return False
        
        for j in range(blocos):
            if mapa[linha][coluna + j] != ' ':
                return False

    return True  