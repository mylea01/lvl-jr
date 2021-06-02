# simulação de dados
import random
dice = [1, 2, 3, 4, 5, 6]
quest = str(input('Você quer jogar o dado? -> '))
resp = ['sim', 'nao']
if quest == resp[0]:
    d = random.choice(dice)
    print(d)
else:
    print('')
print('done')
