# SPDX-FileCopyrightText: 2025 Sekiguchi Tomoyuki
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        self.sub = self.create_subscription(String, "cla", self.cb, 10)
    
    def cb(self, msg):
        self.get_logger().info(f"Published solar flare class type: {msg.data}")
        

def main():
    rclpy.init()
    node = Listener()
    rclpy.spin(node)
if __name__ == '__main__':
    main()
