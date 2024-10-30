def calcular_preco_passagem(Dist):
    if Dis<=200:
        preço= Dis*0.50
    else:
        preço= Dis*0.45
    return preço        


Dis=int(input('Digite a distancia que você deseja percorrer: '))
preço=calcular_preco_passagem(Dis)

print(f'O preço que você vai pagar de passagem é  R$ {preço}')