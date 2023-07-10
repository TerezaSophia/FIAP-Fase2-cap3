print("Este programa irá calcular a média dos alunos pares e ímpares, "
      "indicar qual do grupo de alunos obteve a maior média,"
      "e por fim informara média geral da turma.")
media_par = 0.0
media_impar = 0.0
nota_par_t = 0.0
nota_impar_t = 0.0

print("Você está digitando a nota dos alunos pares. Digite as notas decimais utilizando ponto (.) e não vírgula (,).")
for x in range(2, 51, 2):
    nota_par = float(input("Qual a nota do aluno nº {}?".format(x)))
    if nota_par < 0 or nota_par > 10:
        print("Nota inválida! Digite um valor entre 0 e 10.")
        nota_par = float(input("Qual a nota do aluno nº {}? ".format(x)))
    nota_par_t = nota_par_t + nota_par

print("Você está digitando a nota dos alunos ímpares. Digite as notas decimais utilizando ponto (.) e não vírgula (,).")
for y in range(1, 51, 2):
    nota_impar = float(input("Qual a nota do aluno nº {}?".format(y)))
    if nota_impar < 0 or nota_impar > 10:
        print("Nota inválida! Digite um valor entre 0 e 10.")
        nota_impar = float(input("Qual a nota do aluno nº {}? ".format(y)))
    nota_impar_t = nota_impar_t + nota_impar

media_par = nota_par_t / 25
media_impar = nota_impar_t / 25

if media_par > media_impar:
    print("A média dos alunos pares foi {}, e a média dos alunos ímpares foi {}. "
          "Portanto, os alunos pares obtiveram a maior média.".format(media_par, media_impar))
elif media_impar > media_par:
    print("A média dos alunos pares foi {}, e a média dos alunos ímpares foi {}. "
          "Portanto os alunos ímpares obtiveram a maior média.".format(media_par, media_impar))
else:
    print("A média dos alunos pares foi {}, "
          "e a média dos alunos ímpares foi {}, sendo iguais.".format(media_par, media_impar))
