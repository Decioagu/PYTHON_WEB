from PySide6.QtWidgets import QPushButton, QGridLayout
import math
from variaveis import (FONTE_MEDIO_SIZE, PRIMEIRA_COR, SEGUNDA_COR, TERCEIRA_COR, QUARTA_COR, 
                       QUINTA_COR, SEXTA_COR, SETIMA_COR)

from display import Display, Info
from PySide6.QtCore import Slot
from uteis import _valorNumerico, _valorInteiro
from main_window import MainWindow

class Botoes(QPushButton):
    # construtor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args = args
        self.configStyle() # método de estilo

    # ======================== Método ============================
    # método de estilo
    def configStyle(self):
        '''
        Em Python, o método .font() é usado para definir a fonte de um widget Tkinter. 
        O método aceita um único argumento, que é uma tupla que especifica as 
        propriedades da fonte.

        Python
        label = Label(root, text="Hello, world!")
        label.font = ("Arial", 12, "bold italic") # (fonte, tamanho, estilo)
        # '''
        self.setMinimumSize(75, 75) # (largura, altura)
        
        caracter = str(*self.args) # ('texto)   

        # Estilos cor e tamanho
        if caracter == '=':
            self.setStyleSheet(f"""
                                QPushButton {{
                                    background-color: {SETIMA_COR};
                                    color: white;  
                                }}
                                :hover {{
                                    background-color: {QUINTA_COR};
                                    color: white;
                                }}
                                :pressed {{
                                    background-color: {TERCEIRA_COR};
                                    color: white;
                                }}; 
                                font-size: {FONTE_MEDIO_SIZE}px
                            """)
        elif caracter.isdigit():
            self.setStyleSheet(f"""
                                QPushButton {{
                                    background-color: {PRIMEIRA_COR};
                                    color: white;  
                                }}
                                :hover {{
                                    background-color: {SEGUNDA_COR};
                                    color: white;
                                }}
                                :pressed {{
                                    background-color: {TERCEIRA_COR};
                                    color: white;
                                }}; 
                                font-size: {FONTE_MEDIO_SIZE}px
                            """)
        else:
            self.setStyleSheet(f"""
                                QPushButton {{
                                    background-color: {QUARTA_COR};
                                    color: white;  
                                }}
                                :hover {{
                                    background-color: {QUINTA_COR};
                                    color: white;
                                }}
                                :pressed {{
                                    background-color: {SEXTA_COR};
                                    color: white;
                                }}; 
                                font-size: {FONTE_MEDIO_SIZE}px
                            """)

            '''
            # estilo do texto (cor de fundo, cor do texto ,tamanho)
            # https://doc.qt.io/qtforpython-6/overviews/stylesheet-examples.html

            Para aplicar regras de estilo .setStyleSheet() em diferentes estados:
            # A regra de estilo QPushButton define o estilo do widget padrão. 
            # A regra de estilo :hover define o estilo do widget quando o mouse está sobre ele.
            # A regra de estilo :pressed define o estilo do widget quando ele é pressionado pelo usuário.
            '''

# 1º botoeGrid = BotoesGrid(display, informacao_display)
class BotoesGrid(QGridLayout):
    # construtor
    def __init__(self, display: Display, informacao_display: Info, window: MainWindow, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # teclado (widgets)
        self._gridMask = [
            ['C', '◀','^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N', '0', '.', '='],
        ]

        self.display = display # (módulo "display")
        self.informacao_display = informacao_display  # (módulo "display")
        self.window = window # (módulo "main_window")

        print('self.contador_auxiliar = 0')
        self.contador_auxiliar = 0 # auxilia no controle do sinal negativo "-"
        self._num_esquerda = None # numero esquerda do operador
        self._num_direita = None # numero direita do operador
        self._operador = None # operador matemático
        self._equationInitialValue = 'Sua conta' # valor inicial da equação
        self.equation = self._equationInitialValue # valor da equação
        self._makeGrid() # método  construção do teclado

    # ======================== Método ============================
    # exibir Info acima display (EQUAÇÃO)
    @property
    def equation(self):
        return self._equation
    # receber Info acima display
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.informacao_display.setText(value) # inserir texto

    # Botões do teclado
    def _makeGrid(self):

        # identifica tecla pressionada no teclado (modulo "display" - método "keyPressEvent")
        self.display.enterPrecionado.connect(self._igualClicked) # (módulo "display")
        self.display.limparPrecionado.connect(self.display.backspace) # (módulo "display")
        self.display.deletarPrecionado.connect(self._clear) # (módulo "display")
        self.display.numeroPrecionado.connect(self._recebimento_sinal_do_teclado) # (módulo "display")
        self.display.operadorPrecionado.connect(self._recebimento_sinal_do_teclado) # (módulo "display")
        self.display.pontoPrecionado.connect(self._recebimento_sinal_do_teclado) # (módulo "display")
        self.display.letra_nPrecionado.connect(self._converterNumeroNegativo) # (módulo "display")

        # gerar interface gráfica "teclado (widgets)"
        for linha_number, informacao_da_linha in enumerate(self._gridMask):
            for coluna_numero, botao_texto in enumerate(informacao_da_linha):
                botao = Botoes(botao_texto) # estilo do texto no botão

                # widgets interfaces gráficas do usuário (gerador os botões do teclado)
                print('método _makeGrid => botão clicado...')
                self.addWidget(botao, linha_number, coluna_numero)

                # acionamento das funções (display)
                botaoSlot = self._makeSlot(self._insertButtonTextToDisplay, botao)

                # Identifica clique no teclado (Click)
                self._connectButtonClicked(botao, botaoSlot)
                

    # identifica ação de (Click) no botão "widgets"
    def _connectButtonClicked(self, botao, botaoSlot):
        botao.clicked.connect(botaoSlot) # (Click)
    
    # atrasa execução da função (_insertButtonTextToDisplay)
    def _makeSlot(self, func, *args, **kwargs):
        @Slot()
        def realSlot():
            func(*args, **kwargs)
        return realSlot

    # método de inserção de texto no display (pela tecla da calculadora)
    @Slot()
    def _insertButtonTextToDisplay(self, botao):
        botao_texto = botao.text() # método que retorna uma str de um widget

        if botao_texto == 'C':
            print('método _insertButtonTextToDisplay => limpar')
            self._clear() # limpar

        if botao_texto == '◀':
            print('método _insertButtonTextToDisplay => backspace')
            self.display.backspace() # apagar um espaço

        if botao_texto == 'N':
            print('método _insertButtonTextToDisplay => converter número')
            self._converterNumeroNegativo() # inverter para número negativo
            
        if botao_texto == '=':
            print('método _insertButtonTextToDisplay => "="')
            self._igualClicked() # calcular equação

        if botao_texto in '+-/*^':
            print('método _insertButtonTextToDisplay => +=/*')
            self._operatorClicked(botao_texto) # inserir operador na equação
        
        # concatena str "." no display na variável "novo_valor_display"
        novo_valor_display = self.display.text() + botao_texto 

        # se for número 
        if _valorNumerico(novo_valor_display): # função "_valorNumerico" é do (módulo "uteis")
            print('método _insertButtonTextToDisplay =>', novo_valor_display)
            print('self.contador_auxiliar = 0')
            self.contador_auxiliar = 1 # nega uso de sinal negativo
            self.display.insert(botao_texto) # concatenar elementos no display (lista)

        self.display.setFocus() # manter cursor no display apos execução de algum método   

    # # Click em "C" (método _insertButtonTextToDisplay)
    def _clear(self):
            print('método _clear => Limpar display')
            print('self.contador_auxiliar = 0')
            self.contador_auxiliar = 0 # permite uso de sinal negativo no display
            self._num_esquerda = None # condições inicial
            self._num_direita = None # condições inicial
            self._operador = None # condições inicial
            self.equation = self._equationInitialValue # condições inicial
            self.display.clear() # limpar display


    # Click em operadores matemático '+-/*' (método _insertButtonTextToDisplay)
    def _operatorClicked(self, botao_texto):
        display_texto = self.display.text()  # informação no display
        
        print('método _operatorClicked =>', display_texto, '(display)')
        
        # ================ método auxiliar logica de número negativo ================  
        self._numeroNegativo(botao_texto)
        # ===========================================================================
                   
        # Se JÁ houver número a esquerda e operador, altera operador no informacao_display
        if not self._operador is None: # se operador não estiver vazio
            self._operador = botao_texto # altera operador
            
            # transformar em número inteiro se possível
            novo_valor_num_esquerda = _valorInteiro(self._num_esquerda)

            # altear (EQUAÇÃO)
            self.equation = f'{novo_valor_num_esquerda} {self._operador}' 
            print(f'método _operatorClicked => operador alterado para "{self._operador}"')
            return self._equation # atualizar informacao_display e finaliza função

        # Se NÃO houver número a esquerda, não faz nada, não será adicionado operador.
        if not _valorNumerico(display_texto): # se display sem número
            print('método _operatorClicked => Display vazio...')
            return # finaliza função

        # Se NÃO houver algum número no (informacao_display), adicionar número a esquerda.
        if self._num_esquerda is None: # se numero a esquerda for vazio 
            self._num_esquerda = float(display_texto) # adicionar valor do display
            
        self._operador = botao_texto # valor do operador

        # transformar em número inteiro se possível
        novo_valor_num_esquerda = _valorInteiro(self._num_esquerda)
        # adicionar (EQUAÇÃO)
        self.equation = f'{novo_valor_num_esquerda} {self._operador}' 


    # Click em sinal de igual "=" (método _insertButtonTextToDisplay)
    def _igualClicked(self):
        display_texto = self.display.text() # informação no display

        # se display estiver vazio
        if not _valorNumerico(display_texto): 
            print('método igualClicked => Display vazio...')
            self._showInfo('Display esta vazio.')
            return # finaliza função

        # se operador estiver vazio
        if self._operador is None:
            print('método igualClicked => Informação display vazio...')
            self._showInfo('Falta definir operador.')
            return # finaliza função
        
        self._num_direita = float(display_texto) # valor do _num_direita

        # transformar em número inteiro se possível
        novo_valor_num_esquerda = _valorInteiro(self._num_esquerda)
        novo_valor_num_direita = _valorInteiro(self._num_direita)

        # exibir somente para "self._num_direita" com valor (positivo) 
        self.equation = f'{novo_valor_num_esquerda} {self._operador} {novo_valor_num_direita}' 
        # exibir somente para "self._num_direita" com valor (negativo) 
        equation_auxiliar = f'{novo_valor_num_esquerda} {self._operador} ({novo_valor_num_direita})'      

        # calcular
        try:
            if self._operador == '^':
                 # calcular equação potência "^"
                 resultado = math.pow(float(self._num_esquerda), float(self._num_direita)) 
            else:
                # calcular equação simples "+-/*"
                resultado = eval(self.equation) 
            '''
            A função eval() em Python é uma função embutida que avalia uma expressão 
            escrita como uma string e retorna o valor da expressão, exemplo:

            # eval("1 + 2 * 3")
            # eval("if x > 0: return x else return -x")
            # eval("x and y")
            # eval("abs(-10)")
            '''
        except ZeroDivisionError:
            print('Erro divisão por zero')
            # self.display.clear() # limpar display
            # self.display.setText('Erro divisão por zero') # mensagem de erro p/ usuário (display)
            self._showError('Erro, divisão por zero.')
        except OverflowError:
            print('Número muito grande')
            self._showError('Número muito grande para calcular.')
        else:
            self.display.clear() # limpar display
            novo_resultado = _valorInteiro(resultado) # converte valor em inteiro se puder

            if '-' in str(self._num_direita):
                # exibir calculo na informacao_display se "_num_direita" for (negativo)
                self.informacao_display.setText(f'{equation_auxiliar} = {novo_resultado}')  
            else:
                # exibir calculo na informacao_display se "_num_direita" for (positivo)
                self.informacao_display.setText(f'{self.equation} = {novo_resultado}') 

            self.display.setText(str(novo_resultado)) # inserir "novo_resultado" no display

            # zerar valores em:
            self._num_esquerda = None 
            self._num_direita = None 
            self._operador = None

    # método de inserção de texto no display (exclusivo pelo teclado)
    def _recebimento_sinal_do_teclado(self, botao_texto):

        print(f'_recebimento_sinal_do_teclado => {botao_texto}')

        # concatena str "." no display na variável "novo_valor_display"
        novo_valor_display = self.display.text() + botao_texto

        # se valor for numérico
        if _valorNumerico(novo_valor_display):  
            self.contador_auxiliar = 1 # nega uso de sinal negativo
            self.display.insert(botao_texto) # concatenar elementos no display (insert => lista)
        
        # operador
        if botao_texto in '+-/*^':
            self._operatorClicked(botao_texto)

    # método auxiliar logica de número negativo (método _operatorClicked)
    def _numeroNegativo(self, botao_texto):
        if self._equation != 'Sua conta':
            print('self.contador_auxiliar = 1')
            self.contador_auxiliar = 1 # nega uso de sinal negativo

        if botao_texto == '-' and self.contador_auxiliar == 0:
            print('self.contador_auxiliar = 1')
            self.contador_auxiliar = 1 # nega uso de sinal negativo
            self.display.insert(botao_texto) # concatenar elementos no display (insert => lista)
        else:
            print('self.contador_auxiliar = 0')
            self.contador_auxiliar = 0 # permite uso de sinal negativo
            self.display.clear()  # Limpa o display

    # método auxiliar converter display número negativo 
    def _converterNumeroNegativo(self):

        display_texto = self.display.text() # informação no display

        # Se NÃO houver número a esquerda, não faz nada, não será adicionado operador.
        if not _valorNumerico(display_texto): # se display sem número
            print(' _converterNumeroNegativo => Display vazio...')
            return # finaliza função

        numero = float(display_texto) * -1 # número negativo 
        novo_numero = _valorInteiro(numero) # converter para inteiro se possível

        self.display.setText(novo_numero) # inserir "numero" no display
        # self.display.insert(novo_numero) # concatenar elementos no display (insert => lista)
   
    # ================= Caixa de diálogo =================
    def _showError(self, text):
        msgBox = self.window.makeMsgBox() # (módulo "main_window")
        msgBox.setText(text) # exibi texto na caixa de diálogo
        msgBox.setWindowTitle("Erro") # define o título da caixa de diálogo.
        msgBox.setButtonText(1, "Fechar") # renomear os botões padrão da caixa de diálogo
        msgBox.setInformativeText("Digite valor diferente de zero") # adiciona mensagem na caixa de diálogo
        msgBox.setIcon(msgBox.Icon.Critical) # exibi ícone na caixa de diálogo
        msgBox.exec() # executa a caixa de diálogo

    def _showInfo(self, text):
        msgBox = self.window.makeMsgBox() # (módulo "main_window")
        msgBox.setText(text) # exibi texto na caixa de diálogo
        msgBox.setIcon(msgBox.Icon.Information) # define o ícone da caixa de diálogo.
        msgBox.setWindowTitle("Informação") # define o título da caixa de diálogo.
        msgBox.setButtonText(1, "Fechar") # renomear os botões padrão da caixa de diálogo
        msgBox.exec() # executa a caixa de diálogo

    '''
    A biblioteca QMessageBox() é uma classe do Qt que fornece uma maneira conveniente de 
    exibir caixas de diálogo de mensagem. Essas caixas de diálogo podem ser usadas para 
    exibir mensagens de informação, aviso ou erro, ou para solicitar uma resposta do usuário.

    O parâmetro parent especifica o widget pai da caixa de diálogo. O parâmetro flags 
    especifica as flags da janela da caixa de diálogo.

    Depois de criar uma caixa de diálogo de mensagem, 
    você pode configurar suas propriedades usando os seguintes métodos:

    # setIcon(): define o ícone da caixa de diálogo.
    # setText(): define o texto da caixa de diálogo.
    # setInformativeText(): adicionar texto da caixa de diálogo.
    # setWindowTitle(): define o título da caixa de diálogo.
    # setStandarButtons(): definir os botões padrão que serão exibidos em uma caixa de mensagem
    # setButtonText(): # renomear os botões padrão da caixa de diálogo

    Os botões padrão disponíveis são:

    # QMessageBox.Ok: Botão "OK"
    # QMessageBox.Cancel: Botão "Cancelar"
    # QMessageBox.Yes: Botão "Sim"
    # QMessageBox.No: Botão "Não"
    # QMessageBox.Abort: Botão "Cancelar"
    # QMessageBox.Retry: Botão "Tentar novamente"
    # QMessageBox.Ignore: Botão "Ignorar"
    # QMessageBox.YesAll: Botão "Sim para todos"
    # QMessageBox.NoAll: Botão "Não para todos"
    # QMessageBox.Close: Botão "Fechar"

    Exemplo:
    def _showVazio(self, text):
        msgBox = self.window.makeMsgBox() # (módulo "main_window")
        msgBox.setText(text) # exibi texto na caixa de diálogo
        msgBox.setIcon(msgBox.Icon.Warning) # define o ícone da caixa de diálogo.
        msgBox.setWindowTitle("Vazio") # define o título da caixa de diálogo.
        msgBox.setStandardButtons(msgBox.StandardButton.Ok | msgBox.StandardButton.Cancel) # define os botões padrão da caixa de diálogo.
        msgBox.setButtonText(msgBox.StandardButton.Ok, "Abrir") # renomear os botões padrão da caixa de diálogo
        msgBox.setButtonText(msgBox.StandardButton.Cancel, "Fechar") # renomear os botões padrão da caixa de diálogo
        result = msgBox.exec() # executa a caixa de diálogo

        if result == msgBox.StandardButton.Ok:
            print('Caixa de diálogo = Abrir')
        elif result == msgBox.StandardButton.Cancel:
            print('Caixa de diálogo = Fechar')
    '''  
    # ======================================================