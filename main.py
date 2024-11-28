from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPainter, QColor
import io
from PyQt6 import uic
from ui_file import Ui_Dialog
import sys
from random import randrange


class second(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.A = QLabel(self)
        self.do_paint = False
        self.A.move(200, 0)
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        f = randrange(200, 500)
        f1 = randrange(0, 200)
        f2 = randrange(0, 100)

        r = randrange(0, 255)
        g = randrange(0, 255)
        b = randrange(0, 255)
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(f, f1, f2, f2)



if __name__ == '__main__':
    App = QApplication(sys.argv)
    ex = second()
    ex.show()
    sys.exit(App.exec())