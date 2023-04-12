# -*- coding: utf-8 -*-
import fnmatch
import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsScene

from QT_GUI.qt_gui import *
from core import handwrite_generator


class BasicTools(object):
    def __init__(self):
        # 字体颜色字典
        self.font_color_dict = {
            "black": (0, 0, 0, 255),
            "white": (255, 255, 255, 255),
            "red": (255, 0, 0, 255),
            "blue": (0, 0, 255, 255)
        }

        # 背景颜色字典
        self.background_color_dict = {
            "transparent": (0, 0, 0, 0),
            "white": (255, 255, 255, 255)
        }

        # 默认方法倍率(rate)
        self.default_rate_dict = {
            "x1": 1,
            "x2": 2,
            "x4": 4,
            "x8": 8,
            "x16": 16,
            "x32": 32,
            "x64": 64
        }

    @staticmethod
    def get_ttf_file_path() -> (list, list):
        ttf_library_path = "ttf_library"
        ttf_files = []
        ttf_files_path = []
        for file in os.listdir(ttf_library_path):
            if fnmatch.fnmatch(file, '*.ttf'):
                ttf_files.append(file[:-4])
                ttf_files_path.append(os.path.join(ttf_library_path, file))
        return ttf_files, ttf_files_path


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

    def page_number_change(self):
        if self.page_number.currentText() != "":
            self.img_show_func(self.preview_image_dict[int(self.page_number.currentText())])

    def connect_signal(self):
        self.page_number.currentIndexChanged.connect(self.page_number_change)
        self.pushButton_export.clicked.connect(self.export)

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

        # 设置默认文本
        default_text = (
            "Type something here...\n"
            "Push `Preview` to see the result.\n"
            "Push `Export` to generate the image.\n"
        )
        self.textEdit_main.setPlainText(default_text)

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
        self.params["default_paper_x"] = int(self.lineEdit_width.text())
        self.params["default_paper_y"] = int(self.lineEdit_height.text())
        self.params["default_font"] = self.basic_tools.get_ttf_file_path()[1][self.ttf_selector.currentIndex()]
        self.params["default_font_size"] = int(self.lineEdit_font_size.text())
        self.params["default_line_spacing"] = int(self.lineEdit_line_spacing.text())
        self.params["default_word_spacing"] = int(self.lineEdit_char_distance.text())
        self.params["default_top_margin"] = int(self.lineEdit_margin_top.text())
        self.params["default_bottom_margin"] = int(self.lineEdit_margin_bottom.text())
        self.params["default_left_margin"] = int(self.lineEdit_margin_left.text())
        self.params["default_right_margin"] = int(self.lineEdit_margin_right.text())
        self.params["default_fill"] = self.basic_tools.font_color_dict[self.comboBox_char_color.currentText()]
        self.params["default_background"] = self.basic_tools.background_color_dict[
            self.comboBox_background_color.currentText()]
        self.params["rate"] = self.basic_tools.default_rate_dict[self.comboBox_resolution.currentText()]

    def get_text_from_textedit_main(self):
        return self.textEdit_main.toPlainText()

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
