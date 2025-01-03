# SPDX-FileCopyrightText: 2025 Sekiguchi Tomoyuki
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import requests
import json
from datetime import datetime, timedelta

class SolarFlareTalker(Node):
    def __init__(self):
        super().__init__("solar_flare_talker")
        self.pub = self.create_publisher(String, "cla", 10)
        self.create_timer(5, self.cb)
        self.api_key = 'qguM24OrI2LaM6KWnc9xMF1u0iwcaHqg2JsvNyXH'
        self.url = f'https://api.nasa.gov/DONKI/FLR?startDate={self.get_start_date()}&endDate={self.get_end_date()}&api_key={self.api_key}'
    def get_start_date(self):
        return (datetime.now() - timedelta(days = 1)).strftime('%Y-%m-%d')
    
    def get_end_date(self):
        return datetime.now().strftime('%Y-%m-%d')

    def cb(self):
        response = requests.get(self.url)
        response.raise_for_status()
        solar_flares = response.json()
        class_types = [flare['classType'] for flare in solar_flares]
        msg = String()
        msg.data = ' '.join(class_types) if class_types else 'No solar flares'
        self.pub.publish(msg)
        self.get_logger().info(f'Published solar flare class types: {msg.data}')

        
def main():
    rclpy.init()
    node = SolarFlareTalker()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
