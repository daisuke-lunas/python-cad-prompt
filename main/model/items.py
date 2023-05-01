from ezdxf.layouts import Modelspace
from ezdxf.enums import TextEntityAlignment
from ezdxf.entities.textstyle import Textstyle
from settings import FONT_FILE_NAME


class Room:
    # 線で囲われた四角いもの
    # 始点と幅/高さを持つ
    left: float
    top: float
    height: float
    width: float
    name: str
    # 名前を持つので、真ん中？に文字列を表記できるように

    def __init__(self, left: float, top: float, width: float, height: float, name: str) -> None:
        self.left = left
        self.top = top
        self.height = height
        self.width = width
        self.name = name

    def draw(self, msp: Modelspace, layer: str) -> None:
        points = [(self.left, self.top),
                  (self.left + self.width, self.top),
                  (self.left + self.width, self.top - self.height),
                  (self.left, self.top - self.height)]
        ply = msp.add_polyline2d(points=points,
                                 format="xy",
                                 close=True,
                                 dxfattribs={'layer': layer,
                                             'color': 3,
                                             'linetype': "Continuous",
                                             })
        # hatch = msp.add_hatch(color=3)
        # hatch.set_pattern_fill("ANSI34", scale=0.3)
        # hatch.paths.add_polyline_path(
        # path_vertices=ply.points(),
        # is_closed=True
        # )
        msp.add_text(text=self.name,
                     height=self.height/14,
                     dxfattribs={'layer': layer, 'style': FONT_FILE_NAME}).set_placement(
            (self.left + self.width/2, self.top - self.height/2),
            align=TextEntityAlignment.CENTER
        )


class Wall:
    # こちらも線で囲われた四角いもの
    left: float
    top: float
    # 構造は部屋と同じ。ただ、おきたい位置に対しちょっと外が始点(それは使う側で対処)
    length: float  # 壁は長さ。縦横どちらにも使うので。
    isVertical: bool  # 縦か横か

    # ドアの位置と幅
    doorStartPos: float
    doorLength: float

    # 厚い壁と薄い壁が存在する（固定値）
    isThin: bool
    _thinWidth = 0.5
    _thickWidth = 1

    def __init__(self, left: float, top: float, length: float,
                 doorStartPos=0.0, doorLength=0.0, isVertical=False, isThin=False) -> None:
        self.left = left
        self.top = top
        self.length = length
        self.doorStartPos = doorStartPos
        self.doorLength = doorLength
        self.isVertical = isVertical
        self.isThin = isThin

    def draw(self, msp: Modelspace, layer: str) -> None:
        width = self._thinWidth if self.isThin else self._thickWidth

        rightX = self.left + width if self.isVertical else self.left + self.length
        bottomY = self.top - self.length if self.isVertical else self.top - width

        points = [(self.left, self.top), (rightX, self.top),
                  (rightX, bottomY), (self.left, bottomY)]
        ply = msp.add_polyline2d(points=points,
                                 format="xy",
                                 close=True,
                                 dxfattribs={'layer': layer,
                                             'color': 7,
                                             'linetype': "Continuous",
                                             })
        hatch = msp.add_hatch(color=3)
        hatch.set_pattern_fill("ANSI37", scale=0.3)
        hatch.paths.add_polyline_path(
            path_vertices=ply.points(),
            is_closed=True
        )

        if self.doorLength > 0:
            # ドアを描く
            doorLeftX = self.left if self.isVertical else self.left + self.doorStartPos
            doorTopY = self.top - self.doorStartPos if self.isVertical else self.top
            doorRightX = self.left + width if self.isVertical else doorLeftX + self.doorLength
            doorBottomY = doorTopY - self.doorLength if self.isVertical else self.top - width

            doorPoints = [(doorLeftX, doorTopY), (doorRightX, doorTopY),
                          (doorRightX, doorBottomY), (doorLeftX, doorBottomY)]
            ply2 = msp.add_polyline2d(points=doorPoints,
                                      format="xy",
                                      close=True,
                                      dxfattribs={'layer': layer,
                                                  'color': 4,
                                                  'linetype': "Continuous",
                                                  })
            hatch2 = msp.add_hatch(color=9)
            hatch2.paths.add_polyline_path(
                path_vertices=ply2.points(),
                is_closed=True
            )


class Pillar:
    x: float
    y: float
    radius: float
    # 点と、太さ（ピクセル指定）を持つ
    # その点を中心に、正方形に広がる

    def __init__(self, x, y, r) -> None:
        self.x = x
        self.y = y
        self.radius = r

    def draw(self, msp: Modelspace, layer: str) -> None:
        points = [(self.x - self.radius, self.y + self.radius),
                  (self.x + self.radius, self.y + self.radius),
                  (self.x + self.radius, self.y - self.radius),
                  (self.x - self.radius, self.y - self.radius),]
        ply = msp.add_polyline2d(points=points,
                                 format="xy",
                                 close=True,
                                 dxfattribs={'layer': layer,
                                             'color': 7,
                                             'linetype': "Continuous",
                                             })
        hatch = msp.add_hatch(color=7)
        hatch.paths.add_polyline_path(
            path_vertices=ply.points(),
            is_closed=True
        )
