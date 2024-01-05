'''
PySide6.QtWidgets oferece vários tipos de gerenciadores de layout para organizar 
seus widgets com flexibilidade e eficiência. Aqui estão alguns dos mais comuns:

OBS: widgets são componentes visuais que são usados para criar interfaces gráficas do usuário.

Layouts básicos:

    # QVBoxLayout: Organiza os widgets verticalmente, um em cima do outro. 
    Ideal para listas, caixas de diálogo, formulários simples.
    # QHBoxLayout: Organiza os widgets horizontalmente, um ao lado do outro. 
    Adequado para barras de ferramentas, painéis de botões, etc.

Layouts avançados:

    # QGridLayout: Posiciona os widgets em uma grade com linhas e colunas definidas. 
    Permite controle preciso do posicionamento e dimensionamento. Útil para tabelas, 
    layouts complexos, etc.
    # QStackedLayout: Exibe apenas um widget de cada vez em uma pilha. 
    Perfeito para páginas de configuração, painéis de controle, etc.
    # QFormLayout: Organiza os widgets em pares: rótulo seguido de widget 
    (campo de texto, caixa de seleção, etc.). Útil para formulários de entrada de dados.
    # QBoxLayout: Classe base para QVBoxLayout e QHBoxLayout. Permite criar 
    layouts personalizados estendendo esta classe.
    
Layouts complementares:

    # QScrollArea: Insere um layout dentro de uma área rolável, permitindo exibir 
    uma quantidade maior de conteúdo do que o espaço disponível.
    # QSplitter: Divide o espaço disponibilizado em várias áreas redimensionáveis, 
    possibilitando layouts flexíveis.
    # QTabWidget: Apresenta diferentes layouts em abas separadas. Adequado para 
    interfaces com seções distintas.

Documento gerenciamento de Layout: 
https://doc.qt.io/qt-6/layout.html
'''

# -> QApplication (app)
#   -> QWidget (central_widget)
#       -> QGridLayout (layout)
#           -> QPushButton (botao1)
#           -> QPushButton (botao2)
#           -> QPushButton (botao3)
# -> show
# -> exec

import sys
from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget, QLabel

# ============ Gerenciamento "aplicação" ==============
app = QApplication(sys.argv) # gerencia a aplicação

# ============= Gerenciamento "janela" ================
central_widget = QWidget() # gerencia janela criada

# =========== Gerenciamento Layout "janela"============
layout = QGridLayout() # classe que alinha os widget em linha e coluna (grade de exibição)
central_widget.setLayout(layout) # método = "Classe Container" para layout

texto = QLabel("Meu texto!!!") # adicionar texto
layout.addWidget(texto, 0, 2,1,2) # (widget, linha, coluna, expandir_linha, expandir_coluna)
texto.setStyleSheet('font-size: 20px; color: green') # tamanho e cor

# ====================== widgets ======================
botao1 = QPushButton('Botão 1') # widget botão 
botao1.setStyleSheet('font-size: 70px;') # tamanho

botao2 = QPushButton('Botão 2') # widget botão 
botao2.setStyleSheet('font-size: 40px;') # tamanho

botao3 = QPushButton('Botão 3') # widget botão 
botao3.setStyleSheet('font-size: 40px;') # tamanho

botao4 = QPushButton('Botão 4') # widget botão 
botao4.setStyleSheet('font-size: 40px;') # tamanho

# grade de exibição na janela (layout)
layout.addWidget(botao1, 1, 1, 1, 1) # (widget, linha, coluna, expandir_linha, expandir_coluna)
layout.addWidget(botao2, 1, 4, 2, 1) # (widget, linha, coluna, expandir_linha, expandir_coluna)
layout.addWidget(botao3, 2, 1, 1, 3) # (widget, linha, coluna, expandir_linha, expandir_coluna)
layout.addWidget(botao4, 3, 3, 1, 1) # (widget, linha, coluna, expandir_linha, expandir_coluna)

# =================== exibição e loop =================
central_widget.show()  # central_widget = QWidget() => gerencia hierarquia de widget |.show() => mostra janela
app.exec()  # O loop da aplicação