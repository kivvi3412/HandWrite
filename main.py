# -*- coding: utf-8 -*-
import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsScene

from QT_GUI.qt_gui import *
from core import handwrite_generator
from tools import BasicTools
import requests

class Windows(QtWidgets.QDialog, Ui_Form):
    def __init__(self):
        super(Windows, self).__init__()
        self.setupUi(self)
        self.basic_tools = BasicTools()
        self.generator_engine = handwrite_generator()
        self.params = self.generator_engine.template_params  # 获取默认参数
        self.preview_image_dict = {}

        # 设置默认启动项
        self.set_default()
        self.connect_signal()

    def img_show_func(self, img_path):
        frame = QImage(str(img_path), "PNG")
        frame = frame.scaled(667, 945, Qt.KeepAspectRatio, Qt.SmoothTransformation | Qt.HighEventPriority)
        pix = QPixmap.fromImage(frame)
        item = QGraphicsPixmapItem(pix)
        scene = QGraphicsScene()
        scene.addItem(item)
        self.img_preview.setScene(scene)
        self.img_preview.horizontalScrollBar().setValue(1)  # 设置滚动条初始位置
        self.img_preview.verticalScrollBar().setValue(1)  # 设置滚动条初始位置

    def page_number_change(self):
        if self.page_number.currentText() != "":
            self.img_show_func(self.preview_image_dict[int(self.page_number.currentText())])

    def connect_signal(self):
        self.page_number.currentIndexChanged.connect(self.page_number_change)
        self.pushButton_export.clicked.connect(self.export)
        self.chatGPTPushButton_export.clicked.connect(self.submitToGPT)

    def set_default(self):
        # 设置宽度高度
        self.lineEdit_width.setText(str(self.params["default_paper_x"]))
        self.lineEdit_height.setText(str(self.params["default_paper_y"]))

        # 设置默认字体和候选字体
        self.ttf_selector.addItems(self.basic_tools.get_ttf_file_path()[0])
        self.ttf_selector.setCurrentIndex(0)

        # 设置字体大小，行距，字距
        self.lineEdit_font_size.setText(str(self.params["default_font_size"]))
        self.lineEdit_line_spacing.setText(str(self.params["default_line_spacing"]))
        self.lineEdit_char_distance.setText(str(self.params["default_word_spacing"]))

        # 设置留白
        self.lineEdit_margin_top.setText(str(self.params["default_top_margin"]))
        self.lineEdit_margin_bottom.setText(str(self.params["default_bottom_margin"]))
        self.lineEdit_margin_left.setText(str(self.params["default_left_margin"]))
        self.lineEdit_margin_right.setText(str(self.params["default_right_margin"]))

        # 设置默认字体颜色, 背景颜色
        self.comboBox_char_color.addItems(self.basic_tools.font_color_dict.keys())
        self.comboBox_char_color.setCurrentIndex(0)
        self.comboBox_background_color.addItems(self.basic_tools.background_color_dict.keys())
        self.comboBox_background_color.setCurrentIndex(0)

        # 设置扰动参数
        self.lineEdit_line_spacing_sigma.setText(str(self.params["default_line_spacing_sigma"]))
        self.lineEdit_font_size_sigma.setText(str(self.params["default_font_size_sigma"]))
        self.lineEdit_word_spacing_sigma.setText(str(self.params["default_word_spacing_sigma"]))
        self.lineEdit_perturb_x_sigma.setText(str(self.params["default_perturb_x_sigma"]))
        self.lineEdit_perturb_y_sigma.setText(str(self.params["default_perturb_y_sigma"]))
        self.lineEdit_perturb_theta_sigma.setText(str(self.params["default_perturb_theta_sigma"]))

        # 设置默认文本
        default_text = (
            "使用 PyQt5 编写的手写字生成器，旨在完成一些无用的手写作业任务"
            "本项目提供了丰富的参数设置，以满足您在生成手写字时的个性化需求"
        )
        self.textEdit_main.setPlainText(default_text)

        self.chatGPTTextEdit_main.setPlainText("向ChatGPT说出您的假设")

        # 设置默认倍率
        self.comboBox_resolution.addItems(self.basic_tools.default_rate_dict.keys())
        self.comboBox_resolution.setCurrentIndex(2)

        # 设置默认预览
        self.generator_engine.modify_template_params(default_background=(255, 255, 255, 255))
        preview_image_dict = self.generator_engine.generate_image(default_text)
        self.img_show_func(preview_image_dict[0])
        self.page_number.addItems([str(i) for i in preview_image_dict])  # 设置page列表

    # 读取填写信息
    def get_info_from_form(self):
        self.params["default_paper_x"] = int(float(self.lineEdit_width.text()))
        self.params["default_paper_y"] = int(float(self.lineEdit_height.text()))
        self.params["default_font"] = self.basic_tools.get_ttf_file_path()[1][self.ttf_selector.currentIndex()]
        self.params["default_font_size"] = int(float(self.lineEdit_font_size.text()))
        self.params["default_line_spacing"] = int(float(self.lineEdit_line_spacing.text()))
        self.params["default_word_spacing"] = int(float(self.lineEdit_char_distance.text()))
        self.params["default_top_margin"] = int(float(self.lineEdit_margin_top.text()))
        self.params["default_bottom_margin"] = int(float(self.lineEdit_margin_bottom.text()))
        self.params["default_left_margin"] = int(float(self.lineEdit_margin_left.text()))
        self.params["default_right_margin"] = int(float(self.lineEdit_margin_right.text()))
        self.params["default_fill"] = self.basic_tools.font_color_dict[self.comboBox_char_color.currentText()]
        self.params["default_background"] = self.basic_tools.background_color_dict[
            self.comboBox_background_color.currentText()]
        self.params["rate"] = self.basic_tools.default_rate_dict[self.comboBox_resolution.currentText()]
        self.params["default_line_spacing_sigma"] = float(self.lineEdit_line_spacing_sigma.text())
        self.params["default_font_size_sigma"] = float(self.lineEdit_font_size_sigma.text())
        self.params["default_word_spacing_sigma"] = float(self.lineEdit_word_spacing_sigma.text())
        self.params["default_perturb_x_sigma"] = float(self.lineEdit_perturb_x_sigma.text())
        self.params["default_perturb_y_sigma"] = float(self.lineEdit_perturb_y_sigma.text())
        self.params["default_perturb_theta_sigma"] = float(self.lineEdit_perturb_theta_sigma.text())

    def get_text_from_textedit_main(self):
        return self.textEdit_main.toPlainText()

    def submitToGPT(self):
        text = self.chatGPTTextEdit_main.toPlainText()


        url = "https://openai.api2d.net/v1/chat/completions"

        headers = {
            'Content-Type': 'application/json',
            'x-api2d-no-cache': "1",
            'Authorization': 'Bearer 这里改成api2d的token'
        }

        data = {
            "model": "gpt-3.5-turbo",
            "safe_mode": "true",
            "messages": [{"role": "user", "content": text}]
,
        }
        response = requests.post(url, headers=headers, json=data)
        self.textEdit_main.setText(response.json()["choices"][0]["message"]["content"])

    # 导出
    def export(self):
        folder_path = "outputs"
        if os.path.exists(folder_path):
            # 遍历目录中的所有文件和子目录
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                except Exception as e:
                    print(f"无法删除文件 '{file_path}': {e}")
        else:
            print(f"目录 '{folder_path}' 不存在。")
        self.page_number.clear()
        self.get_info_from_form()
        self.generator_engine.modify_template_params(**self.params)
        self.generator_engine.generate_template()
        self.preview_image_dict = self.generator_engine.generate_image(
            self.get_text_from_textedit_main())
        self.img_show_func(self.preview_image_dict[0])
        self.page_number.addItems([str(i) for i in self.preview_image_dict])


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Windows()
    window.show()
    sys.exit(app.exec_())
