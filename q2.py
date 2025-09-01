
#Tem que rezar pra isso funcionar
numero = 1
media = 0
acimaouigualnamedia = 0
alunosrec = 0

alunos = int(input("Quanto alunos tem na turma?: "))
for n in range(alunos):
    notas = float(input(f"Qual foi a nota do aluno? N°{numero}: "))
    if notas >= 6:
        acimaouigualnamedia +=1
    else:
        alunosrec += 1

calculomdturma = media / alunos
print(f"A média geral da turma: {calculomdturma}")
print(f"Alunos de recuperação: {alunosrec}")
print(f"Alunos na maior ou igual a média: {acimaouigualnamedia}")



