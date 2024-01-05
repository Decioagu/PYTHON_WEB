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
        self.configStyle() # método

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
            ['',  '0', '.', '='],
        ]
        self._makeGrid() # método  

        self.equation = 'variável para manipulação de self.info em função "equation" '  

    # ======================== Método ============================
    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        for linha_number, linha_info in enumerate(self._gridMask):
            for coluna_numero, botao_texto in enumerate(linha_info):
                botao = Botoes(botao_texto) # class Botoes('texto')

                # widgets interfaces gráficas do usuário
                self.addWidget(botao, linha_number, coluna_numero)
           
                # acionamento das funções (display)
                buttonSlot = self._makeButtonDisplaySlot(
                    self._insertButtonTextToDisplay,
                    botao,
                )

                # .clicked.connect() identifica ação de (Click) no botão
                botao.clicked.connect(buttonSlot) # acionamento das funções (display)
    
    # atrasa execução da função ( _insertButtonTextToDisplay)
    def _makeButtonDisplaySlot(self, func, *args, **kwargs):
        @Slot()
        def realSlot():
            func(*args, **kwargs)
        return realSlot

    # função de inserção de texto no display
    def _insertButtonTextToDisplay(self, botao):
        botao_texto = botao.text() # método que retorna uma str em um widget.
        
        # concatena str display na variável "newDisplayValue"
        newDisplayValue = self.display.text() + botao_texto 

        # função (módulo "main_window")
        if not valor_numerico(newDisplayValue): # se não for número 
            return # não retorna nada
        else: # se for número
            self.display.insert(botao_texto) # inserir um elemento em uma lista (ver no display)