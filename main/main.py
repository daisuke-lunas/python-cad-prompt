import ezdxf
from ezdxf.layouts import Modelspace
from ezdxf.entities.textstyle import Textstyle
from model import items
from ezdxf.addons.drawing import matplotlib
from settings import FONT_NAME, FONT_FILE_NAME

LAYER_NAME = "layer1"


def drawOuterWalls(msp: Modelspace) -> None:
    left = 0
    top = 30
    right = 40
    bottom = 0

    # 上の外壁
    wall1 = items.Wall(left - 1, top+1, right+2, doorStartPos=3, doorLength=2)
    wall1.draw(msp, LAYER_NAME)

    # 左の外壁
    wall2 = items.Wall(left - 1, top+1, top+2, doorStartPos=23,
                       doorLength=5, isVertical=True)
    wall2.draw(msp, LAYER_NAME)

    # 右の外壁
    wall3 = items.Wall(right, top+1, top+2, isVertical=True,
                       doorStartPos=15, doorLength=2)
    wall3.draw(msp, LAYER_NAME)

    # 下の外壁
    wall4 = items.Wall(left - 1, bottom, right+2,
                       doorStartPos=32, doorLength=6)
    wall4.draw(msp, LAYER_NAME)

    pillars = [items.Pillar(left, top, 1), items.Pillar(right, top, 1),
               items.Pillar(left, bottom, 1), items.Pillar(right, bottom, 1)]
    for p in pillars:
        p.draw(msp, LAYER_NAME)


def drawRooms(msp: Modelspace) -> None:
    rooms = [items.Room(0, 10, 15, 10, "搬出入口"),
             items.Room(0, 30, 15, 20, "加工場"),
             items.Room(15, 30, 10, 10, "保管庫"),
             items.Room(25, 30, 10, 10, "品質管理室"),
             items.Room(35, 30, 5, 10, "倉庫"),
             items.Room(15, 20, 20, 10, "梱包ライン"),
             items.Room(35, 20, 5, 10, "事務室"),
             items.Room(15, 10, 15, 10, "製品出荷室"),
             items.Room(30, 10, 10, 10, "玄関・応接室")]

    for room in rooms:
        room.draw(msp, LAYER_NAME)


def drawPillars(msp: Modelspace) -> None:
    pillars = [items.Pillar(15, 10, 0.5),
               items.Pillar(30, 10, 0.5),
               items.Pillar(35, 10, 0.5),
               items.Pillar(15, 20, 0.5),
               items.Pillar(35, 20, 0.5),]
    for p in pillars:
        p.draw(msp, LAYER_NAME)


def drawInnerWalls(msp: Modelspace) -> None:
    horizontalWalls = [
        items.Wall(0, 10.25, 15, 2, 11, isThin=True),
        items.Wall(15, 10.25, 15, 5, 5, isThin=True),
        items.Wall(30, 10.25, 5, isThin=True),
        items.Wall(35, 10.25, 5, 3, 1.2, isThin=True),
        items.Wall(15, 20.25, 10, 2.5, 5, isThin=True),
        items.Wall(25, 20.25, 10, 2.5, 5, isThin=True),
        items.Wall(35, 20.25, 5, 3, 1.2, isThin=True),]
    verticalWalls = [
        items.Wall(14.75, 10, 10, 2, 6, isVertical=True, isThin=True),
        items.Wall(14.75, 20, 10, 2.5, 5, isVertical=True, isThin=True),
        items.Wall(14.75, 30, 10, 2, 6, isVertical=True, isThin=True),
        items.Wall(24.75, 30, 10, isVertical=True, isThin=True),
        items.Wall(29.75, 10, 10, 2, 2, isVertical=True, isThin=True),
        items.Wall(34.75, 30, 10, isVertical=True, isThin=True),
        items.Wall(34.75, 20, 10, 8, 1.2, isVertical=True, isThin=True),]

    for w in horizontalWalls + verticalWalls:
        w.draw(msp, LAYER_NAME)


# ------------#

# dxfのversion指定
doc = ezdxf.new(ezdxf.const.DXF2018)
# 日本語フォントの設定(.ttfのみ使用可能)
doc.styles.add(name=FONT_NAME, font=FONT_FILE_NAME+'.ttf')

space = doc.modelspace()

# 今は使ってないので一旦コメント
# doc.layers.new(name=LAYER_NAME, dxfattribs={'lineweight': '20'})


drawOuterWalls(space)
drawRooms(space)
drawInnerWalls(space)
drawPillars(space)


# 保存
path = 'sample-rooms'
doc.saveas(path+'.dxf')

# 画像で保存
matplotlib.qsave(space, path + '.png', size_inches=[2.4, 1.35])
