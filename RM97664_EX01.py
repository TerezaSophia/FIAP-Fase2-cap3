assinatura = input("Qual a assinatura do cliente? Opções: B-Basic, S-Silver, G-Gold, P-Platinum. ")
faturamento_anual = float(input("Qual o faturamento anual do cliente? "))

calculo_bonus = 0.0

if assinatura.upper() == "B":
    calculo_bonus = faturamento_anual * 0.3
elif assinatura.upper() == "S":
    calculo_bonus = faturamento_anual * 0.2
elif assinatura.upper() == "G":
    calculo_bonus = faturamento_anual * 0.1
elif assinatura.upper() == "P":
    calculo_bonus = faturamento_anual * 0.05
else:
    print("Assinatura inválida, por favor digite novamente.")

print("O valor do bônus que o cliente deve pagar é R$ {:.2f} reais.".format(calculo_bonus))
