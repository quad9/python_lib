import sys
import re
sys.path.append('../lib')
import ntzreg


# 氏名揃え　4文字揃え
def name4justify(ins):
    justifed_name = ""
    # 前後の空白を取り去ってから
    ins = ins.strip()
    # 氏名を配列として格納
    name = ins.split()
    # 条件を与えて
    res = re.search("\s", ins)
    # 作業開始
    if res == None:
        justifed_name = ins
    else:
        uji_size = len(name[0])
        mei_size = len(name[1])
        # 〓　〓 => 〓　　〓
        if uji_size == 1 and mei_size == 1:
            justifed_name = f'{name[0]}　　{name[1]}'
        # 〓　〓〓 or 〓〓　〓 or 〓　〓〓〓 or 〓〓〓　〓
        elif uji_size == 1 and mei_size == 2 or uji_size == 2 and mei_size == 1 or uji_size == 1 and mei_size == 3 or uji_size == 3 and mei_size == 1:
            justifed_name = f'{name[0]}　{name[1]}'
        # 〓〓　〓〓 or 〓〓 〓〓〓 or 〓〓〓　〓〓 or
        # 〓〓〓　〓〓〓 or 〓〓〓　〓〓〓〓 or 〓〓〓〓　〓〓〓 or other
        # elif uji_size == 2 and mei_size == 2 or uji_size == 1 and mei_size == 3 or uji_size == 3 and mei_size == 1:
        #     justifed_name = f'{name[0]}{name[1]}'
        else:
            justifed_name = f'{name[0]}{name[1]}'
        
    return justifed_name


# 氏名揃え　5文字揃え
def name5justify(ins):
    justifed_name = ""
    name = ins.split()
    uji_size = len(name[0])
    mei_size = len(name[1])
    # 〓　　　〓
    if uji_size == 1 and mei_size == 1:
        justifed_name = f'{name[0]}　　　{name[1]}'
    # 〓〓　〓〓 or 〓　〓〓〓 or 〓〓〓　〓
    elif uji_size == 2 and mei_size == 2 or uji_size == 1 and mei_size == 3 or uji_size == 3 and mei_size == 1:
        justifed_name = f'{name[0]}　{name[1]}'
    # 〓　　〓〓 or 〓〓　　〓
    elif uji_size == 1 and mei_size == 2 or uji_size == 2 and mei_size == 1:
        justifed_name = f'{name[0]}　　{name[1]}'
    # 〓〓 〓〓〓 or 〓〓〓　〓〓 or 〓〓〓　〓〓〓 or 〓〓〓　〓〓〓〓 or 〓〓〓〓　〓〓〓 or other
    else:
        justifed_name = f'{name[0]}{name[1]}'
        
    return justifed_name


# 氏名揃え　7文字揃え
def name7justify(ins):
    justifed_name = ""
    ins = ntzreg.re_cellstr(ins)
    name = ins.split()
    
    uji_size = len(name[0])
    mei_size = len(name[1])
    # 〓　　　　　〓
    if uji_size == 1 and mei_size == 1:
        justifed_name = f'{name[0]}　　　　　{name[1]}'
    # 〓　〓　〓　〓
    elif uji_size == 2 and mei_size == 2:
        justifed_name = f'{name[0][0]}　{name[0][1]}　{name[1][0]}　{name[1][1]}'
    # 〓　　　〓　〓
    elif uji_size == 1 and mei_size == 2:
        justifed_name = f'{name[0]}　　　{name[1][0]}　{name[1][1]}'
    # 〓　〓　　　〓
    elif uji_size == 2 and mei_size == 1:
        justifed_name = f'{name[0][0]}　{name[0][1]}　　　{name[1]}'
    # 〓　　　〓〓〓 or 〓〓〓　　　〓
    elif uji_size == 1 and mei_size == 3 or uji_size == 3 and mei_size == 1:
        justifed_name = f'{name[0]}　　　{name[1]}'
    # 〓　〓　〓〓〓
    elif uji_size == 2 and mei_size == 3:
        justifed_name = f'{name[0][0]}　{name[0][1]}　{name[1]}'
    # 〓〓〓　〓　〓
    elif uji_size == 3 and mei_size == 2:
        justifed_name = f'{name[0]}　{name[1][0]}　{name[1][1]}'
    # 〓〓〓　〓〓〓
    elif uji_size == 3 and mei_size == 3:
        justifed_name = f'{name[0]}　{name[1]}'
    # 〓〓〓　〓〓〓〓 or 〓〓〓〓　〓〓〓
    elif uji_size == 3 and mei_size == 4 or uji_size == 4 and mei_size == 3:
        justifed_name = f'{name[0]}{name[1]}'
    else:
        justifed_name = "例外発生"
        
    return justifed_name


# 氏名揃え　ルビ付き　4文字揃え
def name4justify_with_ruby(ins):
    justifed_name = ""
    res = re.search("\s", ins.strip())
    if res == None:
        justifed_name = ins
    else:
        name = ins.split()
        uji_size = len(name[0])
        mei_size = len(name[1])
        # 〓　〓 => 〓　　〓
        if uji_size == 1 and mei_size == 1:
            justifed_name = f"[{name[0]}/{name[2]}]　　[{name[1]}/{name[3]}]"
        # 〓　〓〓 or 〓〓　〓
        elif uji_size == 1 and mei_size == 2 or uji_size == 2 and mei_size == 1:
            justifed_name = f"[{name[0]}/{name[2]}]　[{name[1]}/{name[3]}]"
        # 〓〓　〓〓 or 〓　〓〓〓 or 〓〓〓　〓 => 〓〓〓〓
        # 〓〓 〓〓〓 or 〓〓〓　〓〓 or 〓〓〓　〓〓〓 or 〓〓〓　〓〓〓〓 or 〓〓〓〓　〓〓〓 or other
        else:
            justifed_name = f"[{name[0]}/{name[2]}][{name[1]}/{name[3]}]"

    return justifed_name


# 氏名のそれぞれの漢字にルビを付与
def each_han_with_ruby(name, ruby):
    tmp_name_with_ruby = []
    for index in range(len(name)):
        shimei = name[index].split()
        furigana = ruby[index].split()
        name_with_ruby = ""
        for num in range(len(shimei)):
            name_with_ruby += f"[{shimei[num]}/{furigana[num]}]"
        tmp_name_with_ruby.append(name_with_ruby)
    
    return tmp_name_with_ruby    


# # 氏名を5文字で揃える。写真ファイルに付ける氏名用。
# def namaezoroe(ins):
#     tmp_arr = []
#     for str in ins:
#         arr = str.split()
#         uji = arr[0]
#         mei = arr[-1]
#         uji_size = len(arr[0])
#         mei_size = len(arr[-1])
#         if uji_size == 2 and mei_size == 2:
#             tmp_arr.append(f'{arr[0]}　{arr[1]}')
#         elif uji_size == 1 and mei_size == 2 or uji_size == 2 and mei_size == 1:
#             tmp_arr.append(f'{arr[0]}　　{arr[1]}')
#         elif uji_size == 2 and mei_size == 3 or uji_size == 3 and mei_size == 2:
#             tmp_arr.append(f'{arr[0]}{arr[1]}')
#         else:
#             tmp_arr.append('')
#     return tmp_arr
