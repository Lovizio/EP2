import random

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

#Terceira Função

def navio_pode_ser_alocado(mapa, navio_tamanho, linha, coluna, orientacao):
    n = len(mapa)
    if orientacao == 'h':
        if coluna + navio_tamanho > n:
            return False
        for j in range(coluna, coluna + navio_tamanho):
            if mapa[linha][j] != ' ':
                return False
    else:  
        if linha + navio_tamanho > n:
            return False
        for i in range(linha, linha + navio_tamanho):
            if mapa[i][coluna] != ' ':
                return False
    return True

def aloca_navios(mapa, blocos):
    n = len(mapa)
    for navio_tamanho in blocos:
        alocado = False
        while not alocado:
            linha = random.randint(0, n-1)
            coluna = random.randint(0, n-1)
            orientacao = random.choice(['h', 'v'])
            
            if navio_pode_ser_alocado(mapa, navio_tamanho, linha, coluna, orientacao):
                if orientacao == 'h':
                    for j in range(coluna, coluna + navio_tamanho):
                        mapa[linha][j] = 'N'
                else:  
                    for i in range(linha, linha + navio_tamanho):
                        mapa[i][coluna] = 'N'
                alocado = True
    return mapa

#Quarta Função
def foi_derrotado(tabuleiro):
   
    for linha_atual in tabuleiro:
        
        for celula in linha_atual:
            
            if celula == 'N':
                
                return False

  
    return True