# 5. Desafio  Faça uma tabela de jogos para mostrar um campeonato que
# tem 3 times.
#  Deve construir duas listas, com os nomes de 3 times. As duas
# listas deve ter os mesmos nomes dos times.
#  Deve construir dois for, o primeiro recebe o time1 e o segundo o
# time2.
#  Faça uma condição SE (if) para identificar se os times estão
# sorteados diferentes. Use esse comando: if time1 != time2 :


pote1 = ['sport', 'nautico', 'santa']
pote2 = ['sport', 'nautico', 'santa']
for time1 in pote1:
    for time2 in pote2:
        if time1 != time2:
            print(f'{time1}','x', f'{time2}')