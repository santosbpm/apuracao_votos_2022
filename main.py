from json import loads
from time import sleep

import os
import requests


def clear():  # Limpar o terminal como uma atualização
    os.system('cls' if os.name == 'nt' else 'clear')


def formatar(cand, vot, porc):  # Formatação para parecer como um tabela
    print(f"{cand: ^18}│ {vot: ^16}│ {porc: ^16}")


if __name__ == '__main__':
    while True:
        try:
            data = requests.get(  # URL com dados em json da apuração do TSE
                'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')
            json_data = loads(data.content)
            total_votos = json_data['pst']  # Obtém do dicionário a porcetagem total de votos
        except ValueError as e:
            clear()
            print("ocorreu um erro. voltaremos logo! :)")
            print(f"\nErro: {e}")
            continue

        candidato = []
        votos = []
        porcentagem = []

        formatar('Candidato', 'Nº de Votos', 'Porcentagem')
        print(51*'─')

        for informacoes in json_data['cand']:  # Laço que busca cada candidato no arquivo json
            if int(informacoes['seq']) in range(1, 5):  # Controle para pegar informação de 4 candidatos
                formatar(informacoes['nm'], informacoes['vap'], informacoes['pvap'])

        print(f'\nTotal de votos apurados: {total_votos}%')
        sleep(5)
        clear()
