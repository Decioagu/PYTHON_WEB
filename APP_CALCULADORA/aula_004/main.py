import sys
from main_window import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH
from display import Display, Info


if __name__ == '__main__':
    # ============ Gerenciamento "aplicação" ==============
    app = QApplication(sys.argv)

    # ============= Gerenciamento "janela principal" ================
    # "QVBoxLayout" inicia uma janela vertical
    window = MainWindow() # módulo "main_window"

    # ================== Define o ícone ===================
    icon = QIcon(str(WINDOW_ICON_PATH)) # caminho (módulo "variables")
    window.setWindowIcon(icon) # ícone na janela 
    app.setWindowIcon(icon) # ícone no aplicativo

    # ================== Módulo display ===================
    info = Info('2.0 ^ 10.0 = 1024') # exibir informações
    window.addToVLayout(info) # método widgets (módulo "main_window") 

    display = Display('0123456789') # recebe qualquer argumento
    window.addToVLayout(display) # método widgets (módulo "main_window")

    # ======== Ajuste tamanho da janela principal =========
    window.adjustFixedSize() # métopo para ajuste da janela (módulo "main_window")# métopo para ajuste tamanho da janela window (largura, altura)

    # =================== Exibição e loop =================
    window.show() # mostrar janela
    app.exec()  # O loop da aplicação