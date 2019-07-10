from win32com import client as wc
import os

print('Enter your Director\'s path:')
mypath = input()
all_FileNum = 0


def Translate(level, path):
    global all_FileNum
    '''
    将一个目录下所有doc文件转成txt
    '''
    # 该目录下所有文件的名字
    files = os.listdir(path)
    for f in files:
        if (f[0] == '~' or f[0] == '.'):
            continue
        new = path + '\\\\' + f
        print(new)
        # 除去后边的.doc后缀
        tmp = new[:-4]
        # 改成txt格式
        word = wc.Dispatch('Word.Application')
        doc = word.Documents.Open(tmp)
        doc.SaveAs(tmp + '.txt', 4)
        doc.Close()
        all_FileNum = all_FileNum + 1


if __name__ == '__main__':
    Translate(1, mypath)
    print('文件总数 = ', all_FileNum)