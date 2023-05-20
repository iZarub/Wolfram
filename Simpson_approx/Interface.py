from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import pyqtgraph 
from pyqtgraph import PlotWidget, plot
import matplotlib.pyplot as plt

import WolframApi

import wolframparser

from Calculation import (real_dependence,
                         Simpson_dependence)


from TestApi import get_integral





class Window(QWidget):
    def __init__(self, parent = None):
        super(Window, self).__init__(parent)
        self.resize(600, 800)
        self.setWindowTitle("Simpson")
        self.setMinimumSize(QSize(600, 800))
        self.setMaximumSize(QSize(600, 800))
        self.setObjectName("main")
        with open('Simpson_approx/stylesheet.qss', 'r', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

      
        self.parser = wolframparser.Parser()
        self.set_buttons()
        self.set_input()
        self.set_label()

        self.start.clicked.connect(self.set_graph)

    def set_buttons(self):
        self.start = QPushButton(parent=self)
        self.start.setGeometry(QRect(30, 190, 211, 41))
        self.start.setText("Evaluate")
        self.start.setObjectName("start")


    def set_input(self):
        self.lineEdit = QLineEdit(parent=self)
        self.lineEdit.setGeometry(QRect(30, 30, 520, 70))
        self.lineEdit.setPlaceholderText("Type f(x)...")
        font = QFont()
        font.setFamily("Helvetica")
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("chatenter")

        self.lineEdit1 = QLineEdit(parent=self)
        self.lineEdit1.setGeometry(QRect(30, 110, 420, 30))
        self.lineEdit1.setPlaceholderText("Type left lim...")
        font = QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.lineEdit1.setFont(font)
        self.lineEdit1.setObjectName("chatenter1")

        self.lineEdit2 = QLineEdit(parent=self)
        self.lineEdit2.setGeometry(QRect(30, 150, 420, 30))
        self.lineEdit2.setPlaceholderText("Type right lim...")
        font = QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.lineEdit2.setFont(font)
        self.lineEdit2.setObjectName("chatenter1")

    def set_label(self):
        self.visual = QLabel(parent = self)
        self.visual.setGeometry(QRect(0, 220, 650, 500))
        pixmap = QPixmap('C:/Users/adozz/Documents/Wolfram/real.png')
        self.visual.setPixmap(pixmap)
        self.visual.hide()
        
    def set_graph(self):
        if (self.lineEdit.text() and self.lineEdit1.text() and self.lineEdit2.text()) != '':
            input = self.lineEdit.text()
            llim = self.lineEdit1.text()
            rlim = self.lineEdit2.text()

            input_for_calculations = self.parser.convert_to_python_expression(input + "*Cos(k*x)")
            input_for_wolfram = self.parser.convert_to_wolfram_expression(input)

            simpson_y, ks = Simpson_dependence(input_for_calculations, llim, rlim)
            plt.figure()
            plt.plot(ks, simpson_y, label = "Simpson approximation")

            
            integral = get_integral(input_for_wolfram, llim, rlim)
            if integral[0]:
                output_python_expr = self.parser.convert_to_python_expression(integral[1])
                real_y, ks = real_dependence(output_python_expr)
                plt.plot(ks, real_y, label = "Real Wolfram Integration")
                plt.grid()
                plt.legend()
                plt.savefig("real.png")

                pixmap = QPixmap('C:/Users/adozz/Documents/Wolfram/real.png')
                self.visual.setPixmap(pixmap)
                self.visual.show()
            else:
                print(integral[1])


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = Window()
    MainWindow.show()
    sys.exit(app.exec())