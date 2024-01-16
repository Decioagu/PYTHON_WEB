from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QMessageBox


class MainWindow(QMainWindow):
    # ============= Superclasse QMainWindow() ================
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs) 

        # ============= Gerenciamento "janela" ================
        self.cw = QWidget() # classe para gerencia janela criada
        self.setCentralWidget(self.cw) # definir o conteúdo exibido no centro da janela principal

        # =========== Gerenciamento Layout "janela principal"============
        self.vertical_layout = QVBoxLayout() # classe de layout que alinha os widgets verticalmente
        self.cw.setLayout(self.vertical_layout) # método = "Classe Container" para layout

        self.setWindowTitle('Calculadora') # Título da janela

    # ======================= Métodos =========================
    # Janela principal
    def adjustFixedSize(self): 
        self.adjustSize() # usado para ajustar o tamanho de um widget ou janela
        self.setFixedSize(self.width(), self.height()) # ajuste fixo automático conforme conteúdo (largura, altura)

    # Widgets
    def addWidgetLayout(self, widget: QWidget):
            self.vertical_layout.addWidget(widget) # widgets interfaces gráficas do usuário 

    # caixa de diálogo para usuário
    def makeMsgBox(self):
        return QMessageBox(self)
    '''
    A biblioteca QMessageBox() é uma classe do Qt que fornece uma maneira conveniente de 
    exibir caixas de diálogo de mensagem. Essas caixas de diálogo podem ser usadas para 
    exibir mensagens de informação, aviso ou erro, ou para solicitar uma resposta do usuário.

    O parâmetro parent especifica o widget pai da caixa de diálogo. O parâmetro flags 
    especifica as flags da janela da caixa de diálogo.

    Depois de criar uma caixa de diálogo de mensagem, você pode configurar suas propriedades 
    usando os seguintes métodos:

    # setIcon(): define o ícone da caixa de diálogo.
    # setText(): define o texto da caixa de diálogo.
    # setInformativeText(): adicionar texto da caixa de diálogo.
    # setWindowTitle(): define o título da caixa de diálogo.
    # setButtonText(): define os botões padrão da caixa de diálogo.
    # setStandarButtons(): é usada para definir os botões padrão que serão exibidos em uma caixa de mensagem

    Os botões padrão são os botões que aparecem na parte inferior da caixa de diálogo. 
    Os botões padrão disponíveis são:

    # QMessageBox::Ok: indica que o usuário concorda com a mensagem.
    # QMessageBox::Cancel: indica que o usuário não concorda com a mensagem.
    # QMessageBox::Yes: indica que o usuário deseja continuar.
    # QMessageBox::No: indica que o usuário deseja cancelar.
    # QMessageBox::Abort: indica que o usuário deseja abortar a operação.
    # QMessageBox::Retry: indica que o usuário deseja tentar novamente.
    # QMessageBox::Ignore: indica que o usuário deseja ignorar a mensagem.
    '''  
            
