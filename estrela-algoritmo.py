def main():
    cidadePartida = {}
    cidadePartida['nome'] = input('Nome da cidade de partida: ')
    cidadePartida['km_ate_chegada'] = float(input('Km até a chegada: '))
    cidadePartida['custo'] = 0
    print('')

    cidadeChegada = {}
    cidadeChegada['nome'] = input('Nome da cidade de chegada: ')
    cidadeChegada['km_ate_chegada'] = 0
    cidadeChegada['custo'] = 0
    print('')

    qtdEtapas = int(input('Quantidade de etapas: '))
    qtdCaminhos = int(input('Quantidade de caminhos possíveis: '))
    print('')

    cidades = {}
    for i in range(qtdEtapas):
        cidades[i] = {}
        for x in range(qtdCaminhos):
            cidades[i]['nome'] = input(f'Nome cidade etapa {i} caminho {x}: ')
            cidades[i]['km_ate_chegada'] = int(input(f'Km até a chegada: '))
            cidades[i]['custo'] = int(input(f'Custo cidade etapa {i} caminho {x}: '))
            print('')

    f = 0

    f = cidadePartida['custo'] + cidadePartida['km_ate_chegada']

    decisao = {}
    for i in range(qtdEtapas):
        for x in range(qtdCaminhos):
            decisao[x] = int(cidades[i]['custo'] + cidades[i]['km_ate_chegada'])

        menor = 1000000000  # supondo que o f nunca será maior que isso...
        for d in range(len(decisao)):
            if menor > decisao[d]:
                menor = decisao[d]

        f += menor

    print(f'O custo da cidade de partida até a cidade de chegada: {f}')


main()
