print('Faça um programa em Python que carregue uma lista com os modelos de três carros:')

carro = []
litro = []
preco = float(4.90)
km = float(500)

for i in range(1,4):
    carro.append(str(input(f'Carro {i} : ')))
    litro.append(int(input('km por litro: ')))

print('='*80)

for i in range(len(carro)):
    tanque =float(km / litro[i])
    valor =float(tanque * preco)

    print(f' {carro[i]} - {litro[i]} - {tanque:.2f} litros - R$ {valor:.2f}')



