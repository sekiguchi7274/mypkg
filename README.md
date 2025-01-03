# ros2_ws


[![test](https://github.com/sekiguchi7274/ros2_ws/actions/workflows/test.yml/badge.svg)](https://github.com/sekiguchi7274/ros2_ws/actions/workflows/test.yml)


ロボットシステム学で課題2用に作成したものです。ROS2を使用しています。


ROS2を導入したことが無い方は[こちら](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson8.html#1 "ロボットシステム学第8回目")を参考にしていただくと、ROS2を導入しやすいかもしれません。
## 導入方法
# ノード
## solar_flare_talkerノード
NASAのDONKI APIを使用して、直近4回分の観測された太陽フレアのクラス分類をパブリッシュするノード。


###Published Topics

- cla(std_msgs.msg/Stirng)
  - 直近4回観測された太陽フレアのクラス分類
##listenerノード
テスト用ノード。
#テスト環境
-
