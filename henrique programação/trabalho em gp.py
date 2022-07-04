from isbntools.app import *
import random
import webbrowser

acao = ação = ["9780439951784 Northern Lights", "9788556510686  A Máquina do Tempo", "9788578270698  As Crônicas de Nárnia", "9788576164081 Lugar Nenhum", "9788595084742 O Hobbit",
               "9788556510853 O instituto", "9788599296011 Ponto de Impacto", "9788576572787 Star Wars - Marcas da Guerra", "9788595081758 Uma dobra no tempo", "9788532287465 Viagem ao Centro da Terra"]
romance = ['9788581636696 Simplesmente acontece', '9788580573268 Como eu era antes de você', '9788580572261 A Culpa é Das Estrelas', '9788544001820 Orgulho e preconceito', '9788582850404 Romeu e Julieta',
           '9788582850800 O corcunda de Notre-Dame', '9788594318237 O morro dos ventos uivantes', '9788525067425 A cinco passos de você', '9788581630625 P.S. Eu te amo', '9788551005415 Teto Para Dois']
infantil = ['9788574069357 Capitão Cueca e a revoltante revanche da Robocueca Radioativa', '9788543106595 Emocionário: Diga o que você sente', '9781589255517 I Love You to the Moon and Back',
            '9788574066707 Malala a menina que queria ir para a escola', '9788574120287 O grúfalo', '9788538069539 Turma da Mônica - Biblioteca de boas maneiras',
            '9788538078043 Fisher-Price - Como é bom ser gentil', '9788545202660 O Poder da Ação para a Criança', '9788537631324 Olha Quem Sou! Leão', '9788538058977 Perigoso!']
ficcao = ['9788532530783 Harry Potter e a pedra filosofal', '9788594318114 Frankenstein', '9788579605444 God Of War - Uma emocionante jornada pelos reinos fantásticos da mitologia nórdica',
         '9788580575408 O Mar de Monstros - Série Percy Jackson e os Olimpianos', '9788583682981 Star Wars Legends: Infinitos O Retorno de Jedi', '9788581050485 O iluminado',
         '9782352947943 Seul sur Mars', '9788516052560 Peter Pan', '9788594541758 Alice no País das Maravilhas', '9788525052698 Contos de Shakespeare']
terror = ['9788560280940 It: A coisa', '9788584424573 Drácula', '9788556510631 A assombração da Casa da Colina', '9788581052144 Misery: Louca obsessão', '9788581053042 O vilarejo',
          '9786555981735 Ossos do Ofício', '9788595086234 O Exorcista', '9788501404589 A última vítima', '9786555602241 Terra Faminta', '9788556510822 Terror a bordo: 17 histórias turbulentas']

while True:
    print(50*"-")
    recomendacao = int(input("\33[4:33m[1] Recomendação de Livro\n[2] Validar ISBN\n\33[m"))
    if recomendacao == 1:
        print(50 * "-")
        print("\n\33[4:33mRecomendação de Livros\33[m")
        print("""[1] Ação (Recomendação de Cairo)
[2] Romance (Recomendação de Cauã)
[3] Infantil (Recomendação de Afia)
[4] Ficção (Recomendação de Gustavo)
[5] Terror (Recomendação de Cauan)""")
        print(50 * "-")
        escolha = int(input("Sua Escolha: "))
        if escolha == 1:
            escolha_aleatoria = random.choice(acao)
            print(f"Sua recomendação é:{escolha_aleatoria[13:]}")
        if escolha == 2:
            escolha_aleatoria = random.choice(romance)W
            print(f"Sua recomendação é:{escolha_aleatoria[13:]}")
        if escolha == 3:
            escolha_aleatoria = random.choice(infantil)
            print(f"Sua recomendação é:{escolha_aleatoria[13:]}")
        if escolha == 4:
            escolha_aleatoria = random.choice(ficcao)
            print(f"Sua recomendação é:{escolha_aleatoria[13:]}")
        if escolha == 5:
            escolha_aleatoria = random.choice(terror)
            print(f"Sua recomendação é:{escolha_aleatoria[13:]}")
        isbn = escolha_aleatoria
        isbn_lista = list(isbn)

    if recomendacao == 2:
        isbn = str(input("\33[4:33mISBN: \33[m"))
        isbn_lista = list(isbn)
        if len(set(isbn_lista)) == 1:
            print("\33[4:31mISBN Invalido!\33[m")
            exit()
        if len(isbn_lista) > 13:
            print("\33[4:31mLimite de caracterias do ISBN excedeu o limite!\33[m")
            exit()

    contador = 1
    contador2 = 0
    soma_while = 0
    soma2_while = 0
    while contador < 12:
        soma_while += int(isbn_lista[contador]) * 3
        contador += 2
    while contador2 < 11:
        soma2_while += int(isbn_lista[contador2]) * 1
        contador2 += 2
    total_while = soma_while + soma2_while + int(isbn_lista[12])
    verificacao = total_while % 10

    if verificacao == 0:
        if recomendacao == 2:
            print("\33[4:32mISBN Valido!\33[m")
        print(isbn[0:3], "-", isbn[3], "-", isbn[4:8], "-", isbn[8:12], "-", isbn[12], sep="")
        print("")
        try:
            print(50 * "-")
            print(registry.bibformatters['labels'](meta(isbn)))
            print()
            print(50 * "-")
            informacao = int(input("\33[4:33m\nDesejas mais informações?\n[1] Sim\n[2] Não\n\33[m"))
            print(50 * "-")
            if informacao == 1:
                webbrowser.open(f"https://www.amazon.com.br/s?k={isbn}")
        except:
            informacao = int(input("\33[4:33mDeseja informação sobre o livro?\n[1] Sim\n[2] Não\n\33[m"))
            if informacao == 1:
                webbrowser.open(f"https://www.amazon.com.br/s?k={isbn}")
    else:
        print(50 * "-")
        print("\33[4:31mISBN Invalido![m")
    saida = int(input("\33[4:33m[1] Deseja continuar\n[2] Deseja parar\n\33[m"))
    print(50 * "-")
    if saida == 2:
        break