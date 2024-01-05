
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

# ============ Gerenciamento "aplicação" ==============
app = QApplication(sys.argv) # gerencia a aplicação

# ============= Gerenciamento "janela" ================
window = QMainWindow() # uma classe que representa uma janela principal
central_widget = QWidget() # gerencia janela criada
window.setCentralWidget(central_widget) #  definir o conteúdo exibido no centro da janela principal

window.setWindowTitle('Minha janela bonita') # titulo da janela

# =========== Gerenciamento Layout "janela"============
layout = QGridLayout() # classe que alinha os widget em linha e coluna (grade de exibição) 
central_widget.setLayout(layout) # método = "Classe Container" para layout

# ====================== widgets =====================
botao1 = QPushButton('Botão 1') # widget botão
botao1.setStyleSheet('font-size: 70px;') # tamanho

botao2 = QPushButton('Botão 2') # widget botão
botao2.setStyleSheet('font-size: 40px;') # tamanho

botao3 = QPushButton('Botão 3') # widget botão
botao3.setStyleSheet('font-size: 40px;') # tamanho

botao4 = QPushButton('Botão 4') # widget botão
botao4.setStyleSheet('font-size: 40px;') # tamanho

botao5 = QPushButton('Botão 5') # widget botão
botao5.setStyleSheet('font-size: 40px;') # tamanho

# grade de exibição na janela (layout)
layout.addWidget(botao1, 1, 1, 1, 1) # (widget, linha, coluna, expandir_linha, expandir_coluna)
layout.addWidget(botao2, 1, 4, 3, 1) # (widget, linha, coluna, expandir_linha, expandir_coluna)
layout.addWidget(botao3, 2, 3, 1, 1) # (widget, linha, coluna, expandir_linha, expandir_coluna)
layout.addWidget(botao4, 3, 1, 2, 1) # (widget, linha, coluna, expandir_linha, expandir_coluna)
layout.addWidget(botao5, 4, 2, 2, 3) # (widget, linha, coluna, expandir_linha, expandir_coluna)

# ================================= FUNÇÕES ====================================
@Slot()
def primeiro_slot(status_bar): # função "primeira_acao"
    def inner():
        status_bar.showMessage('O meu slot foi executado')
    return inner


@Slot()
def segundo_slot(checked): # função "segunda_acao"
    print('Está marcado?', checked)


@Slot()
def terceiro_slot(action): # função "botao1.clicked"
    def inner():
        segundo_slot(action.isChecked()) # isChecked() retorna um valor booleano indicando pelo (Checkbox)
    return inner

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

# ================================ MENU ===================================
menu = window.menuBar() # cria barra do menu
primeiro_menu = menu.addMenu('Primeiro elemento do menu') # widget = menu
primeira_acao = primeiro_menu.addAction('Primeira de ação') # widget = submenu de ação
status_bar = window.statusBar() # usado para verificar status da janela principal (ação executada)
primeira_acao.triggered.connect(primeiro_slot(status_bar)) # função da ação a ser executada
'''
primeira_acao | .triggered | .connect | (lambda: | primeiro_slot | (status_bar))

Aqui está uma explicação mais detalhada dos da linha de código acima:

# "primeira_acao": é um objeto da classe QAction que representa a ação primeira_acao;
# ".triggered": é um sinal da classe QAction que é emitido quando a ação é clicada pelo usuário;
# ".connect()": é um método da classe QAction que é usado para conectar a uma ação ou objeto;
# "lambda": é uma função anônima que é usada para definir uma ação;
# "primeiro_slot()": ação executada = função ou slot;
# "status_bar": verificar status da ação.

documentação: https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#qaction
'''

status_bar.showMessage('Décio Santana de Aguiar') # ver mensagem (roda pé janela)

segunda_acao = primeiro_menu.addAction('Segunda ação') # widget = submenu de ação
segunda_acao.setCheckable(True) # permite que o botão represente um estado binário ativo ou inativo (Checkbox)
segunda_acao.toggled.connect(segundo_slot) # ".toggled" verifica alteração de status pelo usuário (Click) 
segunda_acao.hovered.connect(terceiro_slot(segunda_acao))
'''
".hovered" é um sinal emitido quando uma ação é destacada pelo usuário, 
quando o usuário passa o cursor sobre: 
    # uma opção de menu;
    # uma  barra de ferramentas;
    # pressiona uma combinação de teclas de atalho de uma ação.
'''
# =====================================================================

# Botão (widgets)
botao1.clicked.connect(terceiro_slot(segunda_acao)) # .clicked verifica se botão foi clicado pelo usuário

# =================== exibição e loop =================
window.show()  # window = QMainWindow() => janela  |.show() => mostra janela
app.exec()  # O loop da aplicação