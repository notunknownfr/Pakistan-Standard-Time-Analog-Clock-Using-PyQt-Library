from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtCore import Qt
import datetime 

class Clock:
    def __init__(self,window):
        self.window=window
        self.hours=0
        self.mins=0
        self.seconds=0

        self.label= QLabel("",self.window)
        self.label.setGeometry((self.window.width()//2)-500,(self.window.height()//2)-200,1000,1000)

        self.pixmap = QPixmap("clock.jpg")
        self.pixmap = self.pixmap.scaled(1060, 1000) 
        self.label.setPixmap(self.pixmap)
        self.label.setAlignment(Qt.AlignCenter)
        
    def drawClock(self,tz=None):
        import pytz
    
        now = datetime.datetime.now(pytz.timezone(tz))

        self.hour= (now.hour % 12) -3
        self.mins=now.minute- 15
        self.seconds=now.second- 15

        pix = self.pixmap.copy()
        painter= QPainter(pix)
        painter.setRenderHint(QPainter.Antialiasing)

        x_cor, y_cor= 545,505

        painter.setPen(QPen(Qt.blue, 10))
        painter.drawLine(x_cor,y_cor, int(x_cor+ 200 * self.cos_calculate(-(30*self.hour+ self.mins/2))),  int(y_cor - 200* self.sin_calculate(-(30*self.hour + self.mins/2))))

        painter.setPen(QPen(Qt.black, 4))
        painter.drawLine(x_cor, y_cor, int(x_cor + 270 * self.cos_calculate(-(6*self.mins))), int(y_cor - 270 * self.sin_calculate(-(6*self.mins))))

        painter.setPen(QPen(Qt.red, 2))
        painter.drawLine(x_cor, y_cor, int(x_cor + 350 * self.cos_calculate(-(6*self.seconds))),int(y_cor - 350 * self.sin_calculate(-(6*self.seconds))))

        painter.end()
        self.label.setPixmap(pix)
       


    def cos_calculate(self,degree):
        import math
        return math.cos(math.radians(degree))

    def sin_calculate(self,degree):
        import math
        return math.sin(math.radians(degree))