# NameChanger

日本語(JPN)と干渉する簡体中国語(CHS)のファイルを日本語に変換するプログラム。

## 実行環境

- pyuthon v3.10.4
- urllib3 v1.26.14
- beautifulsoup4 v4.11.2

## ファイル説明

- `NameChanger.py`
    ファイルの前を変更するプログラム。
- `ScrapingComparisonTables.py`
    [対応表のサイト](http://gigadict.com/JxCsCode.htm)から対応表スクレイピングし、`ComparisonTable.txt`を作成する
- `ComparisonTable.txt`
    `ScrapingComparisonTables.py`で作成した対応表。
    
## 使用方法

1. `NameChanger.py`を実行する。
2. 対象のラジオボタンから変更したい対象を選択する。
![](https://raw.githubusercontent.com/22AMJ19/NameChanger/media/images/2023-06-02.png)
3. ファイルを選択すると、一つのファイルの名前を変更する。
4. フォルダを選択すると、選択したフォルダとそのフォルダの中のフォルダ・ファイルを変換する。
5. 全フォルダを選択すると、選択したフォルダとその中にあるフォルダ内部のファイルを含め、フォルダ・ファイルをすべて変更する。
6. 参照から変換したい対象を選択する。
7. 実行ボタンを押すことで変換が実行される。