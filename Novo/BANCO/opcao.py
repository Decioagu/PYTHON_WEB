def cheque_especial(msg):
    """
    Testa caractere e permanece em loop infinito até usuário
    digitar os valores "S" ou "N" para variável "op"
    
    :msg : texto descrito pelo usuário 
    :op: Variável recebe somente os valores "S" ou "N"
    :return: Retorna variável "op" com o valor "S" ou "N"
    """
    while True:
        op = input(msg).strip().upper()
        if op in 'S':
            op = True
            break
        elif op in 'N':
            op = False
            break
        else:
            print()
            print(f'Opção invalida!')
            print(f'Digite [s] para CONTINUAR ou [n] para SAIR.')
    return op
