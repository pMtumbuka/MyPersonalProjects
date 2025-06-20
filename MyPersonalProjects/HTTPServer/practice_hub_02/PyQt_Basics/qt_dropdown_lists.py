# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_dropdown_lists.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 60, 361, 221))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 251, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 33))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen_a_File = QtWidgets.QMenu(self.menuFile)
        self.menuOpen_a_File.setObjectName("menuOpen_a_File")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionClose_All = QtWidgets.QAction(MainWindow)
        self.actionClose_All.setObjectName("actionClose_All")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setStatusTip("")
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionSelect_All = QtWidgets.QAction(MainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionCtrl_O = QtWidgets.QAction(MainWindow)
        self.actionCtrl_O.setObjectName("actionCtrl_O")
        self.actionGet_Help_Locally = QtWidgets.QAction(MainWindow)
        self.actionGet_Help_Locally.setObjectName("actionGet_Help_Locally")
        self.actionGet_Help_Onine = QtWidgets.QAction(MainWindow)
        self.actionGet_Help_Onine.setObjectName("actionGet_Help_Onine")
        self.menuOpen_a_File.addAction(self.actionCtrl_O)
        self.menuOpen_a_File.addSeparator()
        self.menuFile.addAction(self.menuOpen_a_File.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionClose_All)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuHelp.addAction(self.actionGet_Help_Locally)
        self.menuHelp.addAction(self.actionGet_Help_Onine)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.actionNew.triggered.connect(lambda: self.button_clicked("New Was Clicked!"))
        self.actionSave.triggered.connect(lambda: self.button_clicked("Save Was Clicked!"))
        self.actionSave_As.triggered.connect(lambda: self.button_clicked("Save_As Was Clicked!"))
        self.actionSelect_All.triggered.connect(lambda: self.button_clicked("Select_All Was Clicked!"))
        self.actionCopy.triggered.connect(lambda: self.button_clicked("Copy Was Clicked!"))
        self.actionCut.triggered.connect(lambda: self.button_clicked("Cut Was Clicked!"))
        self.actionPaste.triggered.connect(lambda: self.button_clicked("Paste Was Clicked!"))
        self.actionClose.triggered.connect(lambda: self.button_clicked("Close Was Clicked!"))
        self.actionClose_All.triggered.connect(lambda: self.button_clicked("Close_All Was Clicked!"))
        self.actionDelete.triggered.connect(lambda: self.button_clicked("Delete Was Clicked!"))
        self.actionRedo.triggered.connect(lambda: self.button_clicked("Redo Was Clicked!"))
        self.actionUndo.triggered.connect(lambda: self.button_clicked("Undo Was Clicked!"))
        self.actionGet_Help_Locally.triggered.connect(lambda: self.button_clicked("Get_Help_Locally Was Clicked!"))
        self.actionGet_Help_Onine.triggered.connect(lambda: self.button_clicked("Get_Help_Online Was Clicked!"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOpen_a_File.setTitle(_translate("MainWindow", "Open a File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save a File"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..."))
        self.actionNew.setText(_translate("MainWindow", "New..."))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create a New File"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose.setStatusTip(_translate("MainWindow", "Close the Current File Only"))
        self.actionClose_All.setText(_translate("MainWindow", "Close All"))
        self.actionClose_All.setStatusTip(_translate("MainWindow", "Close All Opened Files"))
        self.actionCut.setText(_translate("MainWindow", "Cut "))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionDelete.setShortcut(_translate("MainWindow", "Ctrl+Del"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All"))
        self.actionSelect_All.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionCtrl_O.setText(_translate("MainWindow", "Ctrl+O"))
        self.actionGet_Help_Locally.setText(_translate("MainWindow", "Get Help Locally"))
        self.actionGet_Help_Locally.setShortcut(_translate("MainWindow", "F1"))
        self.actionGet_Help_Onine.setText(_translate("MainWindow", "Get Help Onine"))
        self.actionGet_Help_Onine.setShortcut(_translate("MainWindow", "Ctrl+F1"))

    def button_clicked(self, message):
        self.label.setText(message)
        self.label.adjustSize()

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
