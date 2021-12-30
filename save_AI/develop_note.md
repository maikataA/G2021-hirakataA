# Noise detection AI

ここは騒音検知AIの詳細ページです．

## 予測スコア

学習データ9割に対して，テストデータは1割です．以下の正解率はテストデータに対する正解率です．

予測正解率：**94.375%**

## データセット

- [ESC-50](https://github.com/karolpiczak/ESC-50)

## データの分類

### ESC-50

| Animals | Natural soundscapes & water sounds  -> other | Human, non-speech sounds | Interior/domestic sounds | Exterior/urban noises |
| :--- | :--- | :--- | :--- | :--- |
| Dog -> other | Rain -> other | Crying baby -> other | Door knock -> other | Helicopter -> Helicopter|
| Rooster -> other | Sea waves -> other | Sneezing -> other | Mouse click -> other | Chainsaw -> chainsaw |
| Pig -> other | Crackling fire -> other | Clapping -> other | Keyboard typing -> other | Siren -> other |
| Cow -> other | Crickets -> other | Breathing -> other | Door, wood creaks -> other | Car horn -> other |
| Frog -> other | Chirping birds -> other | Coughing -> other | Can opening -> other | Engine -> engine |
| Cat | Water drops | Footsteps | Washing machine -> washing_machine | Train -> other |
| Hen -> other | Wind -> other | Laughing -> other | Vacuum cleaner -> vacuum_cleaner | Church bells -> other |
| Insects (flying) -> other | Pouring water -> other | Brushing teeth -> other | Clock alarm -> other | Airplane -> airplane |
| Sheep -> other | Toilet flush -> other | Snoring -> snoring | Clock tick -> other | Fireworks -> other |
| Crow -> other | Thunderstorm -> other | Drinking, sipping -> other | Glass breaking -> other | Hand saw -> other |


## 参考ウェブサイト

- [やさしい AI の始め方](https://poncotuki.com/ai-ml/ai-voicedlml/)
- [ディープラーニングで音声分類](https://qiita.com/cvusk/items/61cdbce80785eaf28349#augmentation)
- [音声分類をいろいろなモデルや特徴量でやってみた](https://qiita.com/kshina76/items/5686923dee2889beba7c)
- [Pythonの並列処理を理解したい［マルチスレッド編］](https://zenn.dev/ryo_kawamata/articles/python-concurrent-thread)
- [機械学習のための音声の特徴量ざっくりメモ (Librosa ,numpy)](https://qiita.com/yutalfa/items/dbd172138db60d461a56)
- [「FFmpeg」をダウンロード、インストール、パスを通す](https://nagaragawa-r.com/download-install-pass-ffmpeg/)

## 実際のところ

実際にリアルタイムで使用すると，予測はほとんど外れると思われます．これは，現実で発生している様な雑音を学習時に**完全に**無視しているためです．また，realtime.pyの処理を完全に理解している訳ではないため，しっかりと音声を入力できているかも不明です．

今後は，現実で発生している雑音を考慮して学習を行うと共に，realtime.pyの処理をしっかりと理解し，対応していきたいと考えております．（一旦は完成です．）
