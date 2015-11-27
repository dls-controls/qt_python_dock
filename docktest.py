#!/bin/env dls-python
from PyQt4 import QtCore, QtGui

app = QtGui.QApplication([''])

mw = QtGui.QMainWindow() # mw = MainWindow
mw.setCentralWidget(None)
mw.showMaximized()

mw.dockWdg1 = QtGui.QDockWidget(mw)
mw.content1 = QtGui.QTreeWidget()
mw.dockWdg1.setWidget(mw.content1)
mw.addDockWidget(QtCore.Qt.TopDockWidgetArea, mw.dockWdg1)
mw.dockWdg1.setWindowTitle("1st dock widget")

mw.dockWdg2 = QtGui.QDockWidget(mw)
mw.content2 = QtGui.QTreeWidget()
mw.dockWdg2.setWidget(mw.content2)
mw.addDockWidget(QtCore.Qt.RightDockWidgetArea, mw.dockWdg2)
mw.dockWdg2.setWindowTitle("2nd dock widget")

mw.dockWdg3 = QtGui.QDockWidget(mw)
mw.content3 = QtGui.QTreeWidget()
mw.dockWdg3.setWidget(mw.content3)
mw.addDockWidget(QtCore.Qt.BottomDockWidgetArea, mw.dockWdg3)
mw.dockWdg3.setWindowTitle("3rd dock widget")

mw.show()
app.exec_()
