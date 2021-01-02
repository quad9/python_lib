import sys
import glob
import pandas as pd
import numpy as np
sys.path.append('../../lib')
import ntzarr

# read CSV file
file_path = glob.glob("./*.csv")

# create deta frame of pandas
df = pd.read_csv(file_path[0], encoding = 'utf-8')

# セルごとの文字列クリーニングを先にすると『NaN』が『nan』になり、
# dorpnaメソッドが効かなくなるので、不要なNaN行を先に削除処理する。
df = df.dropna(how='all').dropna(how='all', axis = 1)

print(ntzarr.pickcell(df["番号"]))
print(ntzarr.pickcell(df["番号"], "i"))