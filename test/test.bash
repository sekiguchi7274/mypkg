#!/usr/bin/bash
# SPDX-FileCopyrightText: 2025 Sekiguchi Tomoyuki
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 30 ros2 run mypkg solar_flare_talker | ros2 topic echo /cla | grep 'X'
