import math

metros_quadrados = float(input("Informe o tamanho em metros quadrados da área a ser pintada: "))

litros_necessarios = metros_quadrados / 3
latas_necessarias = math.ceil(litros_necessarios / 18)
preco_total = latas_necessarias * 80

print(f"\nSerão necessárias {latas_necessarias} latas de tinta")
print(f"Preço total: R$ {preco_total:.2f}")