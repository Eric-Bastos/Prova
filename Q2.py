num1= float(input('Digite a primeira nota: '))
num2= float(input('Digite a segunda  nota: '))
num3= float(input('Digite a terceira nota: '))

media = ( num1+num2+num3)/3
if(media>=7):
    print(f'Você foi aprovado!!, com  {media:.1f} de média')
elif(media>=5 and media<=6.9):
    print(f'Você foi para recuperação, com {media:.1f} de média')
else:
    print(f'Você foi reprovado!!, com {media:.1f} de média')    
