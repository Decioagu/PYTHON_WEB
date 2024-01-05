import sys
from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # ============ Gerenciamento "aplicação" ==============
    app = QApplication(sys.argv)

    # ============= Gerenciamento "janela principal" ================
    # "QVBoxLayout" inicia uma janela vertical
    window = MainWindow() # módulo "main_window"

    # ================== Define o ícone ===================
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon) # ícone na janela 
    app.setWindowIcon(icon) # ícone no aplicativo

    # ============= texto da janela principal =============
    label1 = QLabel('O meu texto') # texto
    label1.setStyleSheet('font-size: 100px;') # tamanho
    window.v_layout.addWidget(label1) # escrever (objeto, linha, coluna, expandir_linha, expandir_coluna)

    # ======== Ajuste tamanho da janela principal =========
    window.adjustFixedSize() # métopo para ajuste da janela (módulo "main_window")# métopo para ajuste tamanho da janela window (largura, altura)

    # =================== Exibição e loop =================
    window.show() # mostrar janela
    app.exec()  # O loop da aplicação