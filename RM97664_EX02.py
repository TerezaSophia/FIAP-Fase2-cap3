print("Este programa irá informar qual o dia da semana escolhido pelos alunos para que "
      "as lives das aulas sejam feitas.")

t_alunos = int(input("Qual o número total de alunos? "))
while t_alunos < 0:
    t_alunos = int(input("Número inválido, digite novamente: "))
# Caso o usuário digite um número inválido.

SEG = 0
TER = 0
QUAR = 0
QUIN = 0
SEXTA = 0
# Obrigatório declarar fora da estrutura de repetição a quantidade de cada variável,
# para não dar erro ao ser atribuído valor.

for x in range(1, t_alunos + 1, 1):
    print("Das opções a seguir: SEG-segunda-feira, TER-terça-feira, QUAR-quarta-feira, "
          "QUIN-quinta-feira e SEXTA-sexta-feira")
    voto = input("Qual dia da semana o aluno nº{} escolheu?".format(x))

    if voto.upper() == "SEG":
        SEG = SEG + 1
    elif voto.upper() == "TER":
        TER = TER + 1
    elif voto.upper() == "QUAR":
        QUAR = QUAR + 1
    elif voto.upper() == "QUIN":
        QUIN = QUIN + 1
    elif voto.upper() == "SEXTA":
        SEXTA = SEXTA + 1
    else:
        print("Dia da semana inválido!")
# Sempre há a possibilidade de ser digitado algo errado.

# Realizar comparação entre os dias da semana.
if SEG > TER and SEG > QUAR and SEG > QUIN and SEG > SEXTA:
    print("O dia da semana escolhido foi a Segunda-feira")
elif TER > SEG and TER > QUAR and TER > QUIN and TER > SEXTA:
    print("O dia da semana escolhido foi a Terça-feira")
elif QUAR > SEG and QUAR > TER and QUAR > QUIN and QUAR > SEXTA:
    print("O dia da semana escolhido foi a Quarta-feira")
elif QUIN > SEG and QUIN > TER and QUIN > QUAR and QUIN > SEXTA:
    print("O dia da semana escolhido foi a Quinta-feira")
elif SEXTA > SEG and SEXTA > TER and SEXTA > QUAR and SEXTA > QUIN:
    print("O dia da semana escolhido foi a Sexta-feira")
else:
    print("Houve um erro, tente novamente! Caso ele persista, por favor entrar em contato com a direção.")
