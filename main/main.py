import ezdxf
from model import items
from ezdxf.addons.drawing import matplotlib
from settings import FONT_NAME

LAYER_NAME = "layer1"
TEXT_LAYER = "textLayer"


def drawWalls() -> None:
    left = 0
    top = 30
    right = 40
    bottom = 0

    # 上の外壁
    wall1 = items.Wall(left - 1, top+1, right+2)
    wall1.draw(msp, LAYER_NAME)

    # 左の外壁
    wall2 = items.Wall(left - 1, top+1, top+2, isVertical=True)
    wall2.draw(msp, LAYER_NAME)

    # 右の外壁
    wall3 = items.Wall(right, top+1, top+2, isVertical=True)
    wall3.draw(msp, LAYER_NAME)

    # 下の外壁
    wall4 = items.Wall(left - 1, bottom, right+2)
    wall4.draw(msp, LAYER_NAME)


# dxfのversion指定
doc = ezdxf.new(ezdxf.const.DXF2018, setup=True)
# 日本語フォントの設定(.ttfのみ使用可能)
doc.styles.add(FONT_NAME, font=FONT_NAME+'.ttf')

msp = doc.modelspace()

doc.layers.new(name=LAYER_NAME, dxfattribs={'lineweight': '20'})
doc.layers.new(name=TEXT_LAYER, dxfattribs={})

room = items.Room(0, 10, 15, 10, "最初の部屋")
room.draw(msp, LAYER_NAME)
drawWalls()


# 保存
path = 'square'
doc.saveas(path+'.dxf')

# 画像で保存
matplotlib.qsave(msp, path + '.png', size_inches=[2.4, 1.35])
