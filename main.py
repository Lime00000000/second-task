from PyQt6.QtWidgets import QApplication, QDialog, QLabel
from PyQt6.QtGui import QPainter, QColor
import io
from PyQt6 import uic
import sys
from random import randrange


template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1120</width>
    <height>493</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <widget class="QPushButton" name="pushButton">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>210</y>
     <width>121</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>Заспавни
круг</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

class second(QDialog):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
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

        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(f, f1, f2, f2)



if __name__ == '__main__':
    App = QApplication(sys.argv)
    ex = second()
    ex.show()
    sys.exit(App.exec())