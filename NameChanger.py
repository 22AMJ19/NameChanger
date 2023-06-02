import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

f = open('ComparisonTable.txt', 'r', encoding='UTF-8')
data = f.read()
INTAB, OUTTAB = data.splitlines()

def check_B ():
    if (v1.get()=='B'):
        filedialog_clicked()
    else:
        dirdialog_clicked()

# フォルダ指定の関数
def dirdialog_clicked():
    iDir = os.path.abspath(os.path.dirname(__file__))
    iDirPath = filedialog.askdirectory(initialdir = iDir)
    entry1.set(iDirPath)

# ファイル指定の関数
def filedialog_clicked():
    fTyp = [("", "*.*")]
    iFile = os.path.abspath(os.path.dirname(__file__))
    iFilePath = filedialog.askopenfilename(filetype = fTyp, initialdir = iFile)
    entry1.set(iFilePath)

# 名前
def convertImage(imgPath):
    if (v1.get()=='B'): # ファイル
        # os.rename(imgPath, imgPath.translate(imgPath.maketrans(OUTTAB, INTAB))) # これだと全部変換しちゃうので/以降を変更するようにする
        dirname = os.path.dirname(imgPath)
        basename = os.path.basename(imgPath)
        os.rename(imgPath, os.path.join(dirname, basename.translate(basename.maketrans(OUTTAB, INTAB))))
        # print(basename.translate(basename.maketrans(OUTTAB, INTAB)))
    elif (v1.get()=='C'):
        renamer(imgPath)
        os.rename(imgPath, os.path.join(os.path.dirname(imgPath), os.path.basename(imgPath).translate(os.path.basename(imgPath).maketrans(OUTTAB, INTAB))))
    else: # フォルダ
        for webpf in os.listdir(imgPath):
            os.rename(os.path.join(imgPath, webpf), os.path.join(imgPath, webpf.translate(webpf.maketrans(OUTTAB, INTAB))))
            # print(imgPath + webpf)
        os.rename(imgPath, os.path.join(os.path.dirname(imgPath), os.path.basename(imgPath).translate(os.path.basename(imgPath).maketrans(OUTTAB, INTAB))))
        # print (os.path.basename(imgPath))

#全フォルダ時の再帰処理用
def renamer (imgPath):
    for webpf in os.listdir(imgPath):
        if (os.path.isdir(os.path.join(imgPath, webpf))):
            renamer(os.path.join(imgPath, webpf))
        os.rename(os.path.join(imgPath, webpf), os.path.join(imgPath, webpf.translate(webpf.maketrans(OUTTAB, INTAB))))
        # print(imgPath + webpf)
    # os.rename(imgPath, os.path.join(os.path.dirname(imgPath), os.path.basename(imgPath).translate(os.path.basename(imgPath).maketrans(OUTTAB, INTAB))))
   

# 実行ボタン押下時の実行関数
def conductMain():
    dirPath = entry1.get()
    convertImage(dirPath)
    if dirPath:
        messagebox.showinfo("info", "完了しました")
    else:
        messagebox.showerror("error", "パスの指定がありません。")

if __name__ == "__main__":

    # rootの作成
    root = Tk()
    root.title("name changer")

    # Frame1の作成
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid(row=0, column=1, sticky=E)

    # 「フォルダ参照」ラベルの作成
    IDirLabel = ttk.Label(frame1, text="参照＞＞", padding=(5, 2))
    IDirLabel.pack(side=LEFT)

    # 「フォルダ参照」エントリーの作成
    entry1 = StringVar()
    IDirEntry = ttk.Entry(frame1, textvariable=entry1, width=30)
    IDirEntry.pack(side=LEFT)

    
    # Frame2の作成
    frame2 = ttk.Frame(root, padding=10)
    frame2.grid(row=1, column=1)

    label_frame = ttk.Labelframe(
        frame2,
        text='対象',
        padding=(10),
        style='My.TLabelframe')

    # Radiobutton 1
    v1 = StringVar()
    rb1 = ttk.Radiobutton(
        label_frame,
        text='フォルダ',
        value='A',
        variable=v1)

    # Radiobutton 2
    rb2 = ttk.Radiobutton(
        label_frame,
        text='ファイル',
        value='B',
        variable=v1)
    
    rb3 = ttk.Radiobutton(
        label_frame,
        text='全フォルダ',
        value='C',
        variable=v1)

    IDirButton = ttk.Button(frame1, text="参照", command=check_B)
    IDirButton.pack(side=LEFT)

    label_frame.grid(row=0, column=1)
    rb1.grid(row=0, column=1) # LabelFrame
    rb2.grid(row=0, column=0) # LabelFrame
    rb3.grid(row=0, column=2)

    # Frame3の作成
    frame3 = ttk.Frame(root, padding=10)
    frame3.grid(row=5,column=1)

    # 実行ボタンの設置
    button1 = ttk.Button(frame3, text="実行", command=conductMain)
    button1.pack(fill = "x", padx=30, side = "left")

    # print(INTAB + "\n" + OUTTAB)

    root.mainloop()