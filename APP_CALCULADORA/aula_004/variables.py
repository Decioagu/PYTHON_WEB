from pathlib import Path

# caminho
ROOT_DIR = Path(__file__).parent
WINDOW_ICON_PATH = ROOT_DIR / 'icon.png'

# Sizing (tamanhos)
'''
    Em Python, o termo "Sizing" é usado para se referir a um conjunto de técnicas 
    que permitem controlar o tamanho de um objeto. Essas técnicas podem ser usadas 
    para especificar o tamanho de um objeto explicitamente ou para permitir que 
    o objeto se ajuste automaticamente ao seu conteúdo.
'''
BIG_FONT_SIZE = 40 # tamanho da fonte
MEDIUM_FONT_SIZE = 25 # tamanho da fonte
SMALL_FONT_SIZE = 15 # tamanho da fonte
TEXT_MARGIN = 15 # margem do texto
MINIMUM_WIDTH = 500 # largura da janela