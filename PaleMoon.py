import sys

print('Você está em uma sala escura. A luz da lua entra pela janela.')
print('Há OURO no canto da sala, junto com uma PÁ e uma CORDA.')
print('Há uma PORTA porta o LESTE.')

print('\n Comando?')
comando = input('\n ->')
if comando == 'pegar ouro' or comando == 'PEGAR OURO'or comando == 'Pegar Ouro' or comando == 'Pegar ouro':
     print('Você pegou o ouro!')
else:
    sys.exit()

print('\n Comando?')
comando = input('\n -> ')
if comando == 'pegar pá' or comando == 'pegar pa' or  comando == 'PEGAR PÁ' or comando == 'Pegar pá' or comando ==  'PEGAR PA' or comando =='Pegar pa':
    print('Você pegou a pá!')
else:
     sys.exit()

print('\n Comando?')
comando = input('\n -> ')
if comando == 'pegar corda' or comando == 'Pegar corda' or comando ==  'PEGAR CORDA' or comando == 'Pegar Corda':
    print('Você pegou a corda!')
else:
     sys.exit()

print('\n Você vê uma porta ao LESTE.')
print('\n Comando?')
comando = input('\n -> ')
if comando == 'Abrir porta' or comando == 'ABRIR PORTA' or comando == 'Abrir Porta' or comando == 'abrir porta':
    print('Você abriu a porta!')
else:
    sys.exit()


print('\n Comando?')
comando = input('\n -> ')
if comando == 'LESTE' or comando == 'leste' or comando == 'Leste':
    print('--------------------------')
    print('\n Pegue sua recompensa.')
    print('\n LUA PÁLIDA SORRI PARA VOCÊ.')
    print('\nVocê está em uma floresta. Existem caminhos para o NORTE, OESTE e LESTE.')
    print('\n Comando?')

    comando = input('\n -> ')
    if comando == 'NORTE' or comando == 'Norte' or comando == 'norte':
        print('--------------------------')
        print('\n Pegue sua recompensa.')
        print('\n LUA PÁLIDA SORRI PARA VOCÊ.')
        print('\nVocê está em uma floresta. Existem caminhos para o NORTE, SUL e LESTE.')
        print('\n Comando?')
    else:
        sys.exit()

    comando = input('\n -> ')
    if comando == 'SUL' or comando == 'sul' or comando == 'Sul':
        print('--------------------------')
        print('\n Pegue sua recompensa.')
        print('\n LUA PÁLIDA SORRI PARA VOCÊ.')
        print('\nVocê está em uma floresta. Existem caminhos para o NORTE, SUL e LESTE.')
        print('\n Comando?')
    else:
        sys.exit()

    comando = input('\n -> ')
    if comando == 'NORTE' or comando == 'Norte' or comando == 'norte':
        print('--------------------------')
        print('\n Pegue sua recompensa.')
        print('\n LUA PÁLIDA SORRI PARA VOCÊ.')
        print('\nVocê está em uma floresta. Existem caminhos para o NORTE, SUL e OESTE.')
        print('\n Comando?')
    else:
        sys.exit()

    comando = input('\n -> ')
    if comando == 'OESTE' or comando == 'Oeste' or comando == 'oeste':
        print('--------------------------')
        print('\n Pegue sua recompensa.')
        print('\n LUA PÁLIDA SORRI PARA VOCÊ.')
        print('\nVocê está em uma floresta. Existem caminhos para o SUL, LESTE e OESTE.')
        print('\n Comando?')
    else:
        sys.exit()

    comando = input('\n ->')

else:
    sys.exit()


