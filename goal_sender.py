import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from nav2_msgs.action import NavigateToPose
from geometry_msgs.msg import PoseStamped

class GoalSender(Node):
    def __init__(self):
        super().__init__('goal_sender')
        self._client = ActionClient(self, NavigateToPose, 'navigate_to_pose')

    def send_goal(self, x, y):
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose.header.frame_id = 'map'
        goal_msg.pose.header.stamp = self.get_clock().now().to_msg()
        goal_msg.pose.pose.position.x = x
        goal_msg.pose.pose.position.y = y
        goal_msg.pose.pose.orientation.w = 1.0

        self.get_logger().info(f'Sending goal: ({x}, {y})')
        self._client.wait_for_server()
        self._client.send_goal_async(goal_msg)

def main():
    rclpy.init()
    node = GoalSender()
    
    # Send robot to these waypoints
    waypoints = [(0.5, 0.5), (-0.5, 0.5), (0.0, 0.0)]
    
    for x, y in waypoints:
        node.send_goal(x, y)
        import time
        time.sleep(8)  # wait before sending next goal

    rclpy.shutdown()

if __name__ == '__main__':
    main()
