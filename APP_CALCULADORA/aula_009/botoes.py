from PySide6.QtWidgets import QPushButton, QGridLayout
from variaveis import (FONTE_MEDIO_SIZE, PRIMEIRA_COR, SEGUNDA_COR, TERCEIRA_COR, QUARTA_COR, 
                       QUINTA_COR, SEXTA_COR, SETIMA_COR)

from display import Display, Info
from PySide6.QtCore import Slot
from uteis import valor_numerico

class Botoes(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args = args
        self.configStyle() # método de estilo

    # ======================== Método ============================
    def configStyle(self):
        '''
        Em Python, o método .font() é usado para definir a fonte de um widget Tkinter. 
        O método aceita um único argumento, que é uma tupla que especifica as 
        propriedades da fonte.

        Python
        label = Label(root, text="Hello, world!")
        label.font = ("Arial", 12, "bold italic") # (fonte, tamanho, estilo)
        # '''
        self.setMinimumSize(75, 75) # (largura, altura)
        
        caracter = str(*self.args) # ('texto)   

        # Estilos
        if caracter == '=':
            self.setStyleSheet(f"""
                                QPushButton {{
                                    background-color: {SEGUNDA_COR};
                                    color: white;  
                                }}
                                :hover {{
                                    background-color: {QUINTA_COR};
                                    color: white;
                                }}
                                :pressed {{
                                    background-color: {TERCEIRA_COR};
                                    color: white;
                                }}; 
                                font-size: {FONTE_MEDIO_SIZE}px
                            """)
        elif caracter.isdigit():
            self.setStyleSheet(f"""
                                QPushButton {{
                                    background-color: {PRIMEIRA_COR};
                                    color: white;  
                                }}
                                :hover {{
                                    background-color: {SEGUNDA_COR};
                                    color: white;
                                }}
                                :pressed {{
                                    background-color: {TERCEIRA_COR};
                                    color: white;
                                }}; 
                                font-size: {FONTE_MEDIO_SIZE}px
                            """)
        else:
            self.setStyleSheet(f"""
                                QPushButton {{
                                    background-color: {QUARTA_COR};
                                    color: white;  
                                }}
                                :hover {{
                                    background-color: {QUINTA_COR};
                                    color: white;
                                }}
                                :pressed {{
                                    background-color: {SEXTA_COR};
                                    color: white;
                                }}; 
                                font-size: {FONTE_MEDIO_SIZE}px
                            """)

            '''
            # estilo do texto (cor de fundo, cor do texto ,tamanho)
            # https://doc.qt.io/qtforpython-6/overviews/stylesheet-examples.html

            Para aplicar regras de estilo .setStyleSheet() em diferentes estados:
            # A regra de estilo QPushButton define o estilo do widget padrão. 
            # A regra de estilo :hover define o estilo do widget quando o mouse está sobre ele.
            # A regra de estilo :pressed define o estilo do widget quando ele é pressionado pelo usuário.
            '''

# 1º botoeGrid = BotoesGrid(display, info)
class BotoesGrid(QGridLayout):
    def __init__(self, display: Display, info: Info, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.display = display # (módulo "display")
        self.info = info  # (módulo "display")
        self._equation = '' # variável para manipulação de self.info em função "equation"

        # teclado
        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            [ '', '0', '.', '='],
        ]
        self._equationInitialValue = 'Sua conta'
        self._num_esquerda = None # numero esquerda do operador
        self._num_direita = None # numero direita do operador
        self._operador = None
        self.equation = self._equationInitialValue
        self._makeGrid() # método  construção do teclado


    # ======================== Método ============================
    # exibir Info acima display
    @property
    def equation(self):
        return self._equation
    # receber Info acima display
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    # Botões do teclado
    def _makeGrid(self):
        for linha_number, linha_info in enumerate(self._gridMask):
            for coluna_numero, botao_texto in enumerate(linha_info):
                botao = Botoes(botao_texto) # estilo do texto no botão

                # widgets interfaces gráficas do usuário (teclado)
                self.addWidget(botao, linha_number, coluna_numero)

                # acionamento das funções (display)
                botaoSlot = self._makeSlot(self._insertButtonTextToDisplay, botao)

                # Identifica clique no teclado (Click)
                self._connectButtonClicked(botao, botaoSlot)
                
    # identifica ação de (Click) no botão
    def _connectButtonClicked(self, botao, botaoSlot):
        botao.clicked.connect(botaoSlot) # (Click)
    
    # atrasa execução da função (_insertButtonTextToDisplay)
    def _makeSlot(self, func, *args, **kwargs):
        @Slot()
        def realSlot():
            func(*args, **kwargs)
        return realSlot

    # método de inserção de texto no display
    def _insertButtonTextToDisplay(self, botao):
        botao_texto = botao.text() # método que retorna uma str em um widget.

        # se botão clicado for 'C'
        if botao_texto == 'C':
            print('método _insertButtonTextToDisplay => limpar')
            self._clear()

        # se botões clicado forem '+-/*'
        if botao_texto in '+-/*':
            print('método _insertButtonTextToDisplay => +=/*')
            self._connectButtonClicked(botao, self._makeSlot(self._operatorClicked, botao))
        
        # concatena str no display na variável "newDisplayValue"
        newDisplayValue = self.display.text() + botao_texto 

        # função "valor_numerico" é do (módulo "uteis")
        if valor_numerico(newDisplayValue): # se for número 
            print('método _insertButtonTextToDisplay =>', newDisplayValue)
            self.display.insert(botao_texto) # inserir um elemento em uma lista (ver no display)

    # método para limpar informações do (display e info)
    def _clear(self):
            print('Vou fazer outra coisa aqui')
            self._num_esquerda = None # numero esquerda do operador
            self._num_direita = None # numero direita do operador
            self._operador = None
            self.equation = self._equationInitialValue
            self.display.clear()

    def _operatorClicked(self, botao):
        botao_texto = botao.text()  # +-/* (etc...)
        print( botao_texto)
        display_texto = self.display.text()  # Deverá ser meu número "_num_esquerda"
        self.display.clear()  # Limpa o display

        # Se a pessoa clicou no operador sem
        # configurar qualquer número
        if not display_texto.isdigit():
            print('Não tem nada para colocar no valor da esquerda')
            return

        # Se houver algo no número da esquerda,
        # não fazemos nada. Aguardaremos o número da direita.
        if self._num_esquerda is None:
            self._num_esquerda = float(display_texto)

        self._operador = botao_texto
        self.equation = f'{self._num_esquerda} {self._operador} ??'