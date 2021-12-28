# Noise detection AI

騒音検知 AI 作ります．

開発状況は気が向き次第ここに記入します．

## インストール

- FFmpeg のインストール [参考](https://nagaragawa-r.com/download-install-pass-ffmpeg/)

## webサイト

- [やさしい AI の始め方](https://poncotuki.com/ai-ml/ai-voicedlml/)
- [ディープラーニングで音声分類](https://qiita.com/cvusk/items/61cdbce80785eaf28349#augmentation)
- [音声分類をいろいろなモデルや特徴量でやってみた](https://qiita.com/kshina76/items/5686923dee2889beba7c)
- (予定)[Pythonの音声処理ライブラリ【LibROSA】で音声読み込み⇒スペクトログラム変換・表示⇒位相推定して音声復元](https://qiita.com/lilacs/items/a331a8933ec135f63ab1)
- [Pythonの並列処理を理解したい［マルチスレッド編］](https://zenn.dev/ryo_kawamata/articles/python-concurrent-thread)
- [機械学習を用いてリアルタイムにギター のコードを分類してみた](https://qiita.com/ha161553/items/80f3056544a3d4ae3352)

### データ

[ESC-50](https://github.com/karolpiczak/ESC-50)

#### 学習データ

- dog ラベル付いたデータ 30 個
- それ以外のラベル付いたデータ 100 個

#### 予測データ

- dog ラベル付いたデータ 8 個
- それ以外のラベル付いたデータ 7 個

#### 相対パス

学習データ（dog）：`./testes/train/dog/*.wav`
学習データ（other）：`./testes/train/other/*.wav`
予測データ（dog）：`./testes/testes/dog/*.wav`
予測データ（other）：`./testes/testes/other/*.wav`

### 結果

**正答率**：**80%** 現在はもっと高いです

|     filename     | 正解  | 予測  | 結果 |
| :--------------: | :---: | :---: | :--: |
| 4-207124-A-0.wav |  dog  |  dog  |  ○   |
|  5-9032-A-0.wav  |  dog  |  dog  |  ○   |
| 5-203128-A-0.wav |  dog  |  dog  |  ○   |
| 5-208030-A-0.wav |  dog  |  dog  |  ○   |
| 5-212454-A-0.wav |  dog  | other |  ×   |
| 5-213855-A-0.wav |  dog  | other |  ×   |
| 5-217158-A-0.wav |  dog  |  dog  |  ○   |
| 5-231762-A-0.wav |  dog  | other |  ×   |
| 1-26806-A-1.wav  | other | other |  ○   |
| 1-27165-A-35.wav | other | other |  ○   |
| 1-27166-A-35.wav | other | other |  ○   |
| 1-27403-A-28.wav | other | other |  ○   |
| 1-27405-A-28.wav | other | other |  ○   |
| 1-27724-A-1.wav  | other | other |  ○   |
| 1-28005-A-18.wav | other | other |  ○   |

## 本番への組み込み

### 使用データ

- [ESC-50](https://github.com/karolpiczak/ESC-50)

#### tmp

録音 -> 保存 -> 読み込み -> 予測やと無理やった．
保存と読み込みを消して直接inputから予測する．
学習データも全部inputに変換してやる．

予測の精度はともかくリアルタイムでのAI判断できた．
学習データをわざわざ作り直さなくてもrealtime.pyからAIちゃんに渡すデータの処理ちゃんとしたら判断できた（ちゃんと判断できてるかは不明...できてなさそうw）

#### Animals

- Dog -> other
- Rooster -> other
- Pig -> other
- Cow -> other
- Frog -> other
- Cat -> other
- Hen -> other
- Insects(flying) -> other
- Sheep -> other
- Crow -> other

#### Natural soundscapes & water sounds

- Rain -> other
- Sea waves -> other
- Cracking fire -> other
- Crickets -> other
- Chirping birds -> other
- Wind -> other
- Pouring water -> other
- Toilet flush -> other
- Thunderstorm -> other

#### Human, non-speech sounds

- Crying baby -> other
- Sneezing -> other
- Clapping -> other
- Breathing -> other
- Coughing -> other
- Footsteps -> other
- Laughing -> other
- Brushing teeth -> other
- Snoring -> Snoring
- Drinking, sipping -> other

#### Interior/domestic sounds

- Door knock -> other
- Mouse click -> other
- Keyboard typing -> other
- Door, wood creaks -> other
- Can opening -> other
- Washing machine -> Washing machine
- Vacuum cleaner -> Vacuum cleaner
- Clock tick -> other
- Glass breaking -> other

#### Exterior/urban noises

- Helicopter -> Helicopter
- Chainsaw -> Chainsaw
- Siren -> other
- Car horn -> other
- Engine -> Engine
- Train -> other
- Church bells -> other
- Airplane -> Airplane
- Fireworks -> other
- Hand saw -> other

other と ラベル付いてるやつで分けて判定

## その他

1. `AI_save1.py` で学習して，学習結果・前処理したデータを保存する．

2. `AI_open1.py` で学習結果から予測を行う．

学習結果とかは `pickle` ディレクトリ内に保存した．学習結果自体はすでに保存済み．予測自体は `AI_open1.py` の実行でできる．感覚的には学習に 20 秒くらいかかった．
