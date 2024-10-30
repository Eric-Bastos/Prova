salario=int(input('Digite o seu salario: '))
casa=int(input('Digite o valor da casa: '))
anos=int(input('Digite a quantidade de anos: '))
qprest= anos*12

prestação= casa/qprest

if(prestação>salario*0.30):
    print('Infelizmente você não pode obter o emprestimo!! ')
else:
    print(f'Emprestimo ok, você vai pagar de prestação R$ {prestação:.2f}')    
