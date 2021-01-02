import sys
import re
import pandas as pd
import numpy as np
sys.path.append('../lib')
import ntzreg

#####################
# 同じグループの縦セルをつまんでいくコードのためのインデックス作成
###
# play_anchor_index
# 処理開始のアンカーとなる配列の作成
# セルを縦につまむ際のトリガーになるインデックスをdf["番号"]から導き出す。
def pickcell(df_column, option= "s"):
    # anchor_index = df_column
    play_anchor_index = []
    for i, num in enumerate(df_column):
        if pd.isnull(num):
            continue
        else:
            play_anchor_index.append(i)
    
    ###
    # pause_anchor_index
    # 処理ここまでと合図するアンカーの配列の作成
    if "s" in option:
        # startはインデックス番号、pauseは最初から何番目を割り出したいときはこちら。
        pause_anchor_index = [n for n in play_anchor_index[1:]]
        pause_anchor_index.append(len(df_column))
    else:
        # start, pauseのインデックス番号をきっちりと割り出したいときはこちら。
        pause_anchor_index = [n - 1 for n in play_anchor_index[1:]]
        pause_anchor_index.append(len(df_column) - 1)

    ###
    # anchor_index
    anchor_index = []
    for play, pause in zip(play_anchor_index, pause_anchor_index):
        anchor_index.append([play, pause])
    
    return anchor_index
