# verifica se valor da string pode ser numérico (verdadeiro ou falso)
def _valorNumerico(string: str):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid

# converte valor da string em inteiro se puder (retorna str)
def _valorInteiro(string: str):
    
    numero = float(string)

    if numero.is_integer():
        numero = int(numero)
    
    print(f'\ndef valor_inteiro(string: str) = {numero}\n')

    return str(numero)
