"""
    Dicas:
    Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
"""

from abc import ABC, abstractmethod
from opcao import cheque_especial

class Conta (ABC):
    # construtor
    def __init__(self, agencia: int, numero_conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo
        

    @abstractmethod
    def sacar(self): # método abstrato
        ...

    def depositar(self, valor):
        print('DEPOSITO')
        self.saldo += valor
        return self.ver_saldo()
    
    def ver_saldo(self) -> None:
        print(f'Seu saldo R$: {self.saldo:.2f}')
        print()
        return

class ContaCorrente(Conta):
    def __init__(self, agencia: int, numero_conta: int, saldo: float=0, limite_atual_cheque_especial = 0) -> None:
        super().__init__(agencia, numero_conta, saldo)
        self.total_limite_cheque_especial = limite_atual_cheque_especial
        self.limite_atual_cheque_especial = limite_atual_cheque_especial

    def limite_cliente(self, limite=0) -> None:
        self.total_limite_cheque_especial = limite

        if self.saldo >= 0: # se saldo valor positivo
            self.limite_atual_cheque_especial = limite
        else: # se saldo valor negativo
            self.limite_atual_cheque_especial = limite + self.saldo
        print(f'Seu limite foi alterado para {limite:.2f}')
        print()

    def sacar(self, valor: float): # implementar método abstrato
        print('SAQUE')
        valor_do_saque = self.saldo - valor
        
        if valor_do_saque > 0:
            self.saldo -= valor
            print('Saque realizado com sucesso!')
                        
        elif valor_do_saque >= self.total_limite_cheque_especial * (-1):
            print('Saldo em conta insuficiente!')
            if self.total_limite_cheque_especial == self.limite_atual_cheque_especial:
                print(f'Valor do cheque especial disponível R$:{self.limite_atual_cheque_especial:.2f}')
            else:
                print(f'Valor do cheque especial disponível R$:{self.limite_atual_cheque_especial:.2f}')
                
            
            op = cheque_especial(f'Deseja utilizar seu cheque especial? [S/N]')

            if op:
                self.limite_atual_cheque_especial -= valor
                self.saldo -= valor
                print('Saque realizado com sucesso!')
        else:
            print('Valor do saque ultrapassa o limite de sua conta.')
        return self.ver_saldo()
    
    def __repr__(self): # retorna uma representação de string de um objeto
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.numero_conta!r}, {self.saldo!r}, {self.limite_atual_cheque_especial})'
        return f'{class_name} = {attrs}'

class ContaPoupanca(Conta):
    def sacar(self, valor: float): # implementar método abstrato
        print('SAQUE')
        valor_do_saque = self.saldo - valor
        if valor_do_saque >= 0:
            self.saldo -= valor
            print('Saque realizado com sucesso!')
        else:
            print('Valor do saque ultrapassa o limite de sua conta.')
        return self.ver_saldo()
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.numero_conta!r}, {self.saldo!r})'
        return f'{class_name} = {attrs}'
    
if __name__ == '__main__':
    # cp1 = ContaPoupanca(111, 111, 400)
    # cp1.sacar(100)
    # cp1.sacar(500)
    # cp1.depositar(300)
    cc1 = ContaCorrente(111,222, 5, 2)
    cc1.ver_saldo()
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    print(cc1)
    cc1.ver_saldo()
    cc1.limite_cliente(5)
    print(cc1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(50)
    print(cc1)
    cc1.sacar(1)
    print(cc1)
    cc1.sacar(1)
    print(cc1)

    