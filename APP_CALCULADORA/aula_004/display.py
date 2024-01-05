from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONT_SIZE, MINIMUM_WIDTH, TEXT_MARGIN, SMALL_FONT_SIZE
from PySide6.QtWidgets import QLabel, QWidget


class Display(QLineEdit):
    # ======================= Construtor =========================
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.configStyle() # método 

    # ======================== Método ============================
    def configStyle(self): # (QLineEdit) configuração do display

        # estilo do texto (cor de fundo, tamanho)
        self.setStyleSheet(f'background-color: red; font-size: {BIG_FONT_SIZE}px') 

        # espaço margem do texto
        margins = [TEXT_MARGIN for _ in range(4)] 
        self.setTextMargins(*margins)

        # dimensão espaço do texto
        self.setMinimumHeight(BIG_FONT_SIZE * 2) # definir a "altura" mínima de um widget
        self.setMinimumWidth(MINIMUM_WIDTH) # definir a "largura" mínima de um widget
        self.setAlignment(Qt.AlignmentFlag.AlignRight) # alinhamento pela direita
        
    '''
    O método .setAlignment() é usado para definir o alinhamento de um widget. 
    Ele especifica como o conteúdo do widget será alinhado dentro do widget.
    O valor de alinhamento pode ser um dos seguintes:
        # Qt.AlignLeft: Alinha o conteúdo à esquerda do widget.
        # Qt.AlignRight: Alinha o conteúdo à direita do widget.
        # Qt.AlignCenter: Alinha o conteúdo ao centro do widget.
        # Qt.AlignTop: Alinha o conteúdo ao topo do widget.
        # Qt.AlignBottom: Alinha o conteúdo ao fundo do widget.
        # Qt.AlignHCenter: Alinha o conteúdo ao centro horizontal do widget.
        # Qt.AlignVCenter: Alinha o conteúdo ao centro vertical do widget.

    '''   

class Info(QLabel):
    # ======================= Construtor =========================
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle() # Método

    # ======================== Método ============================
    def configStyle(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;') # estilo do texto (tamanho)
        self.setAlignment(Qt.AlignmentFlag.AlignRight) # alinhamento pela direita