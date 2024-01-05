import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from variaveis import PASTA_ICON
from display import Display, Info
from botoes import Botoes, BotoesGrid

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

    # ============= Gerenciamento "janela principal" ================
    # "QVBoxLayout" inicia uma janela vertical
    window = MainWindow() # módulo "main_window"
    
    # ================== Define o ícone ===================
    icon = QIcon(str(PASTA_ICON)) # caminho (módulo "variables")
    window.setWindowIcon(icon) # ícone na janela 
    app.setWindowIcon(icon) # ícone no aplicativo

    # ================== Módulo display ===================
    info = Info('2.0 ^ 10.0 = 1024') # exibir informações
    window.addWidgetLayout(info) # método widgets (módulo "main_window") 

    display = Display('0123456789') # recebe qualquer argumento
    window.addWidgetLayout(display) # método widgets (módulo "main_window")

    # ================== Módulo botoes ===================
    botao_1 = Botoes('Texto do botão')
    window.addWidgetLayout(botao_1) # método widgets (módulo "main_window")

    botao_2 = Botoes('Texto do botão')
    window.addWidgetLayout(botao_2) # método widgets (módulo "main_window")

    # "QGridLayout" inicia uma janela de grade (linha e coluna)
    botoeGrid = BotoesGrid() # inicia uma janela de grade (linha e coluna) 
    window.vertical_layout.addLayout(botoeGrid) # adiciona "BotoesGrid()" na janela principal

    # ======== Ajuste tamanho da janela principal =========
    window.adjustFixedSize() # métopo para ajuste da janela (módulo "main_window")# métopo para ajuste tamanho da janela window (largura, altura)

    # =================== Exibição e loop =================
    window.show() # mostrar janela
    app.exec()  # O loop da aplicação