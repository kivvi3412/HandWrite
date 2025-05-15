# -*- coding: utf-8 -*-
from pathlib import Path

from PIL import Image, ImageFont
from handright import Template, handwrite
from tools import BasicTools


class handwrite_generator(object):
    def __init__(self):
        self.template_params = {
            "rate": 4,  # 图片缩放比例
            "default_paper_x": 667,  # 默认纸张宽度 px
            "default_paper_y": 945,  # 默认纸张高度 px
            "default_font": BasicTools.get_ttf_file_path()[1][0],  # 默认字体文件路径
            "default_img_output_path": "outputs",  # 默认图片输出路径
            "default_font_size": 30,  # 默认字体大小
            "default_line_spacing": 70,  # 默认行间距 px
            "default_top_margin": 10,  # 默认顶部留白 px
            "default_bottom_margin": 10,  # 默认底部留白 px
            "default_left_margin": 10,  # 默认左边留白 px
            "default_right_margin": 10,  # 默认右边留白 px
            "default_word_spacing": 1,  # 默认字间距 px
            "default_line_spacing_sigma": 1,  # 默认行间距随机扰动 px
            "default_font_size_sigma": 1,  # 默认字体大小随机扰动 px
            "default_word_spacing_sigma": 1,  # 默认字间距随机扰动 px
            "default_perturb_x_sigma": 1,  # 默认笔画横向偏移随机扰动 px
            "default_perturb_y_sigma": 1,  # 默认笔画纵向偏移随机扰动 px
            "default_perturb_theta_sigma": 0.05,  # 默认笔画旋转偏移随机扰动 rad
            "default_start_chars": "“（[<",  # 特定字符提前换行，防止出现在行尾
            "default_end_chars": "，。",  # 防止特定字符因排版算法的自动换行而出现在行首
            "default_background": (0, 0, 0, 0),  # 默认背景颜色 (透明)
            "default_fill": (0, 0, 0, 255),  # 默认字体填充颜色 (黑色)
        }
        self.template = None    # 模板

    def modify_template_params(self, **kwargs):
        for key, value in kwargs.items():
            self.template_params[key] = value
        self.generate_template()

    def generate_template(self):
        rate = self.template_params["rate"]
        self.template = Template(
            background=Image.new(mode="RGBA", size=(
                self.template_params["default_paper_x"] * rate,
                self.template_params["default_paper_y"] * rate),
                                 color=self.template_params["default_background"]),
            font=ImageFont.truetype(self.template_params["default_font"],
                                    size=self.template_params["default_font_size"] * rate),
            line_spacing=self.template_params["default_line_spacing"] * rate,
            fill=self.template_params["default_fill"],
            left_margin=self.template_params["default_left_margin"] * rate,
            top_margin=self.template_params["default_top_margin"] * rate,
            right_margin=self.template_params["default_right_margin"] * rate,
            bottom_margin=self.template_params["default_bottom_margin"] * rate,
            word_spacing=self.template_params["default_word_spacing"] * rate,
            line_spacing_sigma=self.template_params["default_line_spacing_sigma"] * rate,
            font_size_sigma=self.template_params["default_font_size_sigma"] * rate,
            word_spacing_sigma=self.template_params["default_word_spacing_sigma"] * rate,
            start_chars=self.template_params["default_start_chars"],
            end_chars=self.template_params["default_end_chars"],
            perturb_x_sigma=self.template_params["default_perturb_x_sigma"],
            perturb_y_sigma=self.template_params["default_perturb_y_sigma"],
            perturb_theta_sigma=self.template_params["default_perturb_theta_sigma"]
        )

    def generate_image(self, text):
        temp_file_path_dict = {}
        if self.template is None:
            self.generate_template()
        images = handwrite(text, self.template, "outpus")
        output_dir = Path("outputs")
        output_dir.mkdir(parents=True, exist_ok=True)
        for i, im in enumerate(images):
            assert isinstance(im, Image.Image)
            save_path = output_dir.joinpath(f"{i}.png")
            temp_file_path_dict[i] = save_path
            im.save(save_path)
        return temp_file_path_dict


if __name__ == '__main__':
    generator = handwrite_generator()
    generator.modify_template_params(rate=8)
    generator.generate_template()
    generator.generate_image('''吾读史至商鞅徙木立信一事，而叹吾国国民之愚也，而叹执政者之煞费苦心也，而叹数千年来民智之不开、国几蹈于沦亡之惨也。谓予不信，请罄其说。
法令者，代谋幸福之具也。法令而善，其幸福吾民也必多，吾民方恐其不布此法令，或布而恐其不生效力，必竭全力以保障之，维持之，务使达到完善之目的而止。政府国民互相倚系，安有不信之理？法令而不善，则不惟无幸福之可言，且有危害之足惧，吾民又必竭全力以阻止此法令。虽欲吾信，又安有信之之理？乃若商鞅之与秦民适成此比例之反对，抑又何哉？
商鞅之法，良法也。今试一披吾国四千余年之纪载，而求其利国福民伟大之政治家，商鞅不首屈一指乎？鞅当孝公之世，中原鼎沸，战事正殷，举国疲劳，不堪言状。于是而欲战胜诸国，统一中原，不綦难哉？于是而变法之令出，其法惩奸宄以保人民之权利，务耕织以增进国民之富力，尚军功以树国威，孥贫怠以绝消耗。此诚我国从来未有之大政策，民何惮而不信？乃必徙木以立信者，吾于是知执政者之具费苦心也，吾于是知吾国国民之愚也，吾于是知数千年来民智黑暗国几蹈于沦亡之惨境有由来也
虽然，非常之原，黎民惧焉。民是此民矣，法是彼法矣，吾又何怪焉？吾特恐此徙木立信一事，若令彼东西各文明国民闻之，当必捧腹而笑，噭舌而讥矣。乌乎！吾欲无言。
商鞅“徙木立信”，是一个流传久远的历史故事，最初见于《史记·商君列传》。相传战国秦孝公在位时，宰相商鞅力主变法，但阻力''')
