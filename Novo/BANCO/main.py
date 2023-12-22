"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa
    Cliente
        Clente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

from abc import ABC, abstractmethod
import contas

class Pessoa(ABC):

    @abstractmethod
    def _cadrastro(self):
        ...

    def __init__(self):
        self._nome = None
        self._idade = None
        self._cadastro = []
    
    @property
    def cadastrar_nome_idade(self):
        self.cadastro = (self._nome, self._idade)       
        return self.cadastro
    
    @cadastrar_nome_idade.setter
    def cadastrar_nome_idade(self, nome, idade):
        self._nome = nome
        self._idade = idade
        
        
    # @cadastrar_idade.deleter
    # def cadastrar_nome_idade(self, nome, idade):
    #     ...

class Cliente(Pessoa):

    def _cadrastro(self):
        ...

p = Cliente()
p.cadastrar_nome_idade = (nome='a', idade=1)

