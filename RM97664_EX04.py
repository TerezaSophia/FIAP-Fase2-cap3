minuto = int(input("Para desbloquear a máquina, digite o minuto que está marcado no relógio com um número inteiro"))

fatorial = 1

if minuto < 0:
    print("Não é possível calcular o fatorial de um número negativo.")

elif minuto == 0:
    fatorial = 1

elif minuto == 1:
    fatorial = 1
else:
    for x in range(minuto, 1, -1):
        fatorial = fatorial * x

print("A senha é LIBERDADE{}".format(fatorial))
