dias = input ("Digite os dias:  ")

horas = input ("Digite as horas:  ")

minutos = input ("Digite os minutos:  ")

segundos = input ("Digite os segundos:  ")



segundos = 1

minutos = int (minutos)

horas = int (horas)

dias = int (dias)



print ("Este período de tempo em segundos é", (dias * 86400 + horas * 3600 + minutos * 60 + segundos * 1), "s")