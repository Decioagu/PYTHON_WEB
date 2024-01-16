import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from variaveis import PASTA_ICON
from display import Display, Info
from botoes import BotoesGrid

from qt_material import apply_stylesheet
'''
    # QSS - Estilos do QT for Python
    # https://doc.qt.io/qtforpython/tutorials/basictutorial/widgetstyling.html
    # Dark Theme
    # https://pyqtdarktheme.readthedocs.io/en/latest/how_to_use.html
    # qt-material
    # https://pypi.org/project/qt-material/
    # qdarktheme
    # https://pypi.org/project/pyqtdarktheme/
'''

if __name__ == '__main__':
    # ============ Gerenciamento "aplicação" ==============
    app = QApplication(sys.argv) 
    apply_stylesheet(app, theme='dark_teal.xml') # qt-material (tema escuro)

    # ============= Gerenciamento "janela principal " ================
    # "QVBoxLayout" inicia uma janela vertical
    window = MainWindow() # módulo "main_window"
    
    # ================== Define o ícone ===================
    icon = QIcon(str(PASTA_ICON)) # caminho (módulo "variables")
    window.setWindowIcon(icon) # ícone na janela 
    app.setWindowIcon(icon) # ícone no aplicativo

    # ================== Módulo display ===================
    informacao_display = Info() # exibir informacao_display acima do display
    window.addWidgetLayout(informacao_display) # método widgets (módulo "main_window") 

    display = Display() # exibi informacao_display do teclado
    window.addWidgetLayout(display) # método widgets (módulo "main_window")

    # ================== Módulo botoes ===================
    # "QGridLayout" inicia uma janela de grade (linha e coluna)
    botoeGrid = BotoesGrid(display, informacao_display, window)  # adiciona "Display()" na janela de grade (linha e coluna)
    window.vertical_layout.addLayout(botoeGrid) # adiciona "BotoesGrid()" na janela principal

    # ======== Ajuste tamanho da janela principal =========
    # métopo para ajuste tamanho da janela window (módulo "main_window")
    window.adjustFixedSize() 
    # =================== Exibição e loop =================
    window.show() # mostrar janela
    app.exec()  # O loop da aplicação