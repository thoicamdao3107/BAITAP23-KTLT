from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 544)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # GroupBox 1 - Personal Information
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 30, 741, 211))
        self.groupBox.setObjectName("groupBox")

        # Customer Name
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 40, 111, 21))
        self.label.setObjectName("label")
        self.lineEditCustomerName = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditCustomerName.setGeometry(QtCore.QRect(150, 30, 311, 31))
        self.lineEditCustomerName.setObjectName("lineEditCustomerName")

        # Quantity
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 55, 16))
        self.label_2.setObjectName("label_2")
        self.lineEditQuantity = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditQuantity.setGeometry(QtCore.QRect(150, 80, 311, 31))
        self.lineEditQuantity.setObjectName("lineEditQuantity")

        # Checkbox: Customer is Student
        self.checkBox = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(160, 120, 161, 20))
        self.checkBox.setObjectName("checkBox")

        # Payment
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 55, 16))
        self.label_3.setObjectName("label_3")
        self.lineEditPayment = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditPayment.setGeometry(QtCore.QRect(160, 150, 311, 31))
        self.lineEditPayment.setObjectName("lineEditPayment")

        # Buttons
        self.pushButtonNewSelling = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonNewSelling.setGeometry(QtCore.QRect(510, 30, 171, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/8757607_marketplace_menu_selling_website_social media_icon.png"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonNewSelling.setIcon(icon)
        self.pushButtonNewSelling.setObjectName("pushButtonNewSelling")

        self.pushButtonCalculate = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonCalculate.setGeometry(QtCore.QRect(510, 70, 171, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/8468578_calculator_finance_calculate_mathematics_calculation_icon.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonCalculate.setIcon(icon1)
        self.pushButtonCalculate.setObjectName("pushButtonCalculate")

        self.pushButtonStatistic = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonStatistic.setGeometry(QtCore.QRect(510, 110, 171, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/465076_statistic_analytics_charts_diagram_graph_icon.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonStatistic.setIcon(icon2)
        self.pushButtonStatistic.setObjectName("pushButtonStatistic")

        self.pushButtoExit = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtoExit.setGeometry(QtCore.QRect(510, 150, 171, 31))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/9104334_sign out_logout_exit_out_icon.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.pushButtoExit.setIcon(icon3)
        self.pushButtoExit.setObjectName("pushButtoExit")

        # GroupBox 2 - Statistics
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 741, 201))
        self.groupBox_2.setObjectName("groupBox_2")

        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(40, 40, 171, 16))
        self.label_4.setObjectName("label_4")

        self.lineEditTC = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditTC.setGeometry(QtCore.QRect(230, 30, 311, 31))
        self.lineEditTC.setObjectName("lineEditTC")

        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(40, 90, 171, 16))
        self.label_5.setObjectName("label_5")

        self.lineEditTSC = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditTSC.setGeometry(QtCore.QRect(230, 80, 311, 31))
        self.lineEditTSC.setObjectName("lineEditTSC")

        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(40, 140, 101, 16))
        self.label_6.setObjectName("label_6")

        self.lineEditTR = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditTR.setGeometry(QtCore.QRect(230, 130, 311, 31))
        self.lineEditTR.setObjectName("lineEditTR")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Personal Information:"))
        self.label.setText(_translate("MainWindow", "Customer Name:"))
        self.label_2.setText(_translate("MainWindow", "Quantity:"))
        self.checkBox.setText(_translate("MainWindow", "Customer is Student"))
        self.label_3.setText(_translate("MainWindow", "Payment:"))
        self.pushButtonNewSelling.setText(_translate("MainWindow", "New Selling"))
        self.pushButtonCalculate.setText(_translate("MainWindow", "Calculate"))
        self.pushButtonStatistic.setText(_translate("MainWindow", "Statistic"))
        self.pushButtoExit.setText(_translate("MainWindow", "Exit"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_4.setText(_translate("MainWindow", "Total number of Customers:"))
        self.label_5.setText(_translate("MainWindow", "Total student customers:"))
        self.label_6.setText(_translate("MainWindow", "Total revenue:"))
