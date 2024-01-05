from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    # ============= superclasse QMainWindow() ================
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs) 

        # ============= Gerenciamento "janela" ================
        self.cw = QWidget() # gerencia janela criada
        self.setCentralWidget(self.cw) # definir o conteúdo exibido no centro da janela principal


        # =========== Gerenciamento Layout "janela principal"============
        self.v_layout = QVBoxLayout() #  classe de layout que alinha os widgets verticalmente
        self.cw.setLayout(self.v_layout) # método = "Classe Container" para layout

        self.setWindowTitle('Calculadora') # Título da janela

    # ======================= Métodos =========================
    def adjustFixedSize(self):   
        self.adjustSize() # usado para ajustar o tamanho de um widget ou janela
        self.setFixedSize(self.width(), self.height()) # ajuste fixo automático conforme conteúdo (largura, altura)
