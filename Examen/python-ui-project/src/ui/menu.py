from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QTextEdit, QInputDialog, QTabWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
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
        self.setGeometry(100, 100, 800, 600)
        
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        
        self.create_tab("Ejercicio 1 (sms_revival)", self.sms_revival)
        self.create_tab("Ejercicio 2 (texto_a_morse)", self.texto_a_morse)
        self.create_tab("Ejercicio 3 (limpia_notas)", self.limpia_notas)
        self.create_tab("Ejercicio 4 (emula_sum)", self.emula_sum)
        self.create_tab("Ejercicio 5 (dias_del_mes)", self.dias_del_mes)
        self.create_tab("Ejercicio 6 (enlista)", self.enlista)
        self.create_tab("Ejercicio 7 (cita_con_estilo)", self.cita_con_estilo)
    
    def create_tab(self, title, method):
        tab = QWidget()
        layout = QVBoxLayout()
        
        label = QLabel(title)
        label.setFont(QFont('Arial', 16))
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        
        button = QPushButton("Ejecutar")
        button.setFont(QFont('Arial', 12))
        button.clicked.connect(lambda: self.execute_method(method, tab))
        layout.addWidget(button)
        
        result = QTextEdit()
        result.setReadOnly(True)
        result.setFont(QFont('Arial', 14))
        layout.addWidget(result)
        
        tab.setLayout(layout)
        tab.result = result
        self.tabs.addTab(tab, title)
    
    def execute_method(self, method, tab):
        method(tab)
    
    def sms_revival(self, tab):
        cadena, ok = self.get_input("Introduce una cadena:")
        if ok:
            tab.result.setText(sms_revival(cadena))
    
    def texto_a_morse(self, tab):
        cadena, ok = self.get_input("Introduce una cadena:")
        if ok:
            tab.result.setText(texto_a_morse(cadena))
    
    def limpia_notas(self, tab):
        notas, ok = self.get_input("Introduce una lista de notas separadas por comas:")
        if ok:
            notas_list = list(map(float, notas.split(',')))
            tab.result.setText(str(limpia_notas(notas_list)))
    
    def emula_sum(self, tab):
        lista, ok = self.get_input("Introduce una lista de números separados por comas:")
        if ok:
            lista_nums = list(map(float, lista.split(',')))
            tab.result.setText(str(emula_sum(lista_nums)))
    
    def dias_del_mes(self, tab):
        mes, ok = self.get_input("Introduce un mes:")
        if ok:
            tab.result.setText(str(dias_del_mes(mes)))
    
    def enlista(self, tab):
        cadena, ok = self.get_input("Introduce una cadena de números separados por '/':")
        if ok:
            tab.result.setText(str(enlista(cadena)))
    
    def cita_con_estilo(self, tab):
        tu, ok1 = self.get_input("Introduce tu estilo (0-10):")
        cita, ok2 = self.get_input("Introduce el estilo de tu cita (0-10):")
        if ok1 and ok2:
            tab.result.setText(str(cita_con_estilo(int(tu), int(cita))))
    
    def get_input(self, prompt):
        text, ok = QInputDialog.getText(self, 'Input Dialog', prompt)
        return text, ok