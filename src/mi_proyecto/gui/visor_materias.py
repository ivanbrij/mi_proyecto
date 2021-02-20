from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QGroupBox, QGridLayout, QLabel, QLineEdit, QVBoxLayout
from .dialogo_nueva_materia import Dialogo_nueva_materia

class Aplicacion_Gui(QWidget):

    def __init__(self, logica):
        super().__init__()

        #Se establecen las características de la ventana
        self.title = 'Mi aplicación'
        self.left = 80
        self.top = 80
        self.width = 300
        self.height = 320
        #Inicializamos la ventana principal
        self.inicializar_GUI()
        #Asignamos el valor de la lógica
        self.logica = logica
        self.actualizar_materia()
    
    def actualizar_materia(self):
        actual = self.logica.dar_materia_actual()
        self.txt_nombre.setText(actual["Nombre"])
        self.txt_semestre.setText(actual["Semestre"])
        self.txt_profesor.setText(actual["Profesor"])
        self.txt_nota.setText(str(actual["Nota"]))
      
    def avanzar_materia(self):
        self.logica.avanzar()
        self.actualizar_materia()
    
    def retroceder_materia(self):
        self.logica.retroceder()
        self.actualizar_materia()
      
    def inicializar_GUI(self):
        #inicializamos la ventana
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        #Creamos el distribuidor gráfico principal
        self.distr_vertical = QVBoxLayout()

        #Creamos la caja de materias
        self.caja_materias = QGroupBox("Materia")
        distr_caja_materias = QGridLayout()
        self.caja_materias.setLayout(distr_caja_materias)

        #Creamos las etiquetas y campos de texto de la materia la caja de materias
        self.etiqueta_nombre = QLabel('Nombre')
        self.txt_nombre = QLineEdit()
        self.txt_nombre.setReadOnly(True)

        self.etiqueta_semestre = QLabel('Semestre')
        self.txt_semestre = QLineEdit()

        self.etiqueta_profesor = QLabel('Profesor')
        self.txt_profesor = QLineEdit()

        self.etiqueta_nota = QLabel('Nota')
        self.txt_nota = QLineEdit()

        #Agregamos a la caja de materias las etiquetas
        distr_caja_materias.addWidget(self.etiqueta_nombre, 0,0)
        distr_caja_materias.addWidget(self.etiqueta_semestre, 1,0)
        distr_caja_materias.addWidget(self.etiqueta_profesor, 2,0)
        distr_caja_materias.addWidget(self.etiqueta_nota, 3,0)

        #Agregamos a la caja de materias los campos de texto
        distr_caja_materias.addWidget(self.txt_nombre, 0,1)
        distr_caja_materias.addWidget(self.txt_semestre, 1,1)
        distr_caja_materias.addWidget(self.txt_profesor, 2,1)
        distr_caja_materias.addWidget(self.txt_nota, 3,1)

        #Creamos la caja de botones
        self.caja_botones = QGroupBox()
        distr_caja_botones = QHBoxLayout()
        self.caja_botones.setLayout(distr_caja_botones)
        self.caja_botones.setFixedHeight(50)
        
        #Creamos los botones para la caja de botones
        self.boton_retroceder = QPushButton("<<")
        self.boton_retroceder.clicked.connect(self.retroceder_materia)
        self.boton_avanzar = QPushButton(">>")
        self.boton_avanzar.clicked.connect(self.avanzar_materia)
        self.boton_nueva_materia = QPushButton("Nueva Materia")
        self.boton_nueva_materia.clicked.connect(self.dialogo_nueva_materia)

        #Agregamos los botones a la caja de botones
        distr_caja_botones.addWidget(self.boton_retroceder)
        distr_caja_botones.addWidget(self.boton_avanzar)
        distr_caja_botones.addWidget(self.boton_nueva_materia)


        #Agregamos las cajas a nuestra aplicación
        self.distr_vertical.addWidget(self.caja_materias)
        self.distr_vertical.addWidget(self.caja_botones)
        
        #Definimos el distribuidor principal de la ventana             
        self.setLayout(self.distr_vertical)

        #Hacemos la ventana visible
        self.show()

    def dialogo_nueva_materia(self):
        dialogo = Dialogo_nueva_materia()     
        if dialogo.exec_():
            self.logica.aniadir_materia(dialogo.dar_valores())