import sys
from PyQt5.QtWidgets import QApplication
import window
import analog_clock

def main():
    app=QApplication(sys.argv)
    win=window.MainWindow()

    win.show()

    sys.exit(app.exec_())

if __name__== "__main__":
    main()