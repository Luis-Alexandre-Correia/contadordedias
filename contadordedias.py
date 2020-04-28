Quantidade_de_segundos = input("insira a quantidade de segundos: ")
Segundos_total = int(Quantidade_de_segundos)
dias =Segundos_total//86400
horas_restantes = Segundos_total%86400
horas = horas_restantes//3600
minutos_restantes = horas_restantes%3600
minutos = minutos_restantes//60
segundos= minutos_restantes%60
print(dias, "Dias,", horas, "Horas,", minutos, "minutos,", segundos, "segundos.") 