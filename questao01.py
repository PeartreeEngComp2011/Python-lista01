sb = float(input("Digite o valor do salário bruto: "))
desconto = float(input("Digite o valor dos descontos: "))
saliq = sb - desconto

limemp = saliq * 0.3

vlemp = float(input("Digite o valor do possível empréstimo: "))

if vlemp <= limemp:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado.")
