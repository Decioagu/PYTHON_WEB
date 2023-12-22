
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
from PySide6.QtCore import Slot

class MyWindow(QMainWindow): # superclasse que representa uma janela principal

    # =============== superclasse QMainWindow() =============== 
    def __init__(self, parent=None): # construtor 
        super().__init__(parent) 

        # ============= Gerenciamento "janela" ================
        self.central_widget = QWidget() # gerencia janela criada
        self.setCentralWidget(self.central_widget) #  definir o conteúdo exibido no centro da janela principal

        self.setWindowTitle('Minha janela bonita') # titulo da janela

        # =========== Gerenciamento Layout "janela"============
        self.layout = QGridLayout() # gerencia janela em forma de linha e coluna (grade de exibição)
        self.central_widget.setLayout(self.layout) # método = "Classe Container" para layout
       
        # ====================== widgets =====================
        self.botao1 = self.make_button('Botão 1') # método botão 
        self.botao1.clicked.connect(self.segundo_metodo) # .clicked verifica se botão foi clicado pelo usuário

        self.botao2 = self.make_button('Botão 2') # método botão

        self.botao3 = self.make_button('Botão 3') # método botão

        self.botao4 = self.make_button('Botão 4') # método botão

        self.botao5 = self.make_button('Botão 5') # método botão
        
        # grade de exibição na janela (self.layout)
        self.layout.addWidget(self.botao1, 1, 1, 1, 1) # (objeto, linha, coluna, expandir_linha, expandir_coluna)
        self.layout.addWidget(self.botao2, 1, 4, 3, 1) # (objeto, linha, coluna, expandir_linha, expandir_coluna)
        self.layout.addWidget(self.botao3, 2, 3, 1, 1) # (objeto, linha, coluna, expandir_linha, expandir_coluna)
        self.layout.addWidget(self.botao4, 3, 1, 2, 1) # (objeto, linha, coluna, expandir_linha, expandir_coluna)
        self.layout.addWidget(self.botao5, 4, 2, 2, 3) # (objeto, linha, coluna, expandir_linha, expandir_coluna)

        # ================================ MENU ===================================
        self.menu = self.menuBar() # cria barra do menu
        self.primeiro_menu = self.menu.addMenu('Primeiro elemento do menu') # adicionar opção ao meu
        self.primeira_acao = self.primeiro_menu.addAction('Primeira de ação') # Adicionar ação ao menu
        self.status_bar = self.statusBar() # usado para verificar status da janela principal (ação executada)
        self.primeira_acao.triggered.connect(self.primeiro_metodo) # função da ação a ser executada
        '''
        primeira_acao | .triggered | .connect | (lambda: | primeiro_metodo | (status_bar))

        Aqui está uma explicação mais detalhada dos da linha de código acima:

        # "primeira_acao": é um objeto da classe QAction que representa a ação primeira_acao;
        # ".triggered": é um sinal da classe QAction que é emitido quando a ação é clicada pelo usuário;
        # ".connect()": é um método da classe QAction que é usado para conectar a uma ação ou objeto;
        # "self.primeiro_metodo" uso do método da class

        documentação: https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#qaction
        '''
        
        self.status_bar.showMessage('Décio Santana de Aguiar') # ver mensagem (roda pé janela)

        self.segunda_acao = self.primeiro_menu.addAction('Segunda ação') # Adicionar ação ao menu
        self.segunda_acao.setCheckable(True) # permite que o botão represente um estado binário ativo ou inativo (Checkbox)
        self.segunda_acao.toggled.connect(self.segundo_metodo) # ".toggled" verifica alteração de status pelo usuário (Click)  
        self.segunda_acao.hovered.connect(self.segundo_metodo)
        '''
        ".hovered" é um sinal emitido quando uma ação é destacada pelo usuário, 
        quando o usuário passa o cursor sobre: 
            # uma opção de menu;
            # uma  barra de ferramentas;
            # pressiona uma combinação de teclas de atalho de uma ação.
        '''
    
    # ================================= Métodos ====================================
    @Slot()
    def primeiro_metodo(self): # função "primeira_acao"
        self.status_bar.showMessage('O meu slot foi executado')
       
    @Slot()
    def segundo_metodo(self): # função "segunda_acao"
        print('Está marcado?', self.segunda_acao.isChecked()) # isChecked() retorna um valor booleano indicando pelo (Checkbox)

    def make_button(self, text): # método botão
        btn = QPushButton(text) # botão
        btn.setStyleSheet('font-size: 40px;') # tamanho
        return btn
    

# ============ Gerenciamento "aplicação" ==============
app = QApplication(sys.argv) # gerencia a aplicação

# ============= Gerenciamento "janela" ================
window = MyWindow()

# =================== exibição e loop =================
window.show()  # window = QMainWindow() => janela  |.show() => mostra janela
app.exec()  # O loop da aplicação