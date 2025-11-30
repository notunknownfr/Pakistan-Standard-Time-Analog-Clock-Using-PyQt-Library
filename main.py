import sys
import welcome
from PyQt5.QtWidgets import QApplication

def main():
    app=QApplication(sys.argv)

    mainWindow=welcome.MainWindow()
    timezoneSetup=welcome.TimeZoneSelectionScreen(mainWindow)

   
    sys.exit(app.exec_())

if __name__== "__main__":
    main()