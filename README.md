# python-cad-prompt

## startup

```pip3 install 'ezdxf[draw]'```

```cd ./python-cad-prompt```

```python3 main/main.py```

## トラブルシューティング

### 画像内の日本語が文字化けする場合

[ここも参照](https://self-development.info/ipaexgothic%E3%81%AB%E3%82%88%E3%82%8Bmatplotlib%E3%81%AE%E6%97%A5%E6%9C%AC%E8%AA%9E%E5%8C%96%E3%80%90python%E3%80%91/)

1. まず ```/Users/[user-name]/.matplotlib/fontlist-v330.json``` を削除(キャッシュが悪さをする時がある)

1. ```/usr/local/lib/python3.11/site-packages/matplotlib/mpl-data/matplotlibrc``` を開く
   1. ```#font.family:``` で始まる行を探す
   1. ```font.family:  IPAexGothic``` に書き換える（行頭の#も消す）
