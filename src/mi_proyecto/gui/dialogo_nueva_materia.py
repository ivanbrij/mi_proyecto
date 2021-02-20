from PyQt5.QtWidgets import * #QDialog, QVBoxLayout, QDialogButtonBox, QGridLayout

class Dialogo_nueva_materia(QDialog):

    def __init__(self, *args, **kwargs):
        super(Dialogo_nueva_materia, self).__init__(*args, **kwargs)
        self.setWindowTitle("Agregar nueva materia")

        #Creamos el distribuidor gráfico del diálogo
        self.distribuidor = QVBoxLayout()     

        #Creamos la caja de botones para Save y Cancel
        Q_Botones = QDialogButtonBox.Save | QDialogButtonBox.Cancel
        self.caja_botones = QDialogButtonBox(Q_Botones)
        
        #Conectamos las señales de los botones con las funciones del diálogo
        self.caja_botones.accepted.connect(self.accept)
        self.caja_botones.rejected.connect(self.reject)

        #Inicializamos y añadimos los otros componentes del diálogo
        self.inicializar_dialogo()

        #Añadimos al distribuidor la caja de botones
        self.distribuidor.addWidget(self.caja_botones)

        #Añadimos el distribuidor al diálogo
        self.setLayout(self.distribuidor)   

    def inicializar_dialogo(self):
        
        caja_campos =  QGroupBox("Ingrese los datos")
        distr_campos = QGridLayout()

        self.etiqueta_nombre = QLabel("Nombre")
        self.txt_nombre = QLineEdit()
        self.etiqueta_semestre = QLabel("Semestre")
        self.txt_semestre = QComboBox()
        self.txt_semestre.addItems(["2019-1","2019-2","2020-1"])
        self.etiqueta_profesor = QLabel("Profesor")
        self.txt_profesor = QLineEdit()
        self.etiqueta_nota = QLabel("Nota")
        self.txt_nota = QLineEdit()

        distr_campos.addWidget(self.etiqueta_nombre, 0,0)
        distr_campos.addWidget(self.txt_nombre, 0,1)
        distr_campos.addWidget(self.etiqueta_semestre, 1,0)
        distr_campos.addWidget(self.txt_semestre, 1,1)
        distr_campos.addWidget(self.etiqueta_profesor, 2,0)
        distr_campos.addWidget(self.txt_profesor, 2,1)
        distr_campos.addWidget(self.etiqueta_nota, 3,0)
        distr_campos.addWidget(self.txt_nota, 3,1)

        caja_campos.setLayout(distr_campos)
        self.distribuidor.addWidget(caja_campos)

    def dar_valores(self):
        return {"Nombre":self.txt_nombre.text(), "Semestre": self.txt_semestre.currentText(), "Profesor":self.txt_profesor.text(), "Nota":float(self.txt_nota.text())}

    def accept(self):
        dialogo_confirmacion = QMessageBox()
        dialogo_confirmacion.setIcon(QMessageBox.Question)
        dialogo_confirmacion.setText("¿Está seguro que desea guardar los datos como una nueva materia?")
        dialogo_confirmacion.setWindowTitle("Confirmación")
        dialogo_confirmacion.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        if self.verificar_valores() and dialogo_confirmacion.exec_() == QMessageBox.Yes:
                super().accept()
        else:
                super().reject()

    def verificar_valores(self):
        if self.txt_nombre.text() == "" or self.txt_profesor.text()=="" or self.txt_nota.text()=="":
            dialogo_error = QMessageBox()
            dialogo_error.setIcon(QMessageBox.Critical)
            dialogo_error.setText("Los campos de la nueva materia no pueden estar vacíos")
            dialogo_error.setWindowTitle("Error")
            dialogo_error.setStandardButtons(QMessageBox.Ok)
            dialogo_error.exec_()
            return False
        return True