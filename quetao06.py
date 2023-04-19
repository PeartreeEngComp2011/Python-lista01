import math

metros_quadrados = float(input("Informe o tamanho em metros quadrados da área a ser pintada: "))

litros_necessarios = metros_quadrados / 6
litros_necessarios_com_folga = litros_necessarios * 1.1

# Quantidade e preço de latas de tinta
latas_necessarias = math.ceil(litros_necessarios_com_folga / 18)
preco_latas = latas_necessarias * 80

# Quantidade e preço de galões de tinta
galoes_necessarios = math.ceil(litros_necessarios_com_folga / 3.6)
preco_galoes = galoes_necessarios * 25

# Quantidade e preço de latas e galões de tinta
latas_misturadas = math.floor(litros_necessarios_com_folga / 18)
litros_sobrando = litros_necessarios_com_folga - latas_misturadas * 18
galoes_necessarios = math.ceil(litros_sobrando / 3.6)
preco_misto = latas_misturadas * 80 + galoes_necessarios * 25

print(f"\nSerão necessárias {latas_necessarias} latas de tinta")
print(f"Preço total só com latas: R$ {preco_latas:.2f}")

print(f"\nSerão necessários {galoes_necessarios} galões de tinta")
print(f"Preço total só com galões: R$ {preco_galoes:.2f}")

print(f"\nSerão necessárias {latas_misturadas} latas e {galoes_necessarios} galões de tinta")
print(f"Preço total com latas e galões misturados: R$ {preco_misto:.2f}")