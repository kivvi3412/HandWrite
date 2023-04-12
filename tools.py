# -*- coding: utf-8 -*-
import os
import fnmatch


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
