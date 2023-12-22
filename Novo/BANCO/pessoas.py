import contas

class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

# --- desnecessário apenas para alteração ---
    @property
    def nome(self): 
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        self._idade = idade
# -------------------------------------------

    def __repr__(self): # retorna uma representação de string de um objeto
        class_name = type(self).__name__
        attrs = f'({self._nome!r}, {self.idade!r})'
        return f'{class_name} = {attrs}'


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade)
        self.conta: contas.Conta


if __name__ == '__main__':
    c1 = Cliente('Luiz', 30)
    c1.conta = contas.ContaCorrente(111, 222, 0, 500)
    print(c1)
    c1.nome = 'Ana'
    print(c1.nome)
    print(c1)
    c1.idade = 5
    print(c1)
    print(c1.conta) # vem de repr em "contas.ContaCorrente"
    print(repr(c1))
    print('<==========================================================>')
    c2 = Cliente('Maria', 18)
    c2.conta = contas.ContaPoupanca(112, 223, 100)
    print(c2)
    print(c2.conta)
    print(repr(c2))