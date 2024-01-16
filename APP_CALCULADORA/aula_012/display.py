from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QKeyEvent
from variaveis import FONTE_GRANDE_SIZE, LARGURA_JANELA, MARGEM_TEXTO, FONTE_PEQUENO_SIZE
from uteis import valor_numerico

class Display(QLineEdit):
    enterPrecionado = Signal(str)
    deletarPrecionado = Signal(str)
    limparPrecionado = Signal()
    numeroPrecionado = Signal(str)
    operadorPrecionado = Signal(str)
    '''
    Em PySide6.QtCore, um Signal() é uma classe que representa um evento que pode ser 
    emitido por um objeto. Um Signal() pode ter zero ou mais argumentos, que são os 
    dados que são transmitidos quando o evento é emitido.
    '''

    # ======================= Construtor =========================
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        # self.setReadOnly(True) # não permite acesso ao display
        self.configStyle() # método 

    # ======================== Método ============================
    def configStyle(self): # (QLineEdit) configuração do display

        # estilo do texto (cor de fundo, cor do texto ,tamanho)
        self.setStyleSheet(f'background-color: red; color: black; font-size: {FONTE_GRANDE_SIZE}px') 
        # https://doc.qt.io/qtforpython-6/overviews/stylesheet-examples.html

        # espaço margem do texto
        margem = [MARGEM_TEXTO for _ in range(4)] 
        self.setTextMargins(*margem)

        # dimensão espaço do texto
        self.setMinimumHeight(FONTE_GRANDE_SIZE * 2) # definir a "altura" mínima de um widget
        self.setMinimumWidth(LARGURA_JANELA) # definir a "largura" mínima de um widget
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

    # identifica tecla pressionada no teclado (impede escrita no display)
    def keyPressEvent(self, evento: QKeyEvent) -> None:
        # =============== teclado =================
        # print('Tecla pressionada =',evento.text())
        # print('Código da tecla =',evento.key()) 
        # return super().keyPressEvent(evento) # retorno p/ identificação das teclas
        # ==========================================
        key = evento.key()
        KEYS = Qt.Key
        
        texto_digitado = evento.text().strip() # widget em texto sem espaço

        # elementos do teclado
        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal] # tecla Enter, Retorno, igual
        isDelete = key in [KEYS.Key_Escape, KEYS.Key_C, KEYS.Key_Delete] # tecla Esc, C, Delete
        isLimpar  = key in [KEYS.Key_Backspace, KEYS.Key_Space] # tecla Backspace, Barra de Espaço


        if isEnter:
            print('isEnter pressionado, signal emitido', type(self).__name__, '/ método "keyPressEvent"')
            self.enterPrecionado.emit('Enter') # emitir evento
            return evento.ignore() # ignorar evento
        
        if isDelete:
            print('isDelete pressionado, sinal emitido', type(self).__name__, '/ método "keyPressEvent"')
            self.deletarPrecionado.emit('Deletado') # emitir evento
            return evento.ignore() # ignorar evento

        if isLimpar:
            print('isLimpar pressionado, sinal emitido', type(self).__name__, '/ método "keyPressEvent"')
            self.limparPrecionado.emit() # emitir evento
            return evento.ignore() # ignorar evento
        
        # numero
        if valor_numerico(texto_digitado):
            print('numero pressionado, sinal emitido', texto_digitado, '/ método "keyPressEvent"')
            self.numeroPrecionado.emit(texto_digitado) # emitir evento
            return evento.ignore() # ignorar evento
        
        # operador
        if texto_digitado in '+-/*^':
            print('operador pressionado, sinal emitido', texto_digitado, '/ método "keyPressEvent"')
            self.operadorPrecionado.emit(texto_digitado) # emitir evento
            return evento.ignore() # ignorar evento
        
class Info(QLabel):
    # ======================= Construtor =========================
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle() # Método

    # ======================== Método ============================
    def configStyle(self):
        self.setStyleSheet(f'font-size: {FONTE_PEQUENO_SIZE}px;') # estilo do texto (tamanho)
        self.setAlignment(Qt.AlignmentFlag.AlignRight) # alinhamento pela direita