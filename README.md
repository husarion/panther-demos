# panther-demos

Docker-based demo setups for Panther

## lsc16

Panther with LSLIDAR C16 visualized in Rviz2.

| Component | Hardware model | Docker image                                                                                               |
|-----------|----------------|------------------------------------------------------------------------------------------------------------|
| LiDAR     | LS LIDAR C16   | Built locally                                                                                              |
| Rviz2     | -              | [rviz2:humble-11.2.11-20240320](https://hub.docker.com/r/husarion/rviz2/tags?name=humble-11.2.11-20240320) |

*Note: Refer to a dedicated [readme](./lsc16/README.md) file for more information on how to use the demo.*

## ouster_luxonis

Panther with Ouster LiDAR and Luxonis camera visualized in Foxglove.

| Component       | Hardware model    | Docker image                                                                                                         |
|-----------------|-------------------|----------------------------------------------------------------------------------------------------------------------|
| LiDAR           | Ouster OS1 64     | [ouster:humble-0.10.2-20230831](https://hub.docker.com/r/husarion/ouster/tags?name=humble-0.10.2-20230831)           |
| Camera          | Luxonis OAK-1 PoE | [depthai:humble-2.7.4-20230830](https://hub.docker.com/r/husarion/depthai/tags?name=humble-2.7.4-20230830)           |
| Foxglove        | -                 | [foxglove:1.84.0](hhttps://hub.docker.com/r/husarion/foxglove/tags?name=1.84.0)                                      |
| Foxglove bridge | -                 | [foxglove-bridge:humble-add-depthAI](https://hub.docker.com/r/husarion/foxglove-bridge/tags?name=humble-add-depthAI) |

*Note: Refer to a dedicated [readme](./ouster_luxonis/README.md) file for more information on how to use the demo.*

## sonoma_raceway_simulation

The demo, by simulating a real Sonoma Raceway, allows you to test the operation of data fusion with GPS.

| Component        | Docker image                                                                                    |
| ---------------- | ----------------------------------------------------------------------------------------------- |
| Gazebo simulator | [panther-gazebo:humble-on-sonoma](https://hub.docker.com/r/husarion/panther-gazebo)             |
| Foxglove         | [foxglove:1.84.0](https://hub.docker.com/layers/husarion/foxglove)                              |
| Foxglove bridge  | [foxglove-bridge:humble-0.7.3-20240108](https://hub.docker.com/layers/husarion/foxglove-bridge) |

*Note: Refer to a dedicated [readme](./sonoma_raceway_simulation/README.md) file for more information on how to use the demo.*

## customize_panther

The demo shows how to prepare an URDF model for Panther with different [configuraiton options](https://husarion.com/manuals/panther/panther-options/)

| Component        | Docker image                                                                                    |
| ---------------- | ----------------------------------------------------------------------------------------------- |
| Gazebo simulation & visualization in RViz | [panther-gazebo:humble-2.1.2-20241125](https://hub.docker.com/r/husarion/panther-gazebo)             |

*Note: Refer to a dedicated [readme](./customize_panther/README.md) file for more information on how to use the demo.*