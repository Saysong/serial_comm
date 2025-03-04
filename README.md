# ROS 2 USB Serial Receiver

If you send data to the serial port (e.g., using an external microcontroller like Arduino), the serial_publisher.py node will read it and publish it to the serial_data topic. 
The serial_subscriber.py node will receive and display the messages.

## Build ROS 2 package
Navigate to your workspace and build the package:
```
cd ~/ros2_ws
colcon build --packages-select serial_comm
```
Source the setup file:
```
source install/setup.bash
```
Run the serial publisher:
```
ros2 run serial_comm serial_publisher
```
Run the serial subscriber in another terminal:
```
ros2 run serial_comm serial_subscriber
```
