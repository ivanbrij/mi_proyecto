class Organizador_Materias():
 
    def __init__(self):
        self.lista_materias = []
        self.lista_materias.append({"Nombre":"Introducción a la programación", "Semestre":"2019-1", "Profesor":"Antonio Andrade", "Nota":4.5})
        self.lista_materias.append({"Nombre":"Estructuras de datos", "Semestre":"2019-2", "Profesor":"Hamid Abdallah", "Nota":3.5})
        self.lista_materias.append({"Nombre":"Desarrollo de software", "Semestre":"2020-1", "Profesor":"Rubby Casallas", "Nota":2.0})
        self.lista_materias.append({"Nombre":"Arquitectura de software", "Semestre":"2020-2", "Profesor":"Xiao Lihua", "Nota":4.0})
        self.actual = 0

    def dar_materia_actual(self):
        return self.lista_materias[self.actual]

    def avanzar(self):
        self.actual += 1
        self.actual = self.actual % len(self.lista_materias)

    def retroceder(self):
        self.actual -= 1
        self.actual = self.actual % len(self.lista_materias)

    def aniadir_materia(self, nueva_materia):
        self.lista_materias.append(nueva_materia)