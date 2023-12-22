def l():
    print()


import re
import cor
from título import título


título('EXPRESSÕES REGULARES')
l()
texto = 'Este é um teste de uma expressão regular. (aplicando teste)'
print(f'{cor.vermelho_claro}texto:{cor.limpar} {texto}')
l()
print(f'{cor.verde_claro}IDENTIFICA POSIÇÃO DA PALAVRA DESEJADA INICIO E FIM (UMA VEZ)')
print(f"{cor.amarelo_claro}re.search(r'teste', {cor.vermelho_claro}texto{cor.amarelo_claro}){cor.limpar}")
print(re.search(r'teste', texto))
l()
print(f'{cor.verde_claro}IDENTIFICA QUANTAS VEZES APARECE A PALAVRA DESEJADA EM LISTA')
print(f"{cor.amarelo_claro}fre.findall(r'teste', {cor.vermelho_claro}texto{cor.amarelo_claro}){cor.limpar}")
print(re.findall(r'teste', texto))
l()
print(f'{cor.verde_claro}SUBSTITUI PALAVRA DESEJADA')
print(f"{cor.amarelo_claro}re.sub(r'teste', 'TESTE', {cor.vermelho_claro}texto{cor.amarelo_claro}){cor.limpar}")
print(re.sub(r'teste', '#TESTE#', texto))
l()
print(f'{cor.verde_claro}SUBSTITUI PALAVRA DESEJADA')
print(f"{cor.amarelo_claro}(re.sub(r'teste', '#ABCD#', {cor.vermelho_claro}texto{cor.amarelo_claro}, count=1)){cor.limpar}")
print(re.sub(r'teste', '#ABCD#', texto, count=1))
print(re.sub(r'teste', '#ABCD#', texto))
l()
print(f'{cor.verde_claro}SIMPLIFICA UMA EXPRESSÃO A UM OBJETO PARA SER MANIPULADA{cor.limpar}')
print(f'{cor.vermelho_claro}texto:{cor.limpar} {texto}')
print(f"{cor.amarelo_claro}converte = re.compile(r'teste'){cor.limpar}")
converte = re.compile(r'teste')
print(converte)
print(f'{cor.amarelo_claro}(converte.search({cor.vermelho_claro}texto{cor.amarelo_claro})){cor.limpar}')
print(converte.search(texto))
print(f'{cor.amarelo_claro}(converte.findall({cor.vermelho_claro}texto{cor.amarelo_claro})){cor.limpar}')
print(converte.findall(texto))
print(f"{cor.amarelo_claro}(converte.sub('#TESTE#', {cor.vermelho_claro}texto{cor.amarelo_claro})){cor.limpar}")
print(converte.sub('#TESTE#', texto))
print(f"{cor.amarelo_claro}(converte.sub('#ABCD#', {cor.vermelho_claro}texto{cor.amarelo_claro}, count=1)){cor.limpar}")
print(converte.sub('#ABCD#', texto, count=1))

l()
texto = '''João trouxe flores para sua amada namorada em 10 de janeiro de 1970, Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tarde de domingo.
Também né! Sendo a boa mineira que é, nunca esquecia seu famoso pão de queijo.
Não canso de ouvir a Maria: "Joooooooooooãooooo, o café tá prontinho aqui. Veeemmm!!! Veemm!! Vem!"
MARIA AMA JOÃO!!!
'''
print(f'{cor.vermelho_claro}texto:{cor.limpar} {texto}')
l()
print('\033[93mMeta caracteres: \|.[]+*?{}()^$\\033[m')
print(f'{cor.amarelo_claro}\\ = escapa caracteres especiais para string {cor.limpar}')
print(f'{cor.amarelo_claro}| = ou {cor.limpar}')
print(f'{cor.amarelo_claro}. = substitui qualquer caractere{cor.limpar}')
print(f'{cor.amarelo_claro}[] = captura um conjunto de caracteres em qualquer ordem digitado{cor.limpar}')
print(f"{cor.amarelo_claro}+ = o caractere escolhido pode se repetir 1 ou 'n' na palavra {cor.limpar}")
print(f"{cor.amarelo_claro}* = o caractere escolhido pode se repetir 0 ou 'n' na palavra {cor.limpar}")
print(f"{cor.amarelo_claro}? = o caractere escolhido pode se repetir 0 ou 1 na palavra {cor.limpar}")
print("\033[93m{} = o caractere escolhido pode se repetir mínimo ou máximo\033[m")
print("\033[93m{5} = o caractere escolhido deve se repetir 5 vezes\033[m")
print("\033[93m{5,} = o caractere escolhido deve se repetir no mínimo 5 vezes\033[m")
print("\033[93m{,5} = o caractere escolhido pode se repetir no máximo 5 vezes\033[m")
print("\033[93m{5,10} = o caractere escolhido pode se repetir entre 5 ou 10 vezes\033[m")
print(f'{cor.amarelo_claro}() = captura palavra desejada ou sequencia de caracteres especifico{cor.limpar}')
print(f'{cor.amarelo_claro}^ = Corresponde ao início de uma string{cor.limpar}')
print(f'{cor.amarelo_claro}$ = Corresponde ao termino de uma string{cor.limpar}')
print(f'{cor.amarelo_claro}\w = [a-zA-ZÀ-ú_]{cor.limpar}')
print(f'{cor.amarelo_claro}\W = not [a-zA-ZÀ-ú_]{cor.limpar}')
print(f'{cor.amarelo_claro}\d = [0-9]{cor.limpar}')
print(f'{cor.amarelo_claro}\D = not [0-9]{cor.limpar}')
print(f'{cor.amarelo_claro}\s = [ \\n\\r\\f\\t]{cor.limpar}')
print(f'{cor.amarelo_claro}\S = not [ \\n\\r\\f\\t]{cor.limpar}')
print(f'{cor.amarelo_claro}\\b = define inicio ou fim de um conjunto de caractere desejado {cor.limpar}')
print(f'{cor.amarelo_claro}\B = "not" define inicio ou fim de um conjunto de caractere desejado{cor.limpar}')
print(f'{cor.amarelo_claro}(?:...) = {cor.limpar}')
print(f'{cor.amarelo_claro}(?:...) = não captura de parênteses regulares em um grupo{cor.limpar}')

'''
flags=re.A ou re.ASCII (correspondência somente código ASCII);
flags=re.I ou re.IGNORECASE (ignorar maiúsculas e minúsculas);
flags=re.L ou re.LOCALE (dependente da localidade);
flags=re.M ou re.MULTILINE(várias linhas);
flags=re.S ou re.DOTALL(ponto corresponde a todos);
flags=re.U ou re.VERBOSE(correspondência Unicode);
flags=re.X ou re.VERBOSE  (permite que você separe visualmente seções lógicas e adicione comentários)
'''



print(re.findall(r'[À-ú]', texto))
print(re.findall(r'João|maria|adulto.|fi..........|aq.', texto))
print(re.findall(r'[Jj]oão|[a-zA-Z]aria', texto))
print(re.findall(r'JoÃo|mArIa', texto, flags=re.IGNORECASE))
print(re.findall(r'JoÃo|mArIa', texto, flags=re.I))
print(re.findall(r'[Jj]o+ão', texto))
print(re.findall(r'Jo+ão+', texto))
print(re.findall(r'[Joã]+', texto, flags=re.I))
print(re.findall(r'jo+', texto, flags=re.I))
print(re.findall(r'jo*', texto, flags=re.I))
print(re.findall(r'jo?', texto, flags=re.I))
print(re.findall(r'j*oão', texto))
print(re.findall(r'j*oão+', texto))
print(re.findall(r'Ve{1,3}m*', texto, flags=re.I))
print(re.findall(r'Ve{1,3}m+', texto, flags=re.I))
print(re.findall(r'..Ve.+m*', texto, flags=re.I))
print(re.findall(r'[a-z].Ve.+m*', texto, flags=re.I))
print(re.findall(r'jo{15,}ão{1}', texto, flags=re.I))
print(re.findall(r'jo{,15}ão{2,}', texto, flags=re.I))
print(re.findall(r'jo{10,15}ão{6,10}', texto, flags=re.I))
print(re.findall(r'jo{10,15}ão{3,6}', texto, flags=re.I))
print(re.findall(r'ama[a-z]*', texto, flags=re.I))
print(re.findall(r'queijo.', texto, flags=re.I))
print(re.findall(r'queijo\.', texto, flags=re.I))

texto = 'Décio décio Decio decio DéCiO dÉcIo DeCiO dEcIo'
print(re.findall(r'(decio)', texto))
print(re.findall(r'(decio)', texto, flags=re.I))
print(re.findall(r'(Décio)', texto))
print(re.findall(r'(Décio)', texto, flags=re.I))
print(re.findall(r'(décio|decio)', texto, flags=re.I))
print(re.findall(r'(Décio|Decio)', texto))
print(re.findall(r'(D.cio)', texto))

l()
cpf = '''
104.509.587-81
a098.877.632-72a
642.567.232-09
042767232-08
642.567.23209
72356478173
'''
print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', cpf))
print(re.findall(r'([0-9]{3}\.){2}[0-9]{3}-[0-9]{2}', cpf))
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf)) # "?:" NÃO IMPRIME GRUPO SELECIONADO
print(re.findall(r'[0-9]{3}[0-9]{3}[0-9]{3}[0-9]{2}', cpf))
print(re.findall(r'[0-9\.]+...', cpf))
print(re.findall(r'[0-9\.]+-..', cpf))
print(re.findall(r'[0-9\.]+-.[19]', cpf))
print(re.findall(r'[^a-z]+', cpf))
print(re.findall(r'[^0-9]+', cpf))
print(re.findall(r'[0-9].+-+[0-9]+', cpf))
print(re.findall(r'\d+.+-+\d+', cpf))
print(re.findall(r'\d+.*-?\d+', cpf))


l()
nome = '''Décio
Santana
de
Aguiar'''
print(re.findall(r'^Décio$', nome))
print(re.findall(r'^Décio', nome))
print(re.findall(r'^Santana', nome))
print(re.findall(r'^de$', nome))
print(re.findall(r'Aguiar$', nome))
print(re.findall(r'^Aguiar', nome))
print(re.findall(r'^Décio Santana de Aguiar$', nome))

l()
nome = '''Décio
Santana
de
Aguiar'''
print(re.findall(r'^Décio$', nome, flags=re.M))
print(re.findall(r'^Décio', nome, flags=re.M))
print(re.findall(r'^Santana', nome, flags=re.M))
print(re.findall(r'^de$', nome, flags=re.M))
print(re.findall(r'Aguiar$', nome, flags=re.M))
print(re.findall(r'^Aguiar', nome, flags=re.M))
print(re.findall(r'^.*.$', nome, flags=re.S))


l()
nome = 'Décio Santana de Aguiar'
print(re.findall(r'^Décio', nome))
print(re.findall(r'^Santana', nome))
print(re.findall(r'^de$', nome))
print(re.findall(r'Aguiar$', nome))
print(re.findall(r'^Aguiar', nome))
print(re.findall(r'^Décio Santana de Aguiar$', nome))
print(re.findall(r'^Décio', nome, flags=re.M))
print(re.findall(r'^Santana', nome, flags=re.M))
print(re.findall(r'^de$', nome, flags=re.M))
print(re.findall(r'Aguiar$', nome, flags=re.M))
print(re.findall(r'^Aguiar', nome, flags=re.M))
print(re.findall(r'^Décio Santana de Aguiar$', nome, flags=re.M | re.I))
print(re.findall(r'\w', nome))
print(re.findall(r'\w?', nome))
print(re.findall(r'\w+', nome))
print(re.findall(r'\w+', nome, flags=re.A))
print(re.findall(r'\w*', nome))
print(re.findall(r'\W+', nome))

l()
nome = '''Décio Santana de Aguiar
dÉCIO sANTANA DE aGUIAR
DéCiO SaNtAnA De AgUiAr
DÉCIO SANTANA DE AGUIAR
décio santana de aguiar
[_] [,;:]  [.!?] [^~`´] [¨""]
    {@#$%&*+-}  (01234567890)
'''
print(re.findall(r'\s+', nome))
print(re.findall(r'\S+', nome))
print(re.findall(r'\S+', nome))
print(re.findall(r'\bsan\w+', nome, flags=re.I))
print(re.findall(r'\w+ar\b', nome, flags=re.I))
print(re.findall(r'\b\w{2}\b', nome, flags=re.I))

texto = 'O João gosta de folia Ele adora ser amado'
print(re.findall(r'^o.*o$', texto, flags=re.I))
texto = '''
O João gosta de folia
Ele adora ser amado
'''
print(re.findall(r'^.*o$', texto, flags=re.I))
print(re.findall(r'^.*o$', texto, flags=re.S))
print(re.findall(r'^O.*a$', texto, flags=re.M))
print(re.findall(r'^E.*o$', texto, flags=re.M))
print(re.findall(r'^.*.$', texto, flags=re.M))

texto = '''CADASTRO:
CPF: 104.567.879-90 ATIVO 
CPF: 098.755.632-72 INATIVO
CPF: 167.432.588-84 ATIVO
CPF: 166.432.672-84 INATIVO
CPF: 166.567.875-72 ATIVO
CPF: 166.567.875-72 ATIVO
CPF: a16656787572a ATIVO
'''
print(re.findall(r'.+', texto))
print(re.findall(r'.+', texto, flags=re.S))
print(re.findall(r'\S+', texto))
print(re.findall(r'\w+\S\s\d+.+-?\d+\s\w*', texto))
print(re.findall(r'\w*\S\s(\d+.+-?\d+)\s\w*', texto))
print(re.findall(r'(\w*)\S\s(\d+.+-?\d+)\s(\w*)', texto))
print(re.findall(r'(?:\w*)\S\s(\d+.+-?\d+)\s(?:\w*)', texto))
print(re.findall(r'\w*\S\s(\d+.+-?\d+)\s(?=ativo)', texto, flags=re.I))
print(re.findall(r'\w*\S\s(\d+.+-?\d+)\s(?=inativo)', texto, flags=re.I))
print(re.findall(r'\w*\S\s(\d+.+-?\d+)\s(?!inativo)', texto, flags=re.I))
print(re.findall(r'(\d+.*-?\d+)\s(?=ativo)', texto, flags=re.I))

texto = '''CADASTRO:
ATIVO CPF: 104.567.879-90
INATIVO CPF: 098.755.632-72
ATIVO CPF: 104.432.588-84
INATIVO CPF: 098.432.672-84
INATIVO CPF: 098.567.875-72
ATIVO CPF: 104.567.875-72
'''
print(re.findall(r'(?![inativo]).+', texto, flags=re.I))
print(re.findall(r'(?=[in]*ativo).+', texto, flags=re.I))
print(re.findall(r'(?=inativo).+', texto, flags=re.I))
print(re.findall(r'(?=^ativo).+', texto, flags=re.I | re.M))
print(re.findall(r'(?<=inativo).+', texto, flags=re.I))
print(re.findall(r'(?<=^ativo).+', texto, flags=re.I | re.M))
print(re.findall(r'[\d.-]+', texto, flags=re.I | re.M))
print(re.findall(r'[^\s\d.-]+', texto, flags=re.I | re.M))
l()

texto = '''
CPF: 104.587.509-87
IP: 1.202.12.192
E-MAIL: decio@gmail.com
E-MAIL: santana@gmail.com.br
'''
print(re.findall(r'(?=CPF).+', texto, flags=re.I))
print(re.findall(r'(?=ip).+', texto, flags=re.I))
print(re.findall(r'(?=e-mail).+', texto, flags=re.I))
print(re.findall(r'(?<=e-mail:\s).+', texto, flags=re.I))
print(re.findall(r'\w+@\w+[.com]+[.br]+', texto, flags=re.I))
print(re.findall(r'(\w+@\w+.\w+)\s', texto, flags=re.I))


teste = 'CF.5699'
print(re.findall(r""" 
\w+ # comentario 
\. # comentario 
\d+ # comentario
""", teste, re.X))
print(re.findall(r'\w+\.\d+', teste))

CPF = '''
104.432.588-84
000.000.000-01
000.000.000-00
111.111.111-11
'''
print(re.findall(r'\d+.+-+\d+', CPF))
print(re.findall(r'(?!(\d)\1{2}.\1{3}.\1{3}-\1{2})(\d{3}.\d{3}.\d{3}-+\d{2})', CPF))
print(re.findall(r'(?=(\d)\1{2}.\1{3}.\1{3}-\1{2})(\d{3}.\d{3}.\d{3}-+\d{2})', CPF))

