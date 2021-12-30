# G2021-maikataA_py

本ページでは，ツールに追加した機能や，削除した機能，修正した箇所などを書き込んでいます．

バージョンはGitHubのtagで管理しています．

## [v1.0.0](https://github.com/maikataA/G2021-hirakataA/tree/v1.0.0)

ツールの公開

## [v1.1.0](https://github.com/maikataA/G2021-hirakataA/tree/v1.1.0)

### 機能の追加

- 百均イヤホンの音質向上させるかどうかのチェックボックスを追加

従来は，使用しているイヤホンが百均イヤホンか否かに関わらず（測定を行い），音質を向上させる動作が成されていました．本バージョンからは百均イヤホン用の音質向上をさせるか否かの設定が，チェックボックスからできるようになりました．

- `realtime.py`のスライダーを動かさなくても自動的に増幅する様に変更

従来は，`realtime.py`の**ON/OFF**ボタンを押した後，スライダーの位置を1度変更しなければ増幅が開始されませんでしたが，本バージョンからは**ON/OFF**ボタンを押した直後に増幅が開始されます．

## [v1.2.0](https://github.com/maikataA/G2021-hirakataA/tree/v1.2.0)

### 機能の追加

- 騒音検知AIを実装

データセット[ESC-50](https://qiita.com/cvusk/items/61cdbce80785eaf28349#augmentation)から独自に選別した判断基準により，AIが騒音と判断した場合，増幅量を1/3にします．本機能は**Noise AI**チェックボックスのON/OFFにより動作いたします．詳細は[こちら](https://github.com/maikataA/G2021-hirakataA/blob/main/save_AI/develop_note.md)


## [v1.2.1](https://github.com/maikataA/G2021-hirakataA/tree/v1.2.1)

### 使いやすさの向上

- GitHubのtagへの移動方法追加

`README.md`および`version_note.md`で，各バージョンをクリックすると各バージョンのページへ飛べるように変更．
