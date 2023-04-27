import ezdxf
from model import items
from ezdxf.addons.drawing import matplotlib
from settings import FONT_NAME

LAYER_NAME = "layer1"
TEXT_LAYER = "textLayer"

# dxfのversion指定
doc = ezdxf.new(ezdxf.const.DXF2018, setup=True)
# 日本語フォントの設定(.ttfのみ使用可能)
doc.styles.add(FONT_NAME, font=FONT_NAME+'.ttf')

msp = doc.modelspace()

doc.layers.new(name=LAYER_NAME, dxfattribs={'lineweight': '20'})
doc.layers.new(name=TEXT_LAYER, dxfattribs={})

room = items.Room(0, 0, 15, 10, "最初の部屋")
room.draw(msp, LAYER_NAME)

# 保存
path = 'square'
doc.saveas(path+'.dxf')

# 画像で保存
matplotlib.qsave(msp, path + '.png', size_inches=[1.6, 0.9])
