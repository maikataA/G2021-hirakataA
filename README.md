# G2021-maikataA_py

ゴールデンダンス 2021・枚方 A 班

聴覚障がい者のための骨伝導を用いたコミュニケーション機器の開発～医療・看護・介護での活用～

リアルタイムでイヤホンから取得した音を，周波数ごとに増幅するツールです．

## デモ

このリポジトリには 2 つのツールが入っています．1 つ目`main.py`はイヤホンの周波数特性を測定するためのツールです．

![demo](https://github.com/maikataA/G2021-hirakataA/blob/main/Img/1.gif)

2 つ目`realtime.py`はイヤホンから取り込んだ音声を周波数ごと（10 種類・10 段階）に増幅するためのツールです．

![demo](https://github.com/maikataA/G2021-hirakataA/blob/main/Img/1.png)

## 環境

以下の仮想環境でこのツールを開発しました．

```cmd
$ python -V
Python 3.6.8
```

```cmd
$ pip -V
pip 18.1
```

```cmd
$ pip freeze
> ./requirements.txt
```

## 必要事項

以下の仮想オーディオインターフェースを使用しています．

- VB-CABLE(Windows)

## 使い方

### 1. オーディオデバイスの変更

**設定** -> **サウンド** -> **再生** -> **CABLE Input**を選択．

**設定** -> **サウンド** -> **録音** -> **CABLE Output**を選択．

デフォルトでは上記の設定では音が聞こえない場合があります．測定後は元に戻すのでどちらでもかまいませんが，測定時の音を聞きたい場合は以下の設定をします．

**設定** -> **サウンド** -> **再生** -> **CABLE Output** -> **プロパティ** -> **聴く** -> **このデバイスを聴く**にチェック & **このデバイスを使用して再生する**で普段使用しているデバイスを選択（こちらは**既定の再生デバイス**で問題ないかもしれません）

![demo](https://github.com/maikataA/G2021-hirakataA/blob/main/Img/2.png)

### 2. 測定

本ツールを初めて使用する場合や，使用するイヤホンを変更した場合に行って下さい．本工程を行わずにツールを使用する事は可能ですが，より良い音質のためには測定が必要と思われます．

G2021-maikataA_py のディレクトリに移動し，以下のコードをコマンドラインで実行して下さい．

```cmd
$ python main.py
```

そして，**校正イヤホン測定**をどちらかの耳で測定して下さい．また，**百均イヤホン測定**を両耳で測定して下さい．ファイル名はデフォルトを推奨．

### 3. device index の確認・realtime.pyの編集

以下のコードを実行して下さい．

```cmd
$ python device.py
```

...ここは正直よく分かりません．適当にいじってたらできました．[このウェブサイト](https://hamataku.netlify.app/post/earphone/)を参考にして下さい．また，私の場合の変数を下記に載せておきます．

```python
class MainWindow(QtWidgets.QMainWindow):
    OUTPUT_INDEX = 5 # 編集箇所
    INPUT_INDEX = 1 # 編集箇所
    CALIBRATE_PATH = "calibrate/earphone.npy"  # 校正イヤホンのファイルパス
    LEFT_PATH = "earphone/L.npy"  # 百均イヤホン左のファイルパス
    RIGHT_PATH = "earphone/R.npy"  # 百均イヤホン右のファイルパス
    OUTPUT_FIX = 1  # 基準となる増幅倍率
```

### 4. realtime.pyの実行

オーディオデバイスの選択を使用したいイヤホンに変更した後に，以下のコマンドを実行します．

```cmd
$ python realtime.py
```

**ON/OFF**ボタンを押すと増幅が開始されます．増幅量はお好みでどうぞ．



## 参考ウェブサイト

- [python で百均イヤホンを高音質化！](https://hamataku.netlify.app/post/earphone/)

## ライセンス

[MIT](https://github.com/maikataA/G2021-hirakataA/blob/main/LICENSE)

## 作者

ゴールデンダンス 2021・枚方 A 班
