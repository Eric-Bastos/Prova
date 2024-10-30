limite= 80
multa= 5.00

velocidade= int(input('Digite a velocidade do carro: '))

excesso= (velocidade - limite)
pagar= (excesso * multa)
if(velocidade>limite):
    print(f'O veiculo foi Multado!!, e vai pagar R$ {pagar} ')
else:
    print('O veiculo não foi multado!!')
