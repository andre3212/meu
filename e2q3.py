segundos = int(input("Digite a quantidade de segundos: "))
horas = segundos // 3600 # horas recebe a quantidade de horas
restoh = segundos%3600 
minutos = restoh//60
seg = restoh%60 

print(f'{horas}:{minutos}:{seg}')
