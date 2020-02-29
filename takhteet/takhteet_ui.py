# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'takhteet.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import page_ui as pg
import line_ui as ln
from PyQt5 import QtCore, QtGui, QtWidgets
y=5
def change():
    global y
    y=6
class Ui_MainWindow(object):
    def page(self):
        self.window=QtWidgets.QWidget()
        self.ui=pg.Ui_Form()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def line(self):
        self.window=QtWidgets.QWidget()
        self.ui=ln.Ui_Form_1()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def warning(self,title,message):
        mess=QtWidgets.QMessageBox()

        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
        
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(593, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        #self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        #self.spinBox_2.setObjectName("spinBox_2")
        self.textEdit = QtWidgets.QTextEdit(MainWindow)
        self.textEdit.setObjectName("textEdit")
        #self.verticalLayout_2.addWidget(self.textEdit)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox)
        #self.label_2 = QtWidgets.QLabel(self.centralwidget)
        #self.label_2.setObjectName("label_2")
        #self.verticalLayout_2.addWidget(self.label_2)
        #self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        #self.spinBox.setObjectName("spinBox")
        #self.verticalLayout_2.addWidget(self.spinBox)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setObjectName("spinBox_3")
        self.verticalLayout_2.addWidget(self.spinBox_3)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 20, 693, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 50, 693, 20))
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 10, 693, 41))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 50, 693, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.pushButton.clicked.connect(self.next)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        change()
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Hijri year"))
        self.label.setText(_translate("MainWindow", "Select month"))
        self.comboBox.setItemText(0, _translate("MainWindow", "محرم الحرام"))
        self.comboBox.setItemText(1, _translate("MainWindow", "صفر المظفر"))
        self.comboBox.setItemText(2, _translate("MainWindow", "ربيع الأول"))
        self.comboBox.setItemText(3, _translate("MainWindow", "ربيع الأخر"))
        self.comboBox.setItemText(4, _translate("MainWindow", "جمادي الأول"))
        self.comboBox.setItemText(5, _translate("MainWindow", "جمادي الأخر"))
        self.comboBox.setItemText(6, _translate("MainWindow", "رجب الأصب"))
        self.comboBox.setItemText(7, _translate("MainWindow", "شعبان الكريم"))
        self.comboBox.setItemText(8, _translate("MainWindow", "رمضان المعظم"))
        self.comboBox.setItemText(9, _translate("MainWindow", "شوال المكرم"))
        self.comboBox.setItemText(10, _translate("MainWindow", "ذي القعدة الحرام"))
        self.comboBox.setItemText(11, _translate("MainWindow", "ذي الحجة الحرام"))
        #self.label_2.setText(_translate("MainWindow", "No.of students"))
        self.label_4.setText(_translate("MainWindow", "No.of working days"))
        self.groupBox.setTitle(_translate("MainWindow", "Select layout"))
        self.radioButton_2.setText(_translate("MainWindow", "Grid layout"))
        self.radioButton.setText(_translate("MainWindow", "Tabular layout"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Select takhteet type"))
        self.radioButton_3.setText(_translate("MainWindow", "Line wise"))
        self.radioButton_4.setText(_translate("MainWindow", "Page wise"))
        self.pushButton.setText(_translate("MainWindow", "Proceed"))


    def next(self):
        try:
            #self.close()
            hijri=int(self.textEdit.toPlainText())
            month=self.comboBox.currentText()
            #stud=int(self.spinBox.text())
            days=int(self.spinBox_3.text())
            a = self.radioButton.isChecked()
            b = self.radioButton_2.isChecked()
            c = self.radioButton_3.isChecked()
            d = self.radioButton_4.isChecked()
            if(a==True):#Tabular
                #print(self.radioButton.text())
                form=1
            elif(b==True):#grid
                #print(self.radioButton_2.text())
                form=2
            if(c==True):#line
                #print(self.radioButton_3.text())
                flag=1
                ln.change(hijri,month,form,flag,days)
                self.line()
            elif(d==True):#page
                #print(self.radioButton_4.text())
                flag=2
                pg.change(hijri,month,form,flag,days)
                self.page()
            #print(y)
        except:
            self.warning("Alert","Enter correct details")
        
       

if __name__ == "__main__":
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    print("*********************** WELCOME ***************************")
    print("USER GUIDELINES")
    print("\n1. The user has to feed-in the following details:\n\ta)Current Hijri year and month.\n\tb) Total number of working days.")
    print("\n2. User can either select the tabular layout or grid layout of takhteet.")
    print("\n3. Takhteet can be made safah wise or line wise with the least entity of safah being 0.25.")
    print("\n4. Then depending on the type of takhteet selected, for each student enter,\n\tc) Student's name.\n\td) Student's current surat/page number and ayat/line number.\n\te) Number of safahs/lines per day assigned to the student.")
    print("\n5. All the takhteets of students will be generated in the excel file\n 'takhteet.xlsx' while the program is being\n executed.\n The excel file should be closed while the program is being executed,\n and both the program and the excel file saved in the same directory.")
    
    sys.exit(app.exec_())

