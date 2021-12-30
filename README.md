# G2021-hirakataA

ゴールデンダンス 2021・枚方 A 班

聴覚障がい者のための骨伝導を用いたコミュニケーション機器の開発～医療・看護・介護での活用～

リアルタイムでイヤホンから取得した音を，周波数ごとに増幅するツールです．

## デモ

このリポジトリには 2 つのツールが入っています．1 つ目`main.py`はイヤホンの周波数特性を測定するためのツールです．

![demo](https://github.com/maikataA/G2021-hirakataA/blob/main/Img/1.gif)

2 つ目`realtime.py`はイヤホンから取り込んだ音声を周波数ごと（10 種類・10 段階）に増幅するためのツールです．

![demo](https://github.com/maikataA/G2021-hirakataA/blob/main/Img/4.png)

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

※ **1. オーディオデバイスの変更**，**2. 測定**は音質を良くしたいという方向けです．そのままでかまわない場合は**3. device index の確認・realtime.pyの編集**まで飛ばしていただいて問題ありません．

### 1. オーディオデバイスの変更

**設定** -> **サウンド** -> **再生** -> **CABLE Input**を選択．

**設定** -> **サウンド** -> **録音** -> **CABLE Output**を選択．

デフォルトでは上記の設定では音が聞こえない場合があります．測定後は元に戻すのでどちらでもかまいませんが，測定時の音を聞きたい場合は以下の設定をします．

**設定** -> **サウンド** -> **再生** -> **CABLE Output** -> **プロパティ** -> **聴く** -> **このデバイスを聴く**にチェック & **このデバイスを使用して再生する**で普段使用しているデバイスを選択（こちらは**既定の再生デバイス**で問題ないかもしれません）

![demo](https://github.com/maikataA/G2021-hirakataA/blob/main/Img/2.png)

### 2. 測定

本ツールを初めて使用する場合や，使用するイヤホンを変更した場合に行って下さい．本工程を行わずにツールを使用する事は可能ですが，より良い音質のためには測定が必要と思われます．

G2021-hirakataA のディレクトリに移動し，以下のコードをコマンドラインで実行して下さい．

```cmd
$ python main.py
```

ここからは2つの場合に分かれます．

****

1つめは，音質の良いイヤホンを持っているが，音質の悪いイヤホンで本ツールを使用する場合です．その場合は，音質の良いイヤホンで**校正イヤホン測定**をどちらかの耳で測定して下さい．また，音質の悪いイヤホンで**百均イヤホン測定**を両耳で測定して下さい．保存するファイル名が保存時のデフォルト名以外であればファイルパスを変更する必要が発生します．そのため，ファイル名はデフォルトのままをオススメします．

`realtime.py`を実行した際は**百均イヤホン**のチェックボックスにチェックを入れてご使用下さい．

****

2つめは，上記の場合以外です．その場合は，使用するイヤホンで**校正イヤホン**をどちらかの耳で使用して下さい．保存するファイル名が保存時のデフォルト名以外であればファイルパスを変更する必要が発生します．そのため，ファイル名はデフォルトのままをオススメします．

`realtime.py`を実行した際は**百均イヤホン**のチェックボックスにチェックを入れずにご使用下さい．

****

### 3. device index の確認・realtime.pyの編集

以下のコードを実行して下さい．

```cmd
$ python device.py
```

...ここは正直よく分かりません．適当にいじってたらできました．[このウェブサイト](https://hamataku.netlify.app/post/earphone/)を参考にして下さい．また，私の場合の変数を下に載せておきます．

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

**ON/OFF**ボタンを押すと増幅が開始されます．百均イヤホンのチェックボックス，騒音検知AI，増幅量はお好みでどうぞ．

## バージョン

- v1.0.0
- v1.1.0
- v1.2.0

詳細は[こちら](https://github.com/maikataA/G2021-hirakataA/blob/main/version_note.md)

## 参考ウェブサイト

- [python で百均イヤホンを高音質化！](https://hamataku.netlify.app/post/earphone/)
- [やさしい AI の始め方](https://poncotuki.com/ai-ml/ai-voicedlml/)
- [ディープラーニングで音声分類](https://qiita.com/cvusk/items/61cdbce80785eaf28349#augmentation)
- [音声分類をいろいろなモデルや特徴量でやってみた](https://qiita.com/kshina76/items/5686923dee2889beba7c)
- [Pythonの並列処理を理解したい［マルチスレッド編］](https://zenn.dev/ryo_kawamata/articles/python-concurrent-thread)
- [機械学習のための音声の特徴量ざっくりメモ (Librosa ,numpy)](https://qiita.com/yutalfa/items/dbd172138db60d461a56)
- [「FFmpeg」をダウンロード、インストール、パスを通す](https://nagaragawa-r.com/download-install-pass-ffmpeg/)

## 騒音検知AIに使用したデータセット

- [ESC-50](https://qiita.com/cvusk/items/61cdbce80785eaf28349#augmentation)

## ライセンス

[MIT](https://github.com/maikataA/G2021-hirakataA/blob/main/LICENSE)

## 作者

ゴールデンダンス 2021・枚方 A 班
