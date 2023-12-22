"""
    Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
    Banco será responsável autenticar o cliente e as contas da seguinte maneira:
        Banco tem contas e clientes (Agregação)
        * Checar se a agência é daquele banco
        * Checar se o cliente é daquele banco
        * Checar se a conta é daquele banco
    Só será possível sacar se passar na autenticação do banco (descrita acima)
    Banco autentica por um método.
"""

import contas
import pessoas

class Banco:
    # construtor
    def __init__(
        self,
        agencias: list[int] = None,
        clientes: list[pessoas.Pessoa] = None,
        contas: list[contas.Conta] = None,
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    # checar agencia
    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('_checa_agencia', True)
            return True
        print('_checa_agencia', False)
        return False

    # checar cliente
    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('_checa_cliente', True)
            return True
        print('_checa_cliente', False)
        return False

    # checar conta
    def _checa_conta(self, conta):
        if conta in self.contas:
            print('_checa_conta', True)
            return True
        print('_checa_conta', False)
        return False

    # checar conta do cliente
    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print('_checa_se_conta_e_do_cliente', True)
            return True
        print('_checa_se_conta_e_do_cliente', False)
        return False

    # autebticar todas as checagens
    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)

    # retorna uma representação de string de um objeto
    def __repr__(self): 
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    cliente1 = pessoas.Cliente('Luiz', 30)
    cliente2 = pessoas.Cliente('Maria', 18)
    conta_corrente1 = contas.ContaCorrente(111, 222, 100, 2)
    cliente1.conta = conta_corrente1
    print(cliente1.conta)
    conta_poupanca1 = contas.ContaPoupanca(112, 223, 100)
    print(conta_poupanca1)
    print('<==========================================================>')
    banco = Banco()
    print(banco)
    print(cliente1)
    print('<==========================================================>')
    banco.clientes.extend([cliente1, cliente2])
    print(banco)
    banco.contas.extend([conta_corrente1, conta_poupanca1])
    print(banco)
    banco.agencias.extend([111, 222])
    print(banco)
    print('<==========================================================>')
    if banco.autenticar(cliente1, conta_corrente1):
        conta_corrente1.sacar(101)
        conta_corrente1.sacar(101)
        print(cliente1.conta)