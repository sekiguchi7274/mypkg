# SPDX-FileCopyrightText: 2025 Sekiguchi Tomoyuki
# SPDX-License-Identifier: BSD-3-Clause
import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    solar_flare_talker = launch_ros.actions.Node(
         package='mypkg',      #パッケージの名前を指定
         executable='solar_flare_talker',  #実行するファイルの指定
         )
    listener = launch_ros.actions.Node(
         package='mypkg',
         executable='listener',
         output='screen'        #ログを端末に出すための設定
       )
    return launch.LaunchDescription([solar_flare_talker, listener])
