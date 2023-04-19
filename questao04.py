valor_hora = float(input("Informe o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Informe o número de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - ir - inss - sindicato

print(f"\nSalário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto de IR (11%): R$ {ir:.2f}")
print(f"Desconto de INSS (8%): R$ {inss:.2f}")
print(f"Desconto de Sindicato (5%): R$ {sindicato:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")