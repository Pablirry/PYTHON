from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel, QTextEdit, QInputDialog
from utils.functions import (
    sms_revival,
    texto_a_morse,
    limpia_notas,
    emula_sum,
    dias_del_mes,
    enlista,
    cita_con_estilo
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python UI Project")
        self.setGeometry(100, 100, 600, 400)
        
        self.layout = QVBoxLayout()
        
        self.label = QLabel("Selecciona una opción:")
        self.layout.addWidget(self.label)
        
        self.buttons = []
        self.create_button("Ejercicio 1 (sms_revival)", self.sms_revival)
        self.create_button("Ejercicio 2 (texto_a_morse)", self.texto_a_morse)
        self.create_button("Ejercicio 3 (limpia_notas)", self.limpia_notas)
        self.create_button("Ejercicio 4 (emula_sum)", self.emula_sum)
        self.create_button("Ejercicio 5 (dias_del_mes)", self.dias_del_mes)
        self.create_button("Ejercicio 6 (enlista)", self.enlista)
        self.create_button("Ejercicio 7 (cita_con_estilo)", self.cita_con_estilo)
        
        self.result = QTextEdit()
        self.result.setReadOnly(True)
        self.layout.addWidget(self.result)
        
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
    
    def create_button(self, text, method):
        button = QPushButton(text)
        button.clicked.connect(method)
        self.layout.addWidget(button)
        self.buttons.append(button)
    
    def sms_revival(self):
        cadena, ok = self.get_input("Introduce una cadena:")
        if ok:
            self.result.setText(sms_revival(cadena))
    
    def texto_a_morse(self):
        cadena, ok = self.get_input("Introduce una cadena:")
        if ok:
            self.result.setText(texto_a_morse(cadena))
    
    def limpia_notas(self):
        notas, ok = self.get_input("Introduce una lista de notas separadas por comas:")
        if ok:
            notas_list = list(map(float, notas.split(',')))
            self.result.setText(str(limpia_notas(notas_list)))
    
    def emula_sum(self):
        lista, ok = self.get_input("Introduce una lista de números separados por comas:")
        if ok:
            lista_nums = list(map(float, lista.split(',')))
            self.result.setText(str(emula_sum(lista_nums)))
    
    def dias_del_mes(self):
        mes, ok = self.get_input("Introduce un mes:")
        if ok:
            self.result.setText(str(dias_del_mes(mes)))
    
    def enlista(self):
        cadena, ok = self.get_input("Introduce una cadena de números separados por '/':")
        if ok:
            self.result.setText(str(enlista(cadena)))
    
    def cita_con_estilo(self):
        tu, ok1 = self.get_input("Introduce tu estilo (0-10):")
        cita, ok2 = self.get_input("Introduce el estilo de tu cita (0-10):")
        if ok1 and ok2:
            self.result.setText(str(cita_con_estilo(int(tu), int(cita))))
    
    def get_input(self, prompt):
        text, ok = QInputDialog.getText(self, 'Input Dialog', prompt)
        return text, ok