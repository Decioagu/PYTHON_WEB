# aula 338
# pip install PySide6
# PySide6 para GUI (interface gráfica) com Qt em Python - Instalação
# - A seção original desse curso usou PyQt5 (estamos atualizando para PySide6)
# - Essas bibliotecas (PySide e PyQt) usam a biblioteca Qt
# - Qt é uma biblioteca usada para a criação de GUI (interface gráfica
#   do usuário) escrita em C++.
#   - PySide e PyQt conseguem fazer a ponte (binding) entre o Python e a
#   biblioteca para a criação de interfaces gráficas sem ter que usar outra
#   linguagem de programação.
# - PySide6 é uma referencia à versão 6 da Qt (Qt 6)
# - Qt é multiplataforma, ou seja, deve funcionar em Windows, Linux e Mac.

# Por que mudei de PyQt para PySide na atualização?
# - PySide foi desenvolvido pela The Qt Company (da Nokia), como parte do
#   projeto Qt for Python project - https://doc.qt.io/qtforpython/
# - Por usarem a mesma biblioteca (Qt), PySide e PyQt são extremamente
#   similares, muitas vezes os códigos são idênticos. Portanto, mesmo que você
#   ainda queira usar PyQt, será muito simples portar os códigos. Muitas vezes
#   basta trocar o nome de PySide para PyQt e vice-versa.
#   https://tldrlegal.com/license/gnu-lesser-general-public-license-v3-(lgpl-3)

# - A maior diferença entre PyQt e PySide está na licença:
#   PyQt usa GPL ou commercial e PySide usa LGPL.
#   Em resumo: com PySide, você tem a permissão uso da biblioteca para fins
#   comerciais, sem ter que compartilhar o código escrito por você para o
#   público.
#   Licenças são tópicos complexos, portanto, se oriente sobre elas
#   antes de usar qualquer software de terceiros.

'''
    O PySide é uma biblioteca Python que fornece uma API para o toolkit Qt, 
    um framework de desenvolvimento de aplicações multiplataforma. Com o PySide, 
    você pode criar interfaces gráficas de usuário (GUI) para seus aplicativos Python, 
    utilizando componentes visuais como botões, menus, caixas de diálogo e outros elementos.

    Principais funcionalidades do PySide:

    Criação de interfaces gráficas de usuário:
        # Suporta diversos componentes visuais, como botões, menus, caixas de diálogo, 
        barras de ferramentas, etc.
        # Possui suporte a layout, estilo e animação.
    Interação com o usuário:
        # Suporta eventos de entrada do usuário, como cliques do mouse, pressionamentos 
        de teclas e movimentos do mouse.
        # Permite a criação de diálogos e caixas de diálogo para coletar dados do usuário.
    Acessibilidade:
        # Possui suporte a acessibilidade, permitindo que seus aplicativos sejam usados 
        por pessoas com deficiência.
    Multiplataforma:
        # Funciona em todos os sistemas operacionais suportados pelo Qt, incluindo Windows, 
        macOS, Linux e Android.
'''

import sys
from PySide6.QtWidgets import QApplication, QPushButton

# ============ Gerenciamento "aplicação" ==============
app = QApplication(sys.argv) # gerencia a aplicação

# ====================== widgets ======================
''' widgets são componentes visuais que são usados para criar interfaces gráficas do usuário '''
botao = QPushButton('Texto do botão') # widget botão 
botao.setStyleSheet('font-size: 30px; color: red;') # tamanho do botão
# =====================================================

# =================== exibição e loop =================
botao.show()  # Adiciona o widget na hierarquia e exibe a janela
app.exec()  # O loop da aplicação

'''
O método .setStyleSheet() atribui um estilo a um widget. O estilo pode ser uma 
string contendo o código CSS do estilo ou um objeto QStylesheet.

Definir a "cor" do texto:
    # QLabel label("Olá, mundo!");
    # label.setStyleSheet("color: red;");
Esse código irá definir a cor do texto do label para vermelho.

Definir a "fonte" do texto:
    # QLabel label("Olá, mundo!");
    # label.setStyleSheet("font-family: Arial; font-size: 16px;");
Esse código irá definir a fonte do texto do label para Arial, tamanho 16px.

Definir o "tamanho" do widget:
    # QPushButton button("Clique aqui!");
    # button.setStyleSheet("width: 100px; height: 50px;");
Esse código irá definir o tamanho do botão para 100px de largura e 50px de altura.

Definir a "posição" do widget:
    # QPushButton button("Clique aqui!");
    # button.setStyleSheet("top: 10px; left: 10px;");
Esse código irá definir a posição do botão para 10px da borda superior da janela e 10px da borda esquerda da janela.

Definir o "estilo da borda" do widget:
    # QPushButton button("Clique aqui!");
    # button.setStyleSheet("border-width: 1px; border-color: red;");
Esse código irá definir a largura da borda do botão para 1px e a cor da borda para vermelho.

Definir o "estilo da sombra" do widget:
    # QPushButton button("Clique aqui!");
    # button.setStyleSheet("box-shadow: 0px 0px 10px red;");
Esse código irá definir uma sombra de 10px de raio com cor vermelha ao redor do botão.
'''