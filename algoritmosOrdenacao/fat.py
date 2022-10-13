
# cálculo do fatorial
# 5! = 1 x 2 x 3 x 4 x 5 = 120

# função cálculo fatorial (NÃO SE DEVE FAZER)
# recebe um número
def fatWrong (numero):

    # total = 1 (ja começa no 1, pra não multiplicar por 0)
    total = 1

    # percorre do 1 até o numero digitado 
    for i in range(numero):
        # multiplica o total pelos índices (+1 por que o primeiro índex é 0)
        total *= (i + 1)

    # retorna o total
    return total

print(fatWrong(5))


# algoritmo de ordenação
# cálculo fatorial (DEVE FAZER)

def fat (numero):
    # se o numero for 1
    if numero == 1:
        # retorne o numero (limite para n passar de 1)
        return numero
    else:
        # retorne o numero * a função do numero - 1 (recursão)
        # =
        # guarda em memória, por que ainda não temos o fat(4), fat(3), fat(2)...
        # 5 * fat(5 - 1)
        # 4 * fat(4 - 1)
        # 3 * fat(3 - 1)
        # 2 * fat(2 - 1)
        return numero * fat(numero - 1)