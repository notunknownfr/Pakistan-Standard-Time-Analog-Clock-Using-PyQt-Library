from analog_clock import Clock
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.clock=Clock(self)

        self.setWindowTitle("Clock App")
        self.setWindowIcon(QIcon("icon.jpeg"))
        self.setGeometry(0,0,1700,1050)
        
        self.label=QLabel("PAKISTAN STANDARD TIME",self)
        self.label.setGeometry((self.width()//2)-(700//2),0,700,50)
        self.label.setFont(QFont("Arial", 30))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color:blue;" "background-color: red")
        self.clock.label.move((self.width()//2)- self.clock.label.width()//2,(self.height()//2)- self.clock.label.height()//2)

        self.timer = QTimer()
        self.timer.timeout.connect(self.clock.drawClock)
        self.timer.start(1000) 

if __name__== "__main__":
    app=QApplication(sys.argv)
    window=MainWindow()

    window.show()

    sys.exit(app.exec_())