# QSS - Estilos do QT for Python
# https://doc.qt.io/qtforpython/tutorials/basictutorial/widgetstyling.html
# Dark Theme
# https://pyqtdarktheme.readthedocs.io/en/latest/how_to_use.html
# qt-material
# https://pypi.org/project/qt-material/
# qdarktheme
# https://pypi.org/project/pyqtdarktheme/

from qt_material import apply_stylesheet

# from variaveis import (DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR,
#                        PRIMARY_COLOR)

def cor_escuro(widget):
    apply_stylesheet(widget, theme='dark_teal.xml')

def cor_vermelho(widget):
    apply_stylesheet(widget, theme='light_red.xml')


