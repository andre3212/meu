segundos = int(input())
horas = segundos // 3600
restoh = segundos%3600
minutos = restoh//60
seg = restoh%60 

print(f'{horas}:{minutos}:{seg}')
