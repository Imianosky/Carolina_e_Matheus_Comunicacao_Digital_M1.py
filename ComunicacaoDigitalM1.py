# Arquivo: ComunicacaoDigitalM1.py
# Autores: Carolina Imianosky e Matheus Kreutz
# Criado em 20 de março de 2021 
# Modificado em 29 de março de 2021

import random

# Define os locais dos bits de paridade
def definir_locais(data):
    i = 1
    j = 0
    aux = 1
    while True:
        if data[j] == 'f':          # Caso f chegou no fim
            break
        if i == aux:                # Caso aux igual o indice é o local do bit
            aux += aux
            send.append('p')        # coloca um p no local do bit de paridade
        else:
            send.append(data[j])    # coloca o valor do x representante
            j += 1
        i += 1                      # aumenta o tamanho do pulo para o proximo bit

# define a quantidade de bits de Paridade
def def_qntBParidade():
    qntBParidade = 0
    for valor in send:              # verifica todos os valores do valor a ser enviado
        if valor == 'p':            # caso encontra um p
            qntBParidade += 1       # adiciona a quantidade
    return qntBParidade

# adiciona os valores calcularos dos bits de paridade no valor a ser enviado
def colocar_Bparidade():
    i = 0
    j = 0
    while i < qnt:
        if send[i] == 'p':              # caso encontra um p
            send[i] = bParidade[j]      # adiciona o bit de paridade
            j += 1                      # vai para o proximo bit a ser inserido
        i += 1

# calcula os bits de paridade
def def_BParidade():
    p = 'f'                             # declaração para pegar o primeiro valor
    j = 1                               # j = tamanho do pulo e inicio do laço
    aux = 0
    qntBParidadeAux = qntBParidade
    while qntBParidadeAux > 0:              # laço que vai ocorrer até todos os bits de paridade serem prenchidos
        i = j - 1                           # define o inicio
        while i < qnt:                      # laço que percorre o send
            while aux < j and i < qnt:      # laço que percorre dentro de cada pulo
                if send[i] != 'p':          # caso for p não é calculo pois é onde possue o bit de paridade
                    if p == 'f':            # caso achar o f(first)
                        p = send[i]         # colocar o primeiro valor a ser calculo
                    else:
                        p = p != send[i]    # faz XOR com cada valor e armazena esse valor no p
                aux += 1                    # indece entre os pulos
                i += 1
            i = i + j                       # aumenta o indece geral com o pulo
            aux = 0
        j = j + j                           # aumenta a distancia do pulo
        bParidade.append(int(p))            # adiciona o bit de paridade
        qntBParidadeAux -= 1
        p = 'f'                             # reseta o valor de first

# calcula o local do erro
def verifica_erro():
    j = 0
    i = 1
    aux = 1
    while True:                             # laço que coloca o local dos bits de paridade
        if valErro[j] == 'f':               # caso f chegou ao final do dado
            break
        if i == aux:                        # caso chegou no lugar do bit de paridade
            aux += aux
            sendErro.append('p')            # adiciona ao local
        else:
            sendErro.append(valErro[j])     # caso onde somente adiciona o valor do dado
            j += 1
        i += 1

    i = 0
    j = 0
    while i < qnt:                          # laço que adiciona os bits de paridade ja calculado na valor do erro
        if sendErro[i] == 'p':              # caso encontra o p
            sendErro[i] = bParidade[j]      # adiciona o bit de paridade
            j += 1                          # vai para o proximo bit de paridade
        i += 1

    k = 'f'
    aux = 0
    j = 1
    qntBParidadeAux = qntBParidade
    while qntBParidadeAux > 0:              # laço que calcula a posição do erro
        i = j - 1                           # define o inicio
        while i < qnt:                      # laço que percorre o sendErr
            while aux < j and i < qnt:      # laço que percorre dentro de cada pulo
                if k == 'f':                # caso achar o f(first)
                    k = sendErro[i]         # colocar o primeiro valor a ser calculo
                else:
                    k = k != sendErro[i]    # faz XOR com cada valor e armazena esse valor no k
                aux += 1                    # indece entre os pulos
                i += 1
            i = i + j                       # aumenta o indice geral com o pulo
            aux = 0
        j = j + j                           # aumenta a distancia do pulo
        kList.append(int(k))                # adiciona um bit do local
        qntBParidadeAux -= 1
        k = 'f'                             # reseta o valor de first


# Verifica se a palavra inserida é um num binário
def verificaBinario(texto):
    while True:
        try:
            num = input(texto)
        except ValueError:
            print("O valor inserido não está em binário!")
        else:
            for i in num:
                if i in "10":  # Caso o digito seja 1 ou 0
                    valBin = True
                else:
                    valBin = False
                    break
            if valBin == False:
                print("O valor inserido não está em binário!")
            else:
                if (ind == 1 and len(num) == tam):      # verificação para tamanho igual 8
                    break
                elif (ind == 2 and len(num) == tam):    # verificação para tamanho igual 11
                    break
                elif (ind == 3 and len(num) == tam):    # verificação se todos os valores são de mesmo tamanho caso livre
                    break
                elif tam == 0:                          # tamanho livre (variavel secreta)
                    break
                else:
                    print(f"Tamanho incorreto! Digite um valor binário de tamanho {tam}")
    return num


# soma dois numeros binarios de mesmo tamanho
def somaBinaria(b1, b2, size):
    resultado = ''
    carry = 0                                                           # zera a variavel de armaz. do carry
    for i in range(size - 1, -1, -1):                                   # loop para percorrer todos os bits das palavras

        bitAtual = carry                                                # soma os bits considerando o carry anterior
        bitAtual += 1 if b1[i] == '1' else 0
        bitAtual += 1 if b2[i] == '1' else 0

        resultado = ('1' if bitAtual % 2 == 1 else '0') + resultado     # caso o bitAtual seja 2 ou 3, resultado = 1
                                                                        # caso contrario resultado = 0

        carry = 0 if bitAtual < 2 else 1                                # para bitAtual > 1, carry = 1

    if carry != 0:                                                      # caso o carry nao seja 0
        palavraCarry = '0'
        for i in range(size - 2):                                       # zera a palavraCarry
            palavraCarry += '0'
        palavraCarry += '1'                                             # adiciona 1 ao final da palavraCarry
        resultado = somaBinaria(resultado, palavraCarry, size)          # recursividade para tratar os carrys dos proximos
                                                                        # bits da palavra

    return resultado

# percorre a palavra invertendo todos os bits
def bitFlip(b, size):
    resultado = ''
    for i in range(size):
        if b[i] == '1':
            resultado += '0'
        else:
            resultado += '1'
    return resultado


# percorre toda a palavra e verifica se existe algum 0
def verificaChecksum(b, size):
    for i in range(size):
        if b[i] == '0':                     # caso tenha algum 0 na palavra
            return False                    # retorna falso
    return True


# insere uma inversao de bits em uma posicao aleatoria da palavra
def erroComunicacao(b, size):
    resultado = ''                                  # inicializa a variavel resultado com vazio
    bitAleatorio = random.randint(0, 11)            # escolhe um bit aleatorio para inserir o erro
    for i in range(size):
        if i == bitAleatorio:                       # percorre a palavra ate o bit selecionado
            if b[i] == '1':                         # inverte o bit selecionado
                resultado += '0'                    # adiciona a variavel de resultado
            else:
                resultado += '1'
        else:
            resultado += str(b[i])                  # mantem o valor dos outros bits e adiciona no resultado

    return resultado


menu = ' '
while (menu != 'x'):
    menu = input('Escolha entre:'
                 '\n H - Codificação Hamming'
                 '\n C - Codificação Checksum '
                 '\n X - Sair\nR: ').lower()

    if (menu == 'h'):                               # caso escolha a codificacao Hamming
        tam = 0
        ind = int(input("\nEscolha o tamanho desejado: "
                        "\n 1 - Codigo de Hamming (12,8) "
                        "\n 2 - Tamanho do codigo de aluno (11) "
                        "\nR: "))

        if (ind == 1):                              # define a variavel tam de acordo com a selecao do usuario
            tam = 8
        elif (ind == 2):
            tam = 11
        elif ind == 0:
            tam = 0

        #recebe o valor do dado
        num = verificaBinario(f"\nDigite o valor em binario de tamanho {tam}: ")
        data = [int(x) for x in str(num)]
        data.append('f')            			                    # adiciona um fim

        send = []
        bParidade = []
        qntBParidade = 0

        #chamada de funções
        definir_locais(data)
        qntBParidade = def_qntBParidade()
        qnt = len(send)
        def_BParidade()
        colocar_Bparidade()

        print(send)

        tam = len(str(num))
        ind = 3

        num = verificaBinario("\nDigite o valor do erro: ")          # recebe o valor do erro
        valErro = [int(x) for x in str(num)]
        valErro.append('f')

        sendErro = []
        kList = []
        verifica_erro()
        print()
        print(kList)

    if (menu == 'c'):                                                 # caso escolha a codificação checksum

        tam = 11                                                      # codigo de alunos: Carol 6444830
        ind = 3                                                       # indice de tamanho livre na verificacao
        
        print("\nInsira as tres palavras binarias: ")
        x1 = verificaBinario("1) ")
        x2 = verificaBinario("2) ")
        x3 = verificaBinario("3) ")

        resultado = somaBinaria(str(x1), str(x2), tam)                # realiza a soma entre as palavras 1 e 2
        resultado = somaBinaria(resultado, str(x3), tam)              # realiza a soma do valor anterior com a palavra 3

        checksum = bitFlip(resultado, tam)                            # calcula o checksum
        print("\nPalavra de paridade(checksum): " + checksum)

        erro = input("\nDeseja inverter um bit?"                      # usuario seleciona se quer inserir erro na palavra
                     "\n 1 - sim "
                     "\n 2 - nao "
                     "\nR: ").lower()                                 
        while erro != "s" and erro != "n":
            print("Entrada incorreta, digite novamente.")
            erro = input("\nDeseja inverter um bit?"
                         "\n 1 - sim "
                         "\n 2 - nao "
                         "\nR: ")

        r1 = x1                                                       # variaveis das palavras recebidas
        r2 = x2
        r3 = x3

        if erro == '1':                                               # caso tenha sido selecionado p inserir o erro 
            palavraAleatoria = random.randint(0, 2)                   # aleatoriza uma das palavras p insercao do erro
            if palavraAleatoria == 0:
                r1 = erroComunicacao(x1, tam)                         # insere o erro na palavra recebida escolhida
            elif palavraAleatoria == 1:
                r2 = erroComunicacao(x2, tam)
            else:
                r3 = erroComunicacao(x3, tam)

        print("\nMensagem Recebida: ")
        print("A: " + r1)
        print("B: " + r2)
        print("C: " + r3)
        print("Checksum: " + checksum + "\n")

        rChecksum = somaBinaria(r1, r2, tam)                          # soma as palavras recebidas 1 e 2
        rChecksum = somaBinaria(rChecksum, r3, tam)                   # soma o valor anterior com a palavra recebida 3
        print("Soma das palavras recebidas: " + rChecksum)

        resultadoFinal = somaBinaria(rChecksum, checksum, tam)        # soma os checksums
        print("Soma dos checksums: " + resultadoFinal)

        print("Mensagem recebida corretamente.") if verificaChecksum(resultadoFinal, tam) else print("Falha nas mensagens.")
