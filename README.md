# solar_flare_talker


[![test](https://github.com/sekiguchi7274/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/sekiguchi7274/mypkg/actions/workflows/test.yml)


ロボットシステム学で課題2用に作成したROS2パッケージです。


このリポジトリにはNASAのDONKI APIを使用して、今日の観測された太陽フレアのクラス分類をパブリッシュするノードが含まれています。

## ROS2バージョン

- ROS2 Humble
## 太陽フレアのクラス分類について
太陽の表面で起こる大爆発である太陽フレアは発生するX線の強さによって5段階のA → B → C → M → X のクラス分類で分けられ、それぞれクラスが一つ上がるごとに太陽フレアの規模が約10倍程度強くなります。また、各クラスは1から9の番号で分割され、小数点一桁までの数値で表されます。
|クラス分類|発生頻度|影響|
|:----------|:----------|:---------|
|Xクラス|年に3回程度|Xクラスの中でも特に大きな規模の太陽フレアは、通信やGPSの不具合を起こし,社会経済活動に大きな被害を加える。|
|Mクラス|年に30回程度|地球に影響はない|
|Cクラス|年に300回程度|地球に影響はない|
|Bクラス|年に3000回程度|地球に影響はない|
|Aクラス|年に3000回以上|地球に影響はない|


※引用["新たなるハザード、「太陽フレア」を知る"より表1　執筆者:田村優作](https://www.newton-consulting.co.jp/bcmnavi/column/solar_flare.html#:~:text=%E5%A4%AA%E9%99%BD%E3%83%95%E3%83%AC%E3%82%A2%E3%81%AE%E8%A6%8F%E6%A8%A1%E3%81%AF,%E3%82%82%E3%81%9F%E3%82%89%E3%81%99%E5%8F%AF%E8%83%BD%E6%80%A7%E3%81%8C%E3%81%82%E3%82%8A%E3%81%BE%E3%81%99%E3%80%82)
## 使用例
```
$ros2 run mypkg solar_flare_talker

### 実行結果(別のターミナルでの操作) ###

$ros2 topic echo /cla
data: X1.2 M2.3 X1.1 M1.9 M5.8 M1.5
---
data: X1.2 M2.3 X1.1 M1.9 M5.8 M1.5
---
data: X1.2 M2.3 X1.1 M1.9 M5.8 M1.5
---
data: X1.2 M2.3 X1.1 M1.9 M5.8 M1.5
---
data: X1.2 M2.3 X1.1 M1.9 M5.8 M1.5
---
data: X1.2 M2.3 X1.1 M1.9 M5.8 M1.5
---
data: X1.2 M2.3 X1.1 M1.9 M5.8 M1.5
---
```
# ノード
## solar_flare_talkerノード
NASAのDONKI APIを使用して、今日の観測された太陽フレアのクラス分類をパブリッシュするノード。

### Published Topics
- cla(std_msgs.msg/Stirng)
  - 今日観測された太陽フレアのクラス分類

## listenerノード
テスト用ノード。
# テスト環境
- Ubuntu 22.04.5 LTS
# 参考資料
- [NASA(nasapy)のpythonライブラリを使ってみた](https://web3.hide.ac/articles/DJ_LTtilh)
- [Markdown記法 チートシート](https://qiita.com/Qiita/items/c686397e4a0f4f11683d)
- [datetime --- 基本的な日付と時間の型](https://docs.python.org/ja/3.13/library/datetime.html)
- [新たなハザード、「太陽フレア」を知る](https://www.newton-consulting.co.jp/bcmnavi/column/solar_flare.html#:~:text=%E5%A4%AA%E9%99%BD%E3%83%95%E3%83%AC%E3%82%A2%E3%81%AE%E8%A6%8F%E6%A8%A1%E3%81%AF,%E3%82%82%E3%81%9F%E3%82%89%E3%81%99%E5%8F%AF%E8%83%BD%E6%80%A7%E3%81%8C%E3%81%82%E3%82%8A%E3%81%BE%E3%81%99%E3%80%82)
- [太陽風を起こす3つの太陽活動-天空の神秘オーロラ](https://auroranavi.com/aurora/solar-activity.html#:~:text=%E3%83%95%E3%83%AC%E3%82%A2%E3%81%AE%E8%A6%8F%E6%A8%A1%E3%81%AF%E3%80%81%E6%94%BE%E5%87%BA,%E5%80%8D%E3%81%AE%E8%A6%8F%E6%A8%A1%E3%81%A8%E3%81%AA%E3%82%8A%E3%81%BE%E3%81%99%E3%80%82)
- [4-3 太陽フレア発生予測　情報通信研究機構](https://www.nict.go.jp/publication/shuppan/kihou-journal/houkoku67-1_HTML/2021S-04-03.pdf)
# 権利関係
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。


© 2025 Tomoyuki Sekiguchi
