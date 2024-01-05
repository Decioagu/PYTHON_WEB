import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QLabel


if __name__ == '__main__':
    # ============ Gerenciamento "aplicação" ==============
    app = QApplication(sys.argv)

    # ============= Gerenciamento "janela principal" ================
    # "QVBoxLayout" inicia uma janela vertical
    window = MainWindow() # módulo "main_window"

    # ============= texto da janela principal =============
    label1 = QLabel('O meu texto') # texto
    label1.setStyleSheet('font-size: 100px;') # tamanho
    window.v_layout.addWidget(label1) # escrever (objeto, linha, coluna, expandir_linha, expandir_coluna)

    # ======== ajuste tamanho da janela principal =========
    window.adjustFixedSize() # métopo para ajuste da janela (módulo "main_window")

    # =================== exibição e loop =================
    window.show() # mostrar janela
    app.exec()  # O loop da aplicação