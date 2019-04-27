import math



metros2 = int (input ("Quantos m² você irá pintar? "))



litros = (metros2 / 6)



print ("a)")

latas_necessarias = math.ceil (litros / 18)



print ("Você vai precisar de: ", latas_necessarias, "latas de 18l")



print ("b)")



galoes = math.ceil (litros / 3.6)



print ("Você vai precisar de: ", galoes, "galoes de 3,6l")



print ("c)")



latas = int (litros / 18)

resto = latas_necessarias % 18

galoes = math.ceil (resto / 3.6)



print ("Você usará ", latas_necessarias, "latas de 18l")

print ("e", galoes, "de 3,6l")



preco = (latas_necessarias * 80) + (galoes * 25)



print ("Utilizando Latas e Galões o total a pagar é de", preco, "reais", "você ganhou 10% de desconto. O preço final é:", preco - (preco * 10 / 100), "reais")