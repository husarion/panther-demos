ARG ROS_DISTRO=humble

FROM ros:${ROS_DISTRO}-ros-base

SHELL ["/bin/bash", "-c"]

WORKDIR /ros_ws

ENV DEBIAN_FRONTEND=noninteractive

RUN git clone -b C16_V3.0 https://github.com/Lslidar/Lslidar_ROS2_driver.git ./src/Lslidar_ROS2_driver

RUN apt-get update && apt-get install -y \
    ros-${ROS_DISTRO}-rmw-cyclonedds-cpp && \
  source /opt/ros/${ROS_DISTRO}/setup.bash && \
  rosdep update --rosdistro $ROS_DISTRO && \
  rosdep install -i --from-path src --rosdistro $ROS_DISTRO \
    --skip-keys message_runtime \
    --skip-keys rslidar_input -y && \
  colcon build --symlink-install && \
  apt autoremove -y && \
  apt clean && \
  rm -rf /var/lib/apt/lists/*

COPY ./ros_entrypoint.sh /
RUN chmod +x /ros_entrypoint.sh
ENTRYPOINT [ "/ros_entrypoint.sh" ]