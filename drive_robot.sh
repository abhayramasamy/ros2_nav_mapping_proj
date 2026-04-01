#!/bin/bash

TOPIC="/cmd_vel"
MSG_TYPE="geometry_msgs/msg/TwistStamped"

echo "Moving forward..."
ros2 topic pub --times 30 $TOPIC $MSG_TYPE "{header: {frame_id: 'base_link'}, twist: {linear: {x: 0.2}, angular: {z: 0.0}}}"

echo "Spinning..."
ros2 topic pub --times 30 $TOPIC $MSG_TYPE "{header: {frame_id: 'base_link'}, twist: {linear: {x: 0.0}, angular: {z: 0.8}}}"

echo "Moving forward..."
ros2 topic pub --times 30 $TOPIC $MSG_TYPE "{header: {frame_id: 'base_link'}, twist: {linear: {x: 0.2}, angular: {z: 0.0}}}"

echo "Spinning..."
ros2 topic pub --times 30 $TOPIC $MSG_TYPE "{header: {frame_id: 'base_link'}, twist: {linear: {x: 0.0}, angular: {z: 0.8}}}"

echo "Done!"
