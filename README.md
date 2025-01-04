# solar_flare_talker


[![test](https://github.com/sekiguchi7274/ros2_ws/actions/workflows/test.yml/badge.svg)](https://github.com/sekiguchi7274/ros2_ws/actions/workflows/test.yml)


ロボットシステム学で課題2用に作成したものです。ROS2を使用しています。


[ROS2を導入するのに使用したセットアップスクリプト](https://github.com/ryuichiueda/ros2_setup_scripts)

ROS2を導入したことが無い方は[こちら](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson8.html#1 "ロボットシステム学第8回目")を参考にしていただくと、ROS2を導入しやすいかもしれません。
## ROS2バージョン

- ROS2 foxy
## 導入方法
- コマンドラインでディレクトリをクローンしたい場所で以下のコマンドを実行してください


```
git clone https://github.com/sekiguchi7274/mypkg.git
```


##使用方法
```
cd mypkg && ros2 run mypkg solar_flare_talker
```
# ノード
## solar_flare_talkerノード
NASAのDONKI APIを使用して、直近4回分の観測された太陽フレアのクラス分類をパブリッシュするノード。

### Published Topics
- cla(std_msgs.msg/Stirng)
  - 直近4回観測された太陽フレアのクラス分類

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
