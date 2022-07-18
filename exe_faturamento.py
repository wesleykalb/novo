# projeto de calculo de faturamento onde tive como base, um arquivo .txt com o numero da venda
# e o valor de cada venda
# ================================================= #
# abrindo o arquivo .txt com os dados

with open("vendasloja.txt", 'r') as a:
    texto = a.read()
b = texto.split('\n')
# removendo a primeira linha onde contem as informações do numero da venda e venda
texto = b[1:]

# criado um painel que contem informações e comandos para o usuario acessar


def painel_comando():
    global texto
    operacao = 0
    while operacao != '3':
        print('===============================')
        print('Bem vindo ao painel de comando.')
        print('===============================')
        print('digite 1 para remover uma venda: \n'
              'digite 2 para adicionar uma nova venda: \ndigite 3 para continuar'
              ' para a soma do faturamento:  \ndigite 0 para voltar ao menu inicial: ')
        operacao = input()

# função para remover vendas, onde o usuario informa o numero da venda e o valor

        def remover_venda():
            if operacao == '1':
                remover = input('informe o numero da venda: ') + ';'
                remover = remover + input('agora informe o valor da venda: ')
                if remover in texto:
                    texto.remove(remover)
                else:
                    print('informe um numero ou valor de venda corretos: ')
                    remover = input() + ';'
                    remover = remover + input('agora informe o valor da venda: ')
        remover_venda()

# função para adicionar vendas, onde o usuario informa o numero da venda e o valor

        def add_venda():
            if operacao == '2':
                num_venda = input('informe o numero da venda: ') + ';'
                valor_venda = input('informe o valor da venda: ')
                nova_venda = num_venda + valor_venda
                adionando = texto.append(nova_venda)
        add_venda()


painel_comando()
# formando um laço para somar os valores que estao apos o ';' onde contem o valor de cada venda


def soma_valores():
    faturamento = 0
    for linha in texto:
        c = linha.find(';')
        valor = float(linha[c + 1:])
        faturamento += valor
    return faturamento


print(soma_valores())
# no final do projeto sera apresentado o valor do faturamento





