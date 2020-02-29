# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'line.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import myiter
import test
from PyQt5 import QtCore, QtGui, QtWidgets

hijri=1
month="june"
form=2
flag=1
days=20
def change(h,m,fo,fl,d):
    global hijri
    global month
    global form
    global flag
    global days
    hijri=h
    month=m
    form=fo
    flag=fl
    days=d

class Ui_Form_1(object):

    def warning(self,title,message):
        mess=QtWidgets.QMessageBox()

        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def messagebox(self,title,message):
        mess=QtWidgets.QMessageBox()

        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def setupUi(self, Form_1):
        Form_1.setObjectName("Form_1")
        Form_1.resize(400, 275)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form_1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form_1)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(Form_1)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.label_2 = QtWidgets.QLabel(Form_1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        #self.spinBox = QtWidgets.QSpinBox(Form_1)
        #self.spinBox.setObjectName("spinBox")
        self.textEdit_1 = QtWidgets.QTextEdit(Form_1)
        self.textEdit_1.setObjectName("textEdit_1")
        self.verticalLayout.addWidget(self.textEdit_1)
        self.label_3 = QtWidgets.QLabel(Form_1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.spinBox_2 = QtWidgets.QSpinBox(Form_1)
        self.spinBox_2.setObjectName("spinBox_2")
        
        self.verticalLayout.addWidget(self.spinBox_2)
        self.label_4 = QtWidgets.QLabel(Form_1)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.spinBox_3 = QtWidgets.QSpinBox(Form_1)
        self.spinBox_3.setObjectName("spinBox_3")
        self.verticalLayout.addWidget(self.spinBox_3)
        self.pushButton = QtWidgets.QPushButton(Form_1)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form_1)
        QtCore.QMetaObject.connectSlotsByName(Form_1)
        self.pushButton.clicked.connect(self.ln_gen)
        
    def retranslateUi(self, Form_1):
        _translate = QtCore.QCoreApplication.translate
        Form_1.setWindowTitle(_translate("Form_1", "Form"))
        self.label.setText(_translate("Form_1", "Student Name"))
        self.label_2.setText(_translate("Form_1", "Current page no."))
        self.label_3.setText(_translate("Form_1", "Line no."))
        self.label_4.setText(_translate("Form_1", "Lines per day"))
        self.pushButton.setText(_translate("Form_1", "Generate"))
    def ln_gen(self):
        try:
            name=self.textEdit.toPlainText()
            n=int(self.spinBox_3.text())
            sur=int(self.textEdit_1.toPlainText())
            x=int(self.spinBox_2.text())
            if(name=="" or n==0.0):
                raise Exception()
            yr=myiter.to_arab(hijri)
            v=test.line_search1(x,sur,n,days)
            myiter.to_excel2(v,days,form,name,n,month,yr)
            print("\nTakhteet added in excel sheet")
            self.messagebox("Alert","Takhteet added successfully")
        except:
            self.warning("Alert","Enter valid credentials")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_1 = QtWidgets.QWidget()
    ui = Ui_Form_1()
    ui.setupUi(Form_1)
    Form_1.show()
    sys.exit(app.exec_())

