from ezdxf.layouts import Modelspace
from ezdxf.enums import TextEntityAlignment


class Room:
    # 線で囲われた四角いもの
    # 始点と幅/高さを持つ
    left: int
    top: int
    height: int
    width: int
    name: str
    # 名前を持つので、真ん中？に文字列を表記できるように

    def __init__(self, left: int, top: int, height: int, width: int, name: str) -> None:
        self.left = left
        self.top = top
        self.height = height
        self.width = width
        self.name = name

    def draw(self, msp: Modelspace, layer: str) -> None:
        points = [(self.left, self.top),
                  (self.left + self.width, self.top),
                  (self.left + self.width, self.top + self.height),
                  (self.left, self.top + self.height)]
        ply = msp.add_polyline2d(points=points,
                                 format="xy",
                                 close=True,
                                 dxfattribs={'layer': layer,
                                             'color': 3,
                                             'linetype': "Continuous",
                                             })
        hatch = msp.add_hatch(color=3)
        hatch.set_pattern_fill("GOST_WOOD", scale=2.0)
        hatch.paths.add_polyline_path(
            path_vertices=ply.points(),
            is_closed=True
        )
        msp.add_text(text=self.name,
                     height=5,
                     dxfattribs={'layer': layer, 'style': "OpenSans-Bold"}).set_placement(
            ((self.left + self.width)/2, (self.top + self.height)/2),
            align=TextEntityAlignment.CENTER
        )


class Wall:
    # こちらも線で囲われた四角いもの
    left: int
    top: int
    # 構造は部屋と同じ。ただ、おきたい位置に対しちょっと外が始点(それは使う側で対処)
    length: int  # 壁は長さ。縦横どちらにも使うので。

    # 暑い壁と薄い壁が存在する（固定値でいいと思う）
    _thinWidth = 5
    _thickWidth = 10

    def __init__(self, left, top, length) -> None:
        self.left = left
        self.top = top
        self.length = length


class Pillar:
    x: int
    y: int
    radius: int
    # 点と、太さ（ピクセル指定）を持つ
    # その点を中心に、正方形に広がる

    def __init__(self, x, y, r) -> None:
        self.x = x
        self.y = y
        self.radius = r
