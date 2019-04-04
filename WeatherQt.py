import sys
import time

from PyQt4 import QtCore,QtGui
from PyQt4.QtCore import SIGNAL
from WheatherNow import CityWeather
from PyQt4.QtGui import QApplication, QMainWindow,QFont

from weathergui import Ui_MainWindow

class MainWindow(QMainWindow ,Ui_MainWindow):
        def __init__(self, parent=None, *args, **kwargs):
            QMainWindow.__init__(self)
            self.setupUi(self)
            self.now=CityWeather()
            self.connect(self.pushButton,SIGNAL('clicked()'), self.show_answer)

        def show_answer(self):
            self.city=self.textEdit.toPlainText()
            time.sleep(1)
            self.textEdit_2.setText(str(self.now.output_weather(self.city)))

def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

main()
