import sys
from window import MainWindow
import pytz
from PyQt5.QtWidgets import QWidget, QComboBox, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class TimeZoneSelectionScreen:
    
    def __init__(self,main_window:MainWindow):
        self.mw=main_window
        self.container= QWidget()
        self.container.setGeometry(0,0,1920,1000)
        

        layout=QVBoxLayout()
        
        

        #WELCOME LABEL SETTING
        welcomeLabel= QLabel("Welcome") 
        welcomeLabel.setStyleSheet("color:blue;" "background-color: yellow")       
        welcomeLabel.setFont(QFont("Arial", 70))
        welcomeLabel.setAlignment(Qt.AlignCenter)
        welcomeLabel.setFixedSize(700,200)




        #COMBO SETTING
        self.combo= QComboBox()
        self.combo.setFixedSize(350,150)
        self.combo.addItems(pytz.all_timezones)
        self.combo.setFont(QFont("Arial",20))
        self.combo.setEditable(True)              
        self.combo.lineEdit().setAlignment(Qt.AlignCenter)  
        self.combo.lineEdit().setReadOnly(True)

        #GO BUTTON SETTING
        goButton=QPushButton("GO")
        goButton.setFixedSize(200,150)
        goButton.setFont(QFont("Arial",30))
        goButton.clicked.connect(self.callMainWindow)

        layout.addSpacing(30)
        layout.addWidget(welcomeLabel, alignment=Qt.AlignHCenter)
        layout.addSpacing(50)
        layout.addWidget(self.combo,alignment=Qt.AlignHCenter)
        layout.addSpacing(50)
        layout.addWidget(goButton, alignment=Qt.AlignHCenter)

        layout.addStretch()

        self.container.setLayout(layout)

        self.container.show()

    
    def callMainWindow(self):

        self.container.hide()

        tz = self.combo.currentText()
        self.mw.selected_tz=tz
        self.mw.clock.drawClock(self.mw.selected_tz)
        self.mw.show()
