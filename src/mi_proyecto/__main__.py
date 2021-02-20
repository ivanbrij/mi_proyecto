import sys
from logica.organizador_materias import Organizador_Materias
from gui.visor_materias import Aplicacion_Gui
from PyQt5.QtWidgets import QApplication


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.logica = Organizador_Materias()
        self.gui = Aplicacion_Gui(self.logica)


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())