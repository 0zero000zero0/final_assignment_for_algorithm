# Form implementation generated from reading ui file 'e:\python\final_assignment_for_algorithm\ui\ui.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Base(object):
    def setupUi(self, Base):
        Base.setObjectName("Base")
        Base.resize(1000, 800)
        font = QtGui.QFont()
        font.setPointSize(12)
        Base.setFont(font)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Base)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_7 = QtWidgets.QWidget(parent=Base)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.graphicsView = QtWidgets.QGraphicsView(parent=self.widget_7)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_8.addWidget(self.graphicsView)
        self.result = QtWidgets.QPlainTextEdit(parent=self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.result.setFont(font)
        self.result.setLineWrapMode(QtWidgets.QPlainTextEdit.LineWrapMode.WidgetWidth)
        self.result.setReadOnly(False)
        self.result.setPlainText("")
        self.result.setObjectName("result")
        self.verticalLayout_8.addWidget(self.result)
        self.verticalLayout_8.setStretch(0, 3)
        self.verticalLayout_8.setStretch(1, 1)
        self.horizontalLayout.addWidget(self.widget_7)
        self.options = QtWidgets.QWidget(parent=Base)
        self.options.setObjectName("options")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.options)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.chooses = QtWidgets.QComboBox(parent=self.options)
        self.chooses.setObjectName("chooses")
        self.chooses.addItem("")
        self.chooses.addItem("")
        self.chooses.addItem("")
        self.chooses.addItem("")
        self.verticalLayout_7.addWidget(self.chooses)
        self.widget_2 = QtWidgets.QWidget(parent=self.options)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.widget_2)
        self.label.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.LineWrapMode.WidgetWidth)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.verticalLayout_7.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(parent=self.options)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.start = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.verticalLayout_4.addWidget(self.start)
        self.verticalLayout_7.addWidget(self.widget)
        self.widget_4 = QtWidgets.QWidget(parent=self.options)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pre_step = QtWidgets.QPushButton(parent=self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pre_step.setFont(font)
        self.pre_step.setObjectName("pre_step")
        self.verticalLayout_3.addWidget(self.pre_step)
        self.verticalLayout_7.addWidget(self.widget_4)
        self.widget_3 = QtWidgets.QWidget(parent=self.options)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.next_step = QtWidgets.QPushButton(parent=self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.next_step.setFont(font)
        self.next_step.setObjectName("next_step")
        self.verticalLayout_2.addWidget(self.next_step)
        self.verticalLayout_7.addWidget(self.widget_3)
        self.widget_6 = QtWidgets.QWidget(parent=self.options)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.clear = QtWidgets.QPushButton(parent=self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.verticalLayout_6.addWidget(self.clear)
        self.verticalLayout_7.addWidget(self.widget_6)
        self.widget_5 = QtWidgets.QWidget(parent=self.options)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.quit = QtWidgets.QPushButton(parent=self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quit.setFont(font)
        self.quit.setObjectName("quit")
        self.verticalLayout_5.addWidget(self.quit)
        self.verticalLayout_7.addWidget(self.widget_5)
        self.horizontalLayout.addWidget(self.options)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Base)
        QtCore.QMetaObject.connectSlotsByName(Base)

    def retranslateUi(self, Base):
        _translate = QtCore.QCoreApplication.translate
        Base.setWindowTitle(_translate("Base", "Form"))
        self.result.setPlaceholderText(_translate("Base", "这里将会显示过程与最后的结果"))
        self.chooses.setItemText(0, _translate("Base", "最近点对(蛮力)"))
        self.chooses.setItemText(1, _translate("Base", "最近点对(分治)"))
        self.chooses.setItemText(2, _translate("Base", "凸包(蛮力)"))
        self.chooses.setItemText(3, _translate("Base", "凸包(Graham\'s scan)"))
        self.label.setText(_translate("Base", "点"))
        self.plainTextEdit.setPlainText(_translate("Base", "1 4\n"
"2 1\n"
"4 9\n"
"3 2\n"
"7 1\n"
"-2 4\n"
"-3 2"))
        self.plainTextEdit.setPlaceholderText(_translate("Base", "使用空格隔开坐标 使用换行隔开点 "))
        self.start.setText(_translate("Base", "开始"))
        self.pre_step.setText(_translate("Base", "上一步"))
        self.next_step.setText(_translate("Base", "下一步"))
        self.clear.setText(_translate("Base", "清空"))
        self.quit.setText(_translate("Base", "退出"))
