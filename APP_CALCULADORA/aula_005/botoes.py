from PySide6.QtWidgets import QPushButton, QGridLayout
from variaveis import (FONTE_MEDIO_SIZE, PRIMEIRA_COR, SEGUNDA_COR, TERCEIRA_COR, QUARTA_COR, 
                       QUINTA_COR, SEXTA_COR, SETIMA_COR)


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
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self._makeGrid() # método

    def _makeGrid(self):
        for linha_number, linha_info in enumerate(self._gridMask):
            for coluna_numero, texto_botao in enumerate(linha_info):
                botao = Botoes(texto_botao) # class Botoes('texto')            

                self.addWidget(botao, linha_number, coluna_numero)