
# 1) Criando lista com Array:
# - Crie um array com o valor de 10 produtos;
# - Crie um novo array contendo os produtos com 5% de desconto
# - Mostre ao usuário os valores dos produtos com e sem desconto


products = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

newProducts = []

for i in products:
    newI = i - (i * 0.05) 
    newProducts.append(newI)

print("\n")
print("Lista de produtos:", products)
print("\n")
print("Desconto:", newProducts)
print("\n")
