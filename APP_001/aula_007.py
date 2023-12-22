# -> QApplication (app)
#   -> QMainWindow (window)
#       -> QWidget (central_widget)
#           -> QGridLayout (layout)
#               -> QPushButton (botao1)
#               -> QPushButton (botao2)
#               -> QPushButton (botao3)
#   -> função
#   -> Menu
# -> show
# -> exec

'''
A classe QMainWindow() é uma classe que representa uma janela principal do Qt. 
Ela fornece uma estrutura básica para o desenvolvimento de interfaces gráficas com Qt.

Uma janela principal é uma janela que geralmente contém uma barra de menus, 
uma barra de ferramentas e um widget central. A barra de menus é usada para 
fornecer acesso a comandos e ações da aplicação. A barra de ferramentas é usada 
para fornecer acesso rápido a comandos e ações comuns. O widget central é usado 
para exibir o conteúdo principal da janela.
'''

import sys
from PySide6.QtWidgets import QApplication, QGridLayout, QMainWindow, QPushButton, QWidget

# ============ Gerenciamento "aplicação" ==============
app = QApplication(sys.argv) # gerencia a aplicação

# ============= Gerenciamento "janela" ================
window = QMainWindow() # uma classe que representa uma janela principal
central_widget = QWidget() # gerencia janela criada
window.setCentralWidget(central_widget) #  definir o conteúdo exibido no centro da janela principal

window.setWindowTitle('Minha janela bonita') # titulo da janela

# =========== Gerenciamento Layout "janela"============
layout = QGridLayout() # gerencia janela em forma de linha e coluna
central_widget.setLayout(layout) # método = "Classe Container" para layout

# ====================== widgets ======================
botao1 = QPushButton('Botão 1') # botão
botao1.setStyleSheet('font-size: 70px;') # tamanho

botao2 = QPushButton('Botão 2') # botão
botao2.setStyleSheet('font-size: 40px;') # tamanho

botao3 = QPushButton('Botão 3') # botão
botao3.setStyleSheet('font-size: 40px;') # tamanho

botao4 = QPushButton('Botão 4') # botão
botao4.setStyleSheet('font-size: 40px;') # tamanho

botao5 = QPushButton('Botão 5') # botão
botao5.setStyleSheet('font-size: 40px;') # tamanho

# grade de exibição na janela (principal)
layout.addWidget(botao1, 1, 1, 1, 1) # (objeto, linha, coluna, expandir_linha, expandir_coluna)
layout.addWidget(botao2, 1, 4, 3, 1) # (objeto, linha, coluna, expandir_linha, expandir_coluna)
layout.addWidget(botao3, 2, 3, 1, 1) # (objeto, linha, coluna, expandir_linha, expandir_coluna)
layout.addWidget(botao4, 3, 1, 2, 1) # (objeto, linha, coluna, expandir_linha, expandir_coluna)
layout.addWidget(botao5, 4, 2, 2, 3) # (objeto, linha, coluna, expandir_linha, expandir_coluna)

# ================================= FUNÇÕES ====================================
# função da ação a ser executada (Menu)
def slot_example(status_bar):
    status_bar.showMessage('O meu slot foi executado!!!') # ver mensagem (roda pé janela)

# ================================ MENU ===================================
menu = window.menuBar() # cria barra do menu
primeiro_menu = menu.addMenu('Primeiro elemento do menu') # adicionar opção ao meu
primeira_acao = primeiro_menu.addAction('Execução de ação') # Adicionar ação ao menu
status_bar = window.statusBar() # usado para verificar status da janela principal (ação executada)
primeira_acao.triggered.connect(lambda: slot_example(status_bar)) # função da ação a ser executada

status_bar.showMessage('Décio Santana de Aguiar') # ver mensagem (roda pé janela)

'''
primeira_acao | .triggered | .connect | (lambda: | slot_example | (status_bar))

Aqui está uma explicação mais detalhada dos da linha de código acima:

# "primeira_acao": é um objeto da classe QAction que representa a ação primeira_acao;
# ".triggered": é um sinal da classe QAction que é emitido quando a ação é clicada pelo usuário;
# ".connect()": é um método da classe QAction que é usado para conectar a uma ação ou objeto;
# "lambda": é uma função anônima que é usada para definir uma ação;
# "slot_example()": ação executada = função ou slot;
# "status_bar": verificar status da ação.

documentação: https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#qaction
'''

# =================== exibição e loop =================
window.show()  # window = QMainWindow() => janela  |.show() => mostra janela
app.exec()  # O loop da aplicação