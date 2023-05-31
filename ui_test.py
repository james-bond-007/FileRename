# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testOepYmg.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.dir_select_Button = QPushButton(self.centralwidget)
        self.dir_select_Button.setObjectName(u"dir_select_Button")
        self.dir_select_Button.setGeometry(QRect(190, 50, 83, 32))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(500, 10, 271, 521))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.result_data_Text = QPlainTextEdit(self.layoutWidget)
        self.result_data_Text.setObjectName(u"result_data_Text")

        self.verticalLayout_2.addWidget(self.result_data_Text)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 10, 461, 33))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.init_dir_label = QLabel(self.layoutWidget1)
        self.init_dir_label.setObjectName(u"init_dir_label")

        self.horizontalLayout.addWidget(self.init_dir_label)

        self.init_dir_entry = QLineEdit(self.layoutWidget1)
        self.init_dir_entry.setObjectName(u"init_dir_entry")

        self.horizontalLayout.addWidget(self.init_dir_entry)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 100, 461, 23))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.init_data_label = QLabel(self.layoutWidget2)
        self.init_data_label.setObjectName(u"init_data_label")

        self.horizontalLayout_2.addWidget(self.init_data_label)

        self.init_prefix_Text = QLineEdit(self.layoutWidget2)
        self.init_prefix_Text.setObjectName(u"init_prefix_Text")

        self.horizontalLayout_2.addWidget(self.init_prefix_Text)

        self.label_3 = QLabel(self.layoutWidget2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.init_suffix_Text = QLineEdit(self.layoutWidget2)
        self.init_suffix_Text.setObjectName(u"init_suffix_Text")

        self.horizontalLayout_2.addWidget(self.init_suffix_Text)

        self.layoutWidget3 = QWidget(self.centralwidget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(90, 150, 279, 32))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.modify_Button = QPushButton(self.layoutWidget3)
        self.modify_Button.setObjectName(u"modify_Button")

        self.horizontalLayout_3.addWidget(self.modify_Button)

        self.resume_Button = QPushButton(self.layoutWidget3)
        self.resume_Button.setObjectName(u"resume_Button")

        self.horizontalLayout_3.addWidget(self.resume_Button)

        self.rename_Button = QPushButton(self.layoutWidget3)
        self.rename_Button.setObjectName(u"rename_Button")

        self.horizontalLayout_3.addWidget(self.rename_Button)

        self.layoutWidget4 = QWidget(self.centralwidget)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(20, 200, 451, 331))
        self.verticalLayout = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.log_data_Text = QPlainTextEdit(self.layoutWidget4)
        self.log_data_Text.setObjectName(u"log_data_Text")

        self.verticalLayout.addWidget(self.log_data_Text)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u540d\u5904\u7406\u5668_YSP_V1.0", None))
        self.dir_select_Button.setText(QCoreApplication.translate("MainWindow", u"\u8def\u5f84\u9009\u62e9", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u540e\u7ed3\u679c", None))
        self.init_dir_label.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u6587\u4ef6\u8def\u5f84\uff1a", None))
        self.init_dir_entry.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u76ee\u5f55\u9009\u62e9\u91cd\u547d\u540d\u6587\u4ef6\u76ee\u5f55", None))
        self.init_data_label.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u524d\u7f00\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u540e\u7f00\uff1a", None))
        self.modify_Button.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u524d\u540e\u7f00", None))
        self.resume_Button.setText(QCoreApplication.translate("MainWindow", u"\u5220\u524d\u540e\u7f00", None))
        self.rename_Button.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u65b0\u547d\u540d", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7", None))
    # retranslateUi

