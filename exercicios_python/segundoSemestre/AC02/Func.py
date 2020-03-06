# nome: Vinicius Tertuliano da silva Ra:1901646
# nome: Adalberto gonçalves lira junior RA:1901584
dados = []


def salar(dados):
    if 'DESENVOLVEDOR' in dados[3]:
        if 3000 <= dados[2]:
            dados[2] *= 0.80
            return dados[2]
        else:
            dados[2] *= 0.90
            return dados[2]
    elif 'ANALISTA' in dados[3]:
        if 2000 <= dados[2]:
            dados[2] *= 0.75
            return dados[2]
        else:
            dados[2] *= 0.85
            return dados[2]
    elif 'GERENTE' in dados[3]:
        if 5000 <= dados[2]:
            dados[2] *= 0.70
            return dados[2]
        else:
            dados[2] *= 0.80
            return dados[2]
