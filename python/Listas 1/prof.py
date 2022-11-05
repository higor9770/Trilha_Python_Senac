print('Bem vindos! Aqui está o feedback de vocês do Projeto Piloto:)')
codigo = input('Informe o código para entrar: ')

if(codigo == 'EFGH' or codigo == 'efgh'):
    print('-'*60) 
    print('Olá, Thaís e Higor! Para ver o feedback, responda essa charada.')
    c = '''
            Ocorre uma vez a cada minuto, duas vezes a cada momento, mas jamais a cada quinhentos anos.  

        ''' #mudei a charada
    print(c)
    resposta = str(input('Digite a palavra aqui: '))
    if resposta == 'm' or resposta == 'M':  #mudei a respota da charada
        print('-' * 60)
        print('Parabéns! Você acertou. Passou de fase')
        print('-' * 60)
        print('VERIFICANDO SE VOCÊ SE LEMBRA DO ASSUNTO DE PREMISSAS. hehehe ')
        print('\n')
        print('Hoje está chovendo. Paula tem três filhos.\nPortanto vai chover na quinta feira.')
        print('Qual a conclusão e a(s) premissa(s) da afirmação acima?')
        opcao = int(input('\n(1) Não é um premissa válida\n(2)A afirmação “hoje está chovendo” e “Paula tem três filhos” são as premissas e a conclusão é: “vai chover quinta feira”.\nDigite a opcão correta:'))
        if(opcao == 1):
            print('-' * 60)
            print('Parabéns! Você acertou.')
            print('FEEDBACK')
            f = '''CARACTERÍSTICAS ATENDIDAS DO PROJETO PILOTO\n 
                               Escopo: Atendeu a documentação
                               Objetivo: Realista 
                               Ideia: Bem interessante
                               Engajamento: Satisfatório
                               Categoria: Negócios
                               Apresentação: Satisfatória  
                            '''
            print(f)
            print('PARABÉNS! O PROJETO ATENDEU O PROPÓSITO!')
        elif opcao == 2:
            print('!'*90)
            f = '''
                        Precisa revisar sobre premissas.
                        FEEDBACK:
                        Não terá feedback você errou o pré-requisito!
                        Sorry!  
               '''
            print(f)
            print('!'*90)

    elif resposta != 'm' or resposta != 'M':
        print('Erradissimo!\n') #tirei a resposta pós erro
        print('*'*60)
        print('Segunda chance.')
        print('Sobe, sobe, sobe e jamais desce.') #mudei a charada
        resposta2 = input('Digite a palavra aqui: ')
        if(resposta2 == 'idade'or resposta == 'Idade' or resposta == 'IDADE'): #mudei a reposta da charada e coloquei de diferentes modos
            print('-' * 60) 
            print('parabéns! Vocês são bons hein!')
            print('FEEDBACK') 
            f = '''CARACTERÍSTICAS ATENDIDAS DO PROJETO PILOTO\n 
                            Escopo: Atendeu a documentação
                            Objetivo: Realista 
                            Ideia: Bem interessante
                            Engajamento: Satisfatório
                            Categoria: Negócios
                            Apresentação: Satisfatória   
                        '''
            print(f)
            print('PARABÉNS! O PROJETO ATENDEU O PROPÓSITO!')
        else:
            print('Errou novamente!') #tirei a resposta pós erro
            opcao = int(input('Tentar novamente?\n(1) Sim\n(2) Não\nDigite aqui: '))
            if(opcao == 1):
               charada = '''
                           Você me tem hoje e amanhã você me terá ainda mais. Conforme o tempo passa, eu não sou nada fácil de guardar. Não ocupo nenhum espaço, mas estou sempre num único lugar. Eu sou o que você viu, não o que você vê.
                        '''
               print(charada)
               print('Dica: todos nós temos!')
               resposta3 = input('Digite a palavra aqui: ')
               if(resposta3 == 'memória' or resposta3 == 'MEMÓRIA' or resposta=='Memória'): #coloquei uma nova charada
                    print('-'*60)
                    print('Wow! Como vocês são bons em charadas!')
                    print('Mereceu receber o feedback!')
                    print('FEEDBACK')
                    f = '''
                            CARACTERÍSTICAS ATENDIDAS DO PROJETO PILOTO\n 
                             Escopo: Atendeu a documentação
                             Objetivo: Realista 
                             Ideia: muito interessante 
                             Engajamento: bom
                             Categoria: Negócios
                             Apresentação: muito boa  
                        '''
                    print(f)
                    print('PARABÉNS! O PROJETO ATENDEU O PROPÓSITO!')
                    print('A reposta das outras duas charadas são: 1- M, 2- idade e 3-memória') #coloquei a reposta no final caso a pessoa erre duas vezes e acerta a última
               else:
                    print('Poxa! Errou novamente!Tente novamente em outra compilação.')
            else:
                print('Programa encerrado sem feedback :(')
else:
    print('Intruso querendo verificar o feedback do coleguinha!')
    print('Comando encerrado para verificação')