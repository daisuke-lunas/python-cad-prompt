import ezdxf
from model import items

LAYER_NAME = "layer1"
TEXT_LAYER = "textLayer"
# dxfのversion指定
doc = ezdxf.new(ezdxf.const.DXF2018, setup=True)

doc.layers.new(name=LAYER_NAME, dxfattribs={'lineweight': '20'})
doc.layers.new(name=TEXT_LAYER, dxfattribs={})

msp = doc.modelspace()

room = items.Room(0, 0, 150, 75, "first room!")
room.draw(msp, LAYER_NAME)

# 保存
doc.saveas('square.dxf')
