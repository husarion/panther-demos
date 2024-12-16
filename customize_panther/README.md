# Customize Panther Robot with ROS2 and Docker

This guide explains how to customize the Panther robot using `ros2` and Docker with components from the [husarion/ros_components_description](https://github.com/husarion/ros_components_description) repository. 

## Prerequisites

Ensure you have the following installed on your system:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)
- **xhost**: (for graphical applications in Docker)

## Available Components

Components available for use can be found in the `gz_components.launch.py` file from the `husarion` repository:

- [Available Components](https://github.com/husarion/ros_components_description/blob/ros2/launch/gz_components.launch.py#L66)

Review the available components to decide which ones to use in your configuration. To learn more about each component visit the [Panther Configuration Options manual page](https://husarion.com/manuals/panther/panther-options/). 

## Steps to Customize the Panther

### 1. Allow Docker to access your X11 display for graphical output:

```bash
xhost local:docker
```

Start Docker containers with docker compose:

```bash
docker compose up
```

### 2. Configure Components

Edit the [config/components.yaml](config/components.yaml) with the desired components. Here's a sample configuration:

```yaml
components:
  - type: MAN02
    parent_link: cover_link
    xyz: 0.2 -0.2 0.0
    rpy: 0.0 0.0 0.0
    device_namespace: ur5
```

In this example:
    - `type`: MAN02: Specifies the component type.
    - `parent_link`: cover_link: Defines the parent link to attach the component.
    - `xyz`: 0.2 -0.2 0.0: Sets the position of the component.
    - `rpy`: 0.0 0.0 0.0: Sets the rotation of the component.
    - `device_namespace`: ur5: Sets the device namespace.

### 3. Apply the configuration

Use the following command to launch the configuration in the rviz2 Docker container:

```bash
docker compose exec rviz2 bash -c "source install/setup.bash && ros2 launch /ros2_ws/src/panther_ros/panther_description/launch/overwrite_robot_description.launch.py components_config_path:=/config/components.yaml"
```
