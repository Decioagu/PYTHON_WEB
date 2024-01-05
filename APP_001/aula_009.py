
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

        # Título da janela
        self.setWindowTitle('Minha janela bonita') # titulo da janela

        # =========== Gerenciamento Layout "janela"============
        self.layout = QGridLayout() # classe que alinha os widget em linha e coluna (grade de exibição)
        self.central_widget.setLayout(self.layout) # método = "Classe Container" para layout
       
        # ====================== widgets =====================
        self.botao1 = self.make_button('Botão 1') # método botão 
        self.botao1.clicked.connect(self.segundo_metodo) # .clicked verifica se botão foi clicado pelo usuário

        self.botao2 = self.make_button('Botão 2') # método botão

        self.botao3 = self.make_button('Botão 3') # método botão

        self.botao4 = self.make_button('Botão 4') # método botão

        self.botao5 = self.make_button('Botão 5') # método botão
        
        # grade de exibição na janela (self.layout)
        self.layout.addWidget(self.botao1, 1, 1, 1, 1) # (widget, linha, coluna, expandir_linha, expandir_coluna)
        self.layout.addWidget(self.botao2, 1, 4, 3, 1) # (widget, linha, coluna, expandir_linha, expandir_coluna)
        self.layout.addWidget(self.botao3, 2, 3, 1, 1) # (widget, linha, coluna, expandir_linha, expandir_coluna)
        self.layout.addWidget(self.botao4, 3, 1, 2, 1) # (widget, linha, coluna, expandir_linha, expandir_coluna)
        self.layout.addWidget(self.botao5, 4, 2, 2, 3) # (widget, linha, coluna, expandir_linha, expandir_coluna)

        # ================================ MENU ===================================
        self.menu = self.menuBar() # cria barra do menu
        self.primeiro_menu = self.menu.addMenu('Primeiro elemento do menu') # widget = menu
        self.primeira_acao = self.primeiro_menu.addAction('Primeira de ação') # widget = submenu de ação
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

        self.segunda_acao = self.primeiro_menu.addAction('Segunda ação') # widget = submenu de ação
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
    # função "primeira_acao"
    def primeiro_metodo(self): 
        self.status_bar.showMessage('O meu slot foi executado')
       
    @Slot()
    # função "segunda_acao"
    def segundo_metodo(self): 
        print('Está marcado?', self.segunda_acao.isChecked()) # isChecked() retorna um valor booleano indicando pelo (Checkbox)
    
    # método botão
    def make_button(self, text): 
        btn = QPushButton(text) # widget botão
        btn.setStyleSheet('font-size: 40px;') # tamanho
        return btn
    ''' 
    Em PySide6, um slot é uma função ou método que pode ser conectado a um sinal. 
    Um sinal é um evento que é emitido por um widget ou outro objeto. 
    Quando um sinal é emitido, ele envia dados para todos os slots que estão conectados a ele.
    
    @Slot() É um decorador que marca uma função Python como um slot,
    nem sempre obrigatório.

    Conexões de slot de sinal:
    Ele permite que as funções sejam invocadas como uma resposta a sinais emitidos, 
    muitas vezes acionados por interações ou eventos do usuário.
    Exemplo: O sinal de um botão pode ser conectado a uma função de slot que manipula 
    a ação de clique no botão.clicked()

    Verificação de tipo e segurança:
    Os slots declaram seus tipos de argumento esperados, garantindo a compatibilidade de tipos 
    durante as conexões de slot de sinal. Isso evita possíveis erros e incompatibilidades.

    Meta-informações para Qt:
    O decorador fornece ao sistema de meta-objetos do Qt informações sobre o slot, 
    facilitando a introspecção e recursos dinâmicos.

    OBS:
    @Slot() nem sempre obrigatório:
    Embora recomendado para segurança de tipo e introspecção, os slots podem tecnicamente 
    funcionar sem o decorador "@Slot()" em certos casos. No entanto, é considerada uma boa prática 
    usá-lo de forma consistente.
    '''

# ============ Gerenciamento "aplicação" ==============
app = QApplication(sys.argv) # gerencia a aplicação

# ============= Gerenciamento "janela" ================
window = MyWindow()

# =================== exibição e loop =================
window.show()  # window = QMainWindow() => janela  |.show() => mostra janela
app.exec()  # O loop da aplicação