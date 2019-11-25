from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import Qt, QPoint
from PyQt5.Qt import QPixmap, QImage, QColor, QPainter, QBrush
from PyQt5 import uic
import sys
import random


class RunningButton(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ui.ui", self)
        self.image = QImage(399, 270, QImage.Format_RGB32)
        self.image.fill(QColor(255, 255, 255))
        self.image_out.setPixmap(QPixmap.fromImage(self.image))
        self.draw.clicked.connect(self.draw_circle)

    def draw_circle(self):
        painter = QPainter(self.image)
        painter.setBrush(QBrush(QColor(255, 255, 0)))
        size = random.randint(0, 30)
        point_x = random.randint(0, 399)
        point_y = random.randint(0, 270)
        painter.drawEllipse(QPoint(point_x, point_y), size, size)
        painter.end()
        self.image_out.setPixmap(QPixmap.fromImage(self.image))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RunningButton()
    window.show()
    app.exec()