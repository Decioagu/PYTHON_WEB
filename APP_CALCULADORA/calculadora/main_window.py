from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QMessageBox

class MainWindow(QMainWindow):
    # ============= Superclasse QMainWindow() ================
    # construtor
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

    # Criar widgets
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

    Depois de criar uma caixa de diálogo de mensagem, 
    você pode configurar suas propriedades usando os seguintes métodos:

    # setIcon(): define o ícone da caixa de diálogo.
    # setText(): define o texto da caixa de diálogo.
    # setInformativeText(): adicionar texto da caixa de diálogo.
    # setWindowTitle(): define o título da caixa de diálogo.
    # setStandarButtons(): definir os botões padrão que serão exibidos em uma caixa de mensagem
    # setButtonText(): # renomear os botões padrão da caixa de diálogo

    Os botões padrão disponíveis são:

    # QMessageBox.Ok: Botão "OK"
    # QMessageBox.Cancel: Botão "Cancelar"
    # QMessageBox.Yes: Botão "Sim"
    # QMessageBox.No: Botão "Não"
    # QMessageBox.Abort: Botão "Cancelar"
    # QMessageBox.Retry: Botão "Tentar novamente"
    # QMessageBox.Ignore: Botão "Ignorar"
    # QMessageBox.YesAll: Botão "Sim para todos"
    # QMessageBox.NoAll: Botão "Não para todos"
    # QMessageBox.Close: Botão "Fechar"

    Exemplo:
    def _showVazio(self, text):
        msgBox = self.window.makeMsgBox() # (módulo "main_window")
        msgBox.setText(text) # exibi texto na caixa de diálogo
        msgBox.setIcon(msgBox.Icon.Warning) # define o ícone da caixa de diálogo.
        msgBox.setWindowTitle("Vazio") # define o título da caixa de diálogo.
        msgBox.setStandardButtons(msgBox.StandardButton.Ok | msgBox.StandardButton.Cancel) # define os botões padrão da caixa de diálogo.
        msgBox.setButtonText(msgBox.StandardButton.Ok, "Abrir") # renomear os botões padrão da caixa de diálogo
        msgBox.setButtonText(msgBox.StandardButton.Cancel, "Fechar") # renomear os botões padrão da caixa de diálogo
        result = msgBox.exec() # executa a caixa de diálogo

        if result == msgBox.StandardButton.Ok:
            print('Caixa de diálogo = Abrir')
        elif result == msgBox.StandardButton.Cancel:
            print('Caixa de diálogo = Fechar')
    '''  
            
