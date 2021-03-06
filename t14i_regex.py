import sys
import jaconv
import re
import pandas as pd
import numpy as np
sys.path.append('../lib')
import t14i_string

def csv_reg(df_in):
    rows = []
    # valuesメソッドで1行ごとに文字列を整理していく。
    for row in df_in.values:
        for i, cell in enumerate(row):
            # ###########################################################
            # #####問題点　　　　　　　　　　　　　　　　　　　　　　　　　　#####
            # #####if条件式でcellの中身が空なら次に処理を促すコードにしたい。#####
            # ###########################################################
            if not isinstance(cell, str):
                if np.isnan(cell):
                    continue
            cell = str(cell)
            # 検索置換の開始。
            # ### 全角数字を半角に変換する。
            cell = jaconv.z2h(cell, kana=False, ascii=False, digit=True)
            # ### 数字の桁区切りが全角だった場合　=> 半角に変換。
            # ### こちらは『''』の前に『r』がなくてもグループ化と正規化がうまくいってる？
            cell = re.sub('(?<=\d)，(?=\d+)', '\1,\2', cell)
            # ### 句点読点を統一。通常文章バージョン
            cell = cell.replace('，', '、')  # 理科系バージョン => '、', '，'
            cell = cell.replace('．', '。')  # 理科系バージョン => '。', '．'
            # ### 全角ASCIIを半角に変換する。
            # 全角スペースを■に変換、全角ASCIIを半角に変換、■を全角スペースに戻す。
            cell = cell.replace('　', '■')
            cell = re.sub('[〜～]', '〓から〓', cell)
            cell = jaconv.z2h(cell, kana=False, ascii=True, digit=False)
            cell = cell.replace('■', '　')
            cell = cell.replace('〓から〓', '〜')
            # ### 半角カタカナを全角に変換する。
            cell = jaconv.h2z(cell)
            # ### ASCIIの『()』『[]』を全角に変える。
            # ### 『''』の前に『r』を付けることについて、規則が全く理解できない！
            cell = re.sub('\((.+?)\)', r'（\1）', cell)
            cell = re.sub('\[(.+?)\]', r'［\1］', cell)
            # ### 時間表示の『：』を全角に変換する。
            cell = re.sub('(\d{1,2}):(\d{2})', r'\1：\2', cell)
            # ### 先頭の欧文スペースを取る
            cell = re.sub('^ ', '', cell)
            # ### 箇条書き先頭の数字周りの全角ピリオドをママ活かす。
            # ### ### 句点だった場合
            cell = re.sub('^(\d{1,3})。', r'\1．', cell, flags=re.MULTILINE)
            # ### ### Piriodの場合
            cell = re.sub('^(\d{1,3})\.\s', r'\1．', cell, flags=re.MULTILINE)
            # ### セル内改行、及び、文字列前後の不要なスペースを取り除く。
            row[i] = cell.replace('\n', '▽').strip()
        rows.append(row)
    # 元のヘッダーをここで設置しなおす。
    df = pd.DataFrame(rows, columns = df_in.columns)
    return df


def text_ins_reg(ins):
    # 検索置換の開始。
    # ### 全角数字を半角に変換する。
    ins = jaconv.z2h(ins, kana=False, ascii=False, digit=True)
    # ### 数字の桁区切りが全角だった場合　=> 半角に変換。
    ins = re.sub('^[ +]|[ +]$', '', ins)
    # ### こちらは『''』の前に『r』がなくてもグループ化と正規化がうまくいってる？
    ins = re.sub('(?<=\d)，(?=\d+)', '\1,\2', ins)
    # ### 句点読点を統一。通常文章バージョン
    ins = ins.replace('，', '、')  # 理科系バージョン => '、', '，'
    ins = ins.replace('．', '。')  # 理科系バージョン => '。', '．'
    # ### 全角ASCIIを半角に変換する。
    # 全角スペースを下駄に変換、全角ASCIIを半角に変換、下駄を全角スペースに戻す。
    ins = ins.replace('　', '〓')
    ins = jaconv.z2h(ins, kana=False, ascii=True, digit=False)
    ins = ins.replace('〓', '　')
    # ### 半角カタカナを全角に変換する。
    ins = jaconv.h2z(ins)
    # ### ASCIIの『()』『[]』を全角に変える。
    # ### 『''』の前に『r』を付けることについて、規則が全く理解できない！
    ins = re.sub('\((.+?)\)', r'（\1）', ins)
    ins = re.sub('\[(.+?)\]', r'［\1］', ins)
    # ### 時間表示の『：』を全角に変換する。
    ins = re.sub('(\d{1,2}):(\d{2})', r'\1：\2', ins)
    # ### 箇条書き先頭の数字周りの全角ピリオドをママ活かす。
    # ### ### 句点だった場合
    ins = re.sub('^(\d{1,3})。', r'\1．', ins, flags=re.MULTILINE)
    # ### ### Piriodの場合
    ins = re.sub('^(\d{1,3})\.\s', r'\1．', ins, flags=re.MULTILINE)
    # ### 問題点　文字列前後の不要なスペースを取り除けない。
    # ins = ins.strip()
    ins = re.sub('^\s+', r'', ins, flags=re.MULTILINE)
    # ##############################################
    return ins


def re_cellstr(str):
    # 文字列前後の空白を削除。
    str = str.strip()
    # セル内改行を取り除く。
    str = str.replace('\n', '▽')
    # 半角カタカナを全角に変換する。
    str = jaconv.h2z(str)

    # 全角のアスキーをASCIIへ変換（スペースもASCIIになる。）。
    # 『〜』カラ
    str = re.sub('[〜～]', '〓から〓', str)
    # 『（）』カッコ
    str = re.sub('(（)(.+?)(）)', r'〓Rカッコ〓\2〓Rカッコ〓', str)
    str = re.sub('(［)(.+?)(］)', r'〓Bカッコ〓\2〓Bカッコ〓', str)
    str = jaconv.z2h(str, kana=False, ascii=True, digit=False)
    # 『〜』カラ復号
    str = str.replace('〓から〓', '〜')
    # 『（）』カッコ復号
    str = re.sub('(〓Rカッコ〓)(.+?)(〓Rカッコ〓)', r'（\2）', str)
    str = re.sub('(〓Bカッコ〓)(.+?)(〓Bカッコ〓)', r'（\2）', str)

    # スペース（複数含む）をスペース一つに変換。
    str = re.sub("\s+", " ", str)
    # コラムが右に1列増えるのを防ぐため。
    str = re.sub(",", "/", str)
    return str


def delete_return(lines):
    ### オプション。句点以外で終わる改行コードを取り去る。
    lines = re.sub('(?<!。)\n', '', lines)
    return lines
