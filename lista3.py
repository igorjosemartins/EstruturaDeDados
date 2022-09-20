
# 3) Crie uma lista de produtos com os seguintes requisitos:
    
#     – Inicializará com 10 produtos, preços e quantidades;
#     – Faça um Foreach para calcular o valor total de cada produto;
#     – Ao final, mostre todos os produtos, preços, quantidade, total por produto e o total geral.


produtos = [
    # "produtos", preços, quantidades, total
    ["Samsung 520", 5000, 2, 0],
    ["Samsung S10", 2500, 5, 0],
    ["Iphone 13", 6000, 3, 0],
    ["Iphone 10", 3000, 2, 0]
]

totalizador = 0

for p in produtos:
    # total = preço * quantidade 
    p[3] = p[1] * p[2]
    totalizador += p[3]
    print(p)

print("Valor total da compra: ", totalizador)