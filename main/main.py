import ezdxf
from ezdxf.enums import TextEntityAlignment

LAYER_NAME = "layer1"
TEXT_LAYER = "textLayer"
# dxfのversion指定
doc = ezdxf.new("R2018", setup=True)

doc.layers.new(name=LAYER_NAME, dxfattribs={'lineweight': '20'})
doc.layers.new(name=TEXT_LAYER, dxfattribs={'height': 20, 'font': ""})

msp = doc.modelspace()

# 四角を作成
msp.add_line(start=[0, 0], end=[100, 0], dxfattribs={'layer': LAYER_NAME})
msp.add_line(start=[0, 0], end=[0, 100], dxfattribs={'layer': LAYER_NAME})
msp.add_line(start=[100, 0], end=[100, 100], dxfattribs={'layer': LAYER_NAME})
msp.add_line(start=[0, 100], end=[100, 100], dxfattribs={'layer': LAYER_NAME})

msp.add_text(text="最初の部屋", height=0.35).set_placement(
    (50, 50),
    align=TextEntityAlignment.CENTER
)

# 保存
doc.saveas('square.dxf')
