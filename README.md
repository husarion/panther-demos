# panther-demos

Docker-based demo setups for Panther

## lsc16

Panther with LSLIDAR C16 visualized in Rviz2.

| Component | Hardware model | Docker image                                                                                                                                                                                         |
| --------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LiDAR     | LS LIDAR C16   | Built locally                                                                                                                                                                                        |
| Rviz2     | -              | [rviz2:humble-11.2.11-20240320](https://hub.docker.com/layers/husarion/rviz2/humble-11.2.11-20240320/images/sha256-320574ab3c4c93145a21e86fe44dd93b17d25a97841e85b6a9fbbf6729a4e41f?context=explore) |

*Note: Refer to a dedicated [readme](./lsc16/README.md) file for more information on how to use the demo.*

## ouster_luxonis

Panther with Ouster LiDAR and Luxonis camera visualized in Foxglove.

| Component       | Hardware model    | Docker image                                                                                                                                                                                                   |
| --------------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LiDAR           | Ouster OS1 64     | [ouster:humble-0.10.2-20230831](https://hub.docker.com/layers/husarion/ouster/humble-0.10.2-20230831/images/sha256-ae0cd563c6e46676075e1a1ef9abb887f2c57d8a10d29fb8d18eef8ef20546f0?context=explore)           |
| Camera          | Luxonis OAK-1 PoE | [depthai:humble-2.7.4-20230830](https://hub.docker.com/layers/husarion/depthai/humble-2.7.4-20230830/images/sha256-e2f01a5c7fbecae0a8a1a0f5078e1d71dcf1499dce39f994b82ac9fc5aad28aa?context=explore)           |
| Foxglove        | -                 | [foxglove:1.84.0](https://hub.docker.com/layers/husarion/foxglove/1.84.0/images/sha256-ddd1041e3a8d884930dc595bb98673cb78e8263dafffcc8c24382d7db616cd03?context=explore)                                       |
| Foxglove bridge | -                 | [foxglove-bridge:humble-add-depthAI](https://hub.docker.com/layers/husarion/foxglove-bridge/humble-add-depthAI/images/sha256-b89941f0332e0b29049db0eb78ad732dfeadd7c42d94d5b0c7cbb87f3a24088d?context=explore) |

*Note: Refer to a dedicated [readme](./ouster_luxonis/README.md) file for more information on how to use the demo.*

## sonoma_raceway_simulation

The demo, by simulating a real Sonoma Raceway, allows you to test the operation of data fusion with GPS.

| Component        | Docker image                                                                                    |
| ---------------- | ----------------------------------------------------------------------------------------------- |
| Gazebo simulator | [panther-gazebo:humble-on-sonoma](https://hub.docker.com/r/husarion/panther-gazebo)             |
| Foxglove         | [foxglove:1.84.0](https://hub.docker.com/layers/husarion/foxglove)                              |
| Foxglove bridge  | [foxglove-bridge:humble-0.7.3-20240108](https://hub.docker.com/layers/husarion/foxglove-bridge) |

*Note: Refer to a dedicated [readme](./sonoma_raceway_simulation/README.md) file for more information on how to use the demo.*
