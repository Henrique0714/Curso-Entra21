# def situacao():
#     if dic["nota"] >= 7 and dic["nota"] <=10:
#         return "Aprovado"
#     elif dic["nota"] >= 10 or dic["nota"] < 0:
#         return "Invalido"
#     else:
#         return "Reprovado"
#
# dic = {"nome": input("digite seu nome: "),
#        "nota": float(input("digite sua nota: "))}
#
# print(dic["nome"])
# print(dic["nota"])
# print(situacao())


# from random import randint
# from operator import itemgetter
#
# dic = {}
# for i in range(1, 5):
#     dic[f'jogador{i}'] = randint(1, 6)
#
# dic2 = sorted(dic.items(), key=itemgetter(1), reverse=True)
#
# for i, dic in enumerate(dic2):
#     print(f'{i + 1} - {dic2[i]}')

from datetime import date

dicionario = {}
ano_atual = date.today().year
dicionario['nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de nascimento: '))
dicionario['idade'] = ano_atual - ano_nascimento
dicionario['ctps'] = int(input('Número da carteira de trabalho (0 se não tiver): '))
if dicionario['ctps'] > 0:
    dicionario['contratação'] = int(input('Ano de contratação: '))
    dicionario['salario'] = float(input('Salário: R$'))
    dicionario['aposentadoria'] = dicionario['contratação'] + 35
print(dicionario)

for chave, valor in dicionario.items():
    if chave == 'ctps':
        if valor == 0:
            print('Não tem carteira de trabalho.')
    else:
        print(f'O campo {chave} tem o valor {valor}.')




