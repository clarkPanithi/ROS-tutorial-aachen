#!/usr/bin/env python3
import rclpy

def main():
    rclpy.init()
    node = rclpy.create_node('firstnode')
    rclpy.spin(node)
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()
# This is a simple ROS2 node that does nothing but spin.
# It is a good starting point for creating your own nodes.
# The node is created using the rclpy library, which is the Python client library for ROS2.
   
if __name__ == '__main__':
    main()