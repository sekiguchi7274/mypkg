# solar_flare_talker


[![test](https://github.com/sekiguchi7274/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/sekiguchi7274/mypkg/actions/workflows/test.yml)


ロボットシステム学で課題2用に作成したROS2パッケージです。

## ROS2バージョン

- ROS2 Humble
## 使用例
```
ros2 run mypkg solar_flare_talker

### 実行結果 ###

ros2 topic echo /cla
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
# 権利関係
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。


© 2025 Tomoyuki Sekiguchi
