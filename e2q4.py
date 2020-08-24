lista = []
for n in range(1, 6): # algoritmo pede a entrada de cinco valores e forma uma lista
    numero= int(input())
    lista.append(numero)

maximo =max(lista) # valor maxímo digitado pelo usuário
minimo = min(lista) #valor minimo digitado pelo usuário
media = (sum(lista))/5 #média aritmetica dos valores digitados
print(f'A maior numero digitádo é {maximo}, o menor é {minimo} e a média aritmetica é {media}')
