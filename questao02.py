nt1 = float(input("Digite a primeira nota: "))
nt2 = float(input("Digite a segunda nota: "))
nt3 = float(input("Digite a terceira nota: "))

med = (nt1 + nt2 + nt3) / 3

if med >= 7.0:
    print("Aluno aprovado!")
elif med >= 5.0:
    print("Aluno em recuperação.")
else:
    print("Aluno reprovado.")
