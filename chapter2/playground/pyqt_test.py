import os
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas_datareader.data as web
import pandas as pd
from pandas import Series, DataFrame

# 라벨
def show_label():
    # pyqt : 이벤트 루프이해, app이 종료되면 "After event loop" 출력된다.
    app = QApplication(sys.argv)
    label = QLabel("Hello, PyQt")
    label.show()

    print("Before event loop")
    app.exec_()
    print("After event loop")


# 버튼 + 이벤트 연결
def show_button():
    # pyqt : 시그널
    def clicked_slot():
        print('clicked')

    app = QApplication(sys.argv)

    btn = QPushButton("Hello, PyQt")
    btn.clicked.connect(clicked_slot)
    btn.show()

    app.exec_()


# 클래스 이용 MainWindow 사용하기.
def show_window():
    # pyqt : 클래스 이용, 간단한 UI 만들기.
    class MyWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setupUI()

        def setupUI(self):
            self.setWindowTitle("Review")

            btn1 = QPushButton("Click me", self)
            btn1.move(20, 20)
            btn1.clicked.connect(self.btn_clicked)

        def btn_clicked(self):
            QMessageBox.about(self, "message", "clicked")

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()


def show_window_of_qtdesigner():
    root_path = os.path.abspath(__file__ + "/../..")  # root 경로 가져오기.
    form_class = uic.loadUiType(root_path + "/qt_test.ui")[0]  # qt_test.ui

    class MyWindow(QMainWindow, form_class): #상속
        def __init__(self):
            super().__init__()
            self.setupUi(self)

            # 상태바
            self.statusBar = QStatusBar(self)
            self.setStatusBar(self.statusBar)

            # 이벤트 연결하기.
            self.pushButton.clicked.connect(lambda: self.btnClicked())
            self.lineEdit.textChanged.connect(lambda: self.lineEditChanged())

            # 라디오 버튼 이용하기.
            self.radioButtonDay.setChecked(True)
            self.radioButtonDay.clicked.connect(lambda: self.radioBtnClicked())
            self.radioButtonWeek.clicked.connect(lambda: self.radioBtnClicked())
            self.radioButtonMonth.clicked.connect(lambda: self.radioBtnClicked())

            # 체크박스 이용하기
            self.checkBox5Line.setChecked(True)
            self.checkBox20Line.setChecked(True)
            self.checkBox60Line.setChecked(False)

            self.checkBox5Line.stateChanged.connect(lambda: self.checkBtnClicked())
            self.checkBox20Line.stateChanged.connect(lambda: self.checkBtnClicked())
            self.checkBox60Line.stateChanged.connect(lambda: self.checkBtnClicked())

            # QSpinBox 이용하기
            self.spinBoxBuy.valueChanged.connect(lambda: self.spinBoxValueChanged())
            self.spinBoxSell.valueChanged.connect(lambda: self.spinBoxValueChanged())

            # dialog 이용하기
            self.pushButtonOpenFile.clicked.connect(lambda: self.btnClickedOpenFileDialog())
            self.pushButtonInputDialog.clicked.connect(lambda: self.btnClickedInputDialog())
            self.pushButtonCustomDialog.clicked.connect(lambda: self.btnClickedCustomDialog())

        def btnClicked(self):
            value = self.lineEdit.text()
            self.label.setText(value)
            self.statusBar.showMessage("clicked button")

        def lineEditChanged(self):
            value = self.lineEdit.text()
            self.label.setText(value)
            self.statusBar.showMessage("input line edit")

        def radioBtnClicked(self):
            if self.radioButtonDay.isChecked():
                self.statusBar.showMessage("일봉 선택")
            elif self.radioButtonWeek.isChecked():
                self.statusBar.showMessage("주봉 선택")
            elif self.radioButtonMonth.isChecked():
                self.statusBar.showMessage("월봉 선택")

        def checkBtnClicked(self):
            if self.checkBox5Line.isChecked():
                pass
            elif self.checkBtn20Line.isChecked():
                pass
            elif self.checkBnt60Line.isChecked():
                pass

        def spinBoxValueChanged(self):
            valueBuy = self.spinBoxBuy.value()
            valueSell = self.spinBoxSell.value()
            self.statusBar.showMessage("매수:" + str(valueBuy) + ", 매도" + str(valueSell))
            pass

        def btnClickedOpenFileDialog(self):
            fname = QFileDialog.getOpenFileName(self)
            self.statusBar.showMessage(fname[0])

        def btnClickedInputDialog(self):
            text, ok = QInputDialog.getInt(self, '매수 수량', '매수 수량을 입력하세요.')
            if ok:
                self.statusBar.showMessage("매수:" + text)

        def btnClickedCustomDialog(self):
            show_pw_dialog_of_qtdesigner()


    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()


def show_layout_of_qtdesigner():
    root_path = os.path.abspath(__file__ + "/../..")  # root 경로 가져오기.
    form_class = uic.loadUiType(root_path + "/qt_layout_test.ui")[0]  # qt_test.ui

    class MyWindow(QTabWidget, form_class):
        def __init__(self):
            super().__init__()
            self.setupUi(self)

    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()


def show_pw_dialog_of_qtdesigner():
    root_path = os.path.abspath(__file__ + "/../..")  # root 경로 가져오기.
    form_class = uic.loadUiType(root_path + "/qt_pw_dialog_test.ui")[0]  # qt_test.ui

    class MyDialog(QDialog, form_class):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.id = None
            self.pw = None

            self.buttonBox.clicked.connect(lambda: self.btnClicked())

        def btnClicked(self):
            self.id = self.lineEditId.text()
            self.pw = self.lineEditPw.text()

    dlg = MyDialog()
    dlg.exec_()
    id = dlg.id
    password = dlg.password
    return id, password


def show_chart_of_qtdesigner():

    class MyWindow(QWidget):
        def __init__(self):
            super().__init__()
            self.setupUI()

        def setupUI(self):
            self.setGeometry(600, 200, 1200, 600)
            self.setWindowTitle("PyChart Viewer v0.1")
            self.setWindowIcon(QIcon('icon.png'))

            self.lineEdit = QLineEdit()
            self.pushButton = QPushButton("차트그리기")
            self.pushButton.clicked.connect(self.pushButtonClicked)

            self.fig = plt.Figure()
            self.canvas = FigureCanvas(self.fig)

            leftLayout = QVBoxLayout()
            leftLayout.addWidget(self.canvas)

            # Right Layout
            rightLayout = QVBoxLayout()
            rightLayout.addWidget(self.lineEdit)
            rightLayout.addWidget(self.pushButton)
            rightLayout.addStretch(1)

            layout = QHBoxLayout()
            layout.addLayout(leftLayout)
            layout.addLayout(rightLayout)
            layout.setStretchFactor(leftLayout, 1)
            layout.setStretchFactor(rightLayout, 0)

            self.setLayout(layout)

        def pushButtonClicked(self): # 078930
            code = self.lineEdit.text()
            # start_date = '2017-01-11'
            df = web.DataReader(code + ".ks", "yahoo")
            df['MA20'] = df['Adj Close'].rolling(window=20).mean()
            df['MA60'] = df['Adj Close'].rolling(window=60).mean()

            ax = self.fig.add_subplot(111)
            ax.plot(df.index, df['Adj Close'], label='Adj Close')
            ax.plot(df.index, df['MA20'], label='MA20')
            ax.plot(df.index, df['MA60'], label='MA60')
            ax.legend(loc='upper right')
            ax.grid()

            self.canvas.draw()

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    # show_window_of_qtdesigner()
    # show_layout_of_qtdesigner()
    # show_dialog_of_qtdesigner()
    show_chart_of_qtdesigner()
    pass
