# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1110, 645)
        self.horizontalLayout_14 = QHBoxLayout(Form)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.Display = QVBoxLayout()
        self.Display.setObjectName(u"Display")
        self.img_preview = QGraphicsView(Form)
        self.img_preview.setObjectName(u"img_preview")

        self.Display.addWidget(self.img_preview)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_line_spacing_sigma = QLabel(Form)
        self.label_line_spacing_sigma.setObjectName(u"label_line_spacing_sigma")

        self.horizontalLayout_13.addWidget(self.label_line_spacing_sigma)

        self.label_font_size_sigma = QLabel(Form)
        self.label_font_size_sigma.setObjectName(u"label_font_size_sigma")

        self.horizontalLayout_13.addWidget(self.label_font_size_sigma)

        self.label_word_spacing_sigma = QLabel(Form)
        self.label_word_spacing_sigma.setObjectName(u"label_word_spacing_sigma")

        self.horizontalLayout_13.addWidget(self.label_word_spacing_sigma)

        self.label_perturb_x_sigma = QLabel(Form)
        self.label_perturb_x_sigma.setObjectName(u"label_perturb_x_sigma")

        self.horizontalLayout_13.addWidget(self.label_perturb_x_sigma)

        self.label_perturb_y_sigma = QLabel(Form)
        self.label_perturb_y_sigma.setObjectName(u"label_perturb_y_sigma")

        self.horizontalLayout_13.addWidget(self.label_perturb_y_sigma)

        self.label_perturb_theta_sigma = QLabel(Form)
        self.label_perturb_theta_sigma.setObjectName(u"label_perturb_theta_sigma")

        self.horizontalLayout_13.addWidget(self.label_perturb_theta_sigma)


        self.Display.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lineEdit_line_spacing_sigma = QLineEdit(Form)
        self.lineEdit_line_spacing_sigma.setObjectName(u"lineEdit_line_spacing_sigma")

        self.horizontalLayout_12.addWidget(self.lineEdit_line_spacing_sigma)

        self.lineEdit_font_size_sigma = QLineEdit(Form)
        self.lineEdit_font_size_sigma.setObjectName(u"lineEdit_font_size_sigma")

        self.horizontalLayout_12.addWidget(self.lineEdit_font_size_sigma)

        self.lineEdit_word_spacing_sigma = QLineEdit(Form)
        self.lineEdit_word_spacing_sigma.setObjectName(u"lineEdit_word_spacing_sigma")

        self.horizontalLayout_12.addWidget(self.lineEdit_word_spacing_sigma)

        self.lineEdit_perturb_x_sigma = QLineEdit(Form)
        self.lineEdit_perturb_x_sigma.setObjectName(u"lineEdit_perturb_x_sigma")

        self.horizontalLayout_12.addWidget(self.lineEdit_perturb_x_sigma)

        self.lineEdit_perturb_y_sigma = QLineEdit(Form)
        self.lineEdit_perturb_y_sigma.setObjectName(u"lineEdit_perturb_y_sigma")

        self.horizontalLayout_12.addWidget(self.lineEdit_perturb_y_sigma)

        self.lineEdit_perturb_theta_sigma = QLineEdit(Form)
        self.lineEdit_perturb_theta_sigma.setObjectName(u"lineEdit_perturb_theta_sigma")

        self.horizontalLayout_12.addWidget(self.lineEdit_perturb_theta_sigma)


        self.Display.addLayout(self.horizontalLayout_12)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.page_label = QLabel(Form)
        self.page_label.setObjectName(u"page_label")
        self.page_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.page_label)

        self.page_number = QComboBox(Form)
        self.page_number.setObjectName(u"page_number")

        self.horizontalLayout.addWidget(self.page_number)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 8)

        self.Display.addLayout(self.horizontalLayout)


        self.horizontalLayout_14.addLayout(self.Display)

        self.Info = QVBoxLayout()
        self.Info.setObjectName(u"Info")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_width = QLabel(Form)
        self.label_width.setObjectName(u"label_width")

        self.horizontalLayout_2.addWidget(self.label_width)

        self.label_height = QLabel(Form)
        self.label_height.setObjectName(u"label_height")

        self.horizontalLayout_2.addWidget(self.label_height)


        self.Info.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_width = QLineEdit(Form)
        self.lineEdit_width.setObjectName(u"lineEdit_width")

        self.horizontalLayout_3.addWidget(self.lineEdit_width)

        self.resolution_x = QLabel(Form)
        self.resolution_x.setObjectName(u"resolution_x")

        self.horizontalLayout_3.addWidget(self.resolution_x)

        self.lineEdit_height = QLineEdit(Form)
        self.lineEdit_height.setObjectName(u"lineEdit_height")

        self.horizontalLayout_3.addWidget(self.lineEdit_height)


        self.Info.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.ttf_selector = QComboBox(Form)
        self.ttf_selector.setObjectName(u"ttf_selector")

        self.horizontalLayout_4.addWidget(self.ttf_selector)


        self.Info.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_font_size = QLabel(Form)
        self.label_font_size.setObjectName(u"label_font_size")

        self.horizontalLayout_5.addWidget(self.label_font_size)

        self.label_line_spacing = QLabel(Form)
        self.label_line_spacing.setObjectName(u"label_line_spacing")

        self.horizontalLayout_5.addWidget(self.label_line_spacing)

        self.label_char_distance = QLabel(Form)
        self.label_char_distance.setObjectName(u"label_char_distance")

        self.horizontalLayout_5.addWidget(self.label_char_distance)


        self.Info.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lineEdit_font_size = QLineEdit(Form)
        self.lineEdit_font_size.setObjectName(u"lineEdit_font_size")

        self.horizontalLayout_6.addWidget(self.lineEdit_font_size)

        self.lineEdit_line_spacing = QLineEdit(Form)
        self.lineEdit_line_spacing.setObjectName(u"lineEdit_line_spacing")

        self.horizontalLayout_6.addWidget(self.lineEdit_line_spacing)

        self.lineEdit_char_distance = QLineEdit(Form)
        self.lineEdit_char_distance.setObjectName(u"lineEdit_char_distance")

        self.horizontalLayout_6.addWidget(self.lineEdit_char_distance)


        self.Info.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_margin = QLabel(Form)
        self.label_margin.setObjectName(u"label_margin")

        self.horizontalLayout_7.addWidget(self.label_margin)


        self.Info.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lineEdit_margin_top = QLineEdit(Form)
        self.lineEdit_margin_top.setObjectName(u"lineEdit_margin_top")

        self.horizontalLayout_8.addWidget(self.lineEdit_margin_top)

        self.lineEdit_margin_bottom = QLineEdit(Form)
        self.lineEdit_margin_bottom.setObjectName(u"lineEdit_margin_bottom")

        self.horizontalLayout_8.addWidget(self.lineEdit_margin_bottom)

        self.lineEdit_margin_left = QLineEdit(Form)
        self.lineEdit_margin_left.setObjectName(u"lineEdit_margin_left")

        self.horizontalLayout_8.addWidget(self.lineEdit_margin_left)

        self.lineEdit_margin_right = QLineEdit(Form)
        self.lineEdit_margin_right.setObjectName(u"lineEdit_margin_right")

        self.horizontalLayout_8.addWidget(self.lineEdit_margin_right)


        self.Info.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_char_color = QLabel(Form)
        self.label_char_color.setObjectName(u"label_char_color")

        self.horizontalLayout_10.addWidget(self.label_char_color)

        self.label_background_color = QLabel(Form)
        self.label_background_color.setObjectName(u"label_background_color")

        self.horizontalLayout_10.addWidget(self.label_background_color)


        self.Info.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.comboBox_char_color = QComboBox(Form)
        self.comboBox_char_color.setObjectName(u"comboBox_char_color")

        self.horizontalLayout_9.addWidget(self.comboBox_char_color)

        self.comboBox_background_color = QComboBox(Form)
        self.comboBox_background_color.setObjectName(u"comboBox_background_color")

        self.horizontalLayout_9.addWidget(self.comboBox_background_color)


        self.Info.addLayout(self.horizontalLayout_9)

        self.textEdit_main = QTextEdit(Form)
        self.textEdit_main.setObjectName(u"textEdit_main")

        self.Info.addWidget(self.textEdit_main)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.comboBox_resolution = QComboBox(Form)
        self.comboBox_resolution.setObjectName(u"comboBox_resolution")
        self.comboBox_resolution.setIconSize(QSize(16, 16))

        self.horizontalLayout_11.addWidget(self.comboBox_resolution)

        self.pushButton_export = QPushButton(Form)
        self.pushButton_export.setObjectName(u"pushButton_export")

        self.horizontalLayout_11.addWidget(self.pushButton_export)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 5)

        self.Info.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_14.addLayout(self.Info)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_line_spacing_sigma.setText(QCoreApplication.translate("Form", u"\u884c\u95f4\u8ddd\u6270\u52a8", None))
        self.label_font_size_sigma.setText(QCoreApplication.translate("Form", u"\u5b57\u4f53\u5927\u5c0f\u6270\u52a8", None))
        self.label_word_spacing_sigma.setText(QCoreApplication.translate("Form", u"\u5b57\u95f4\u8ddd\u6270\u52a8", None))
        self.label_perturb_x_sigma.setText(QCoreApplication.translate("Form", u"\u6a2a\u5411\u7b14\u753b\u6270\u52a8", None))
        self.label_perturb_y_sigma.setText(QCoreApplication.translate("Form", u"\u7eb5\u5411\u7b14\u753b\u6270\u52a8", None))
        self.label_perturb_theta_sigma.setText(QCoreApplication.translate("Form", u"\u65cb\u8f6c\u7b14\u753b\u6270\u52a8", None))
        self.page_label.setText(QCoreApplication.translate("Form", u"Page:", None))
        self.label_width.setText(QCoreApplication.translate("Form", u"\u5bbd\u5ea6", None))
        self.label_height.setText(QCoreApplication.translate("Form", u"\u9ad8\u5ea6", None))
        self.resolution_x.setText(QCoreApplication.translate("Form", u"x", None))
        self.label_font_size.setText(QCoreApplication.translate("Form", u"\u5b57\u4f53\u5927\u5c0f", None))
        self.label_line_spacing.setText(QCoreApplication.translate("Form", u"\u884c\u8ddd", None))
        self.label_char_distance.setText(QCoreApplication.translate("Form", u"\u5b57\u8ddd", None))
        self.label_margin.setText(QCoreApplication.translate("Form", u"\u7559\u767d(\u4e0a,\u4e0b,\u5de6,\u53f3)", None))
        self.label_char_color.setText(QCoreApplication.translate("Form", u"\u5b57\u4f53\u8272", None))
        self.label_background_color.setText(QCoreApplication.translate("Form", u"\u80cc\u666f\u8272", None))
        self.pushButton_export.setText(QCoreApplication.translate("Form", u"Export", None))
    # retranslateUi

