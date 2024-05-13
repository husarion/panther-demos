# panther-demos

Docker-based demo setups for Panther

## lsc16

Panther with LSLDIAR C16 visualized in Foxglove.

| Component type  | Hardware model | Docker image                                                                                                                                                                                                         |
| --------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LiDAR           | Ouster OS1 64  | Built locally                                                                                                                                                                                                        |
| Foxglove        | -              | [foxglove:1.84.0-20240119](https://hub.docker.com/layers/husarion/foxglove/1.84.0-20240119/images/sha256-ddd1041e3a8d884930dc595bb98673cb78e8263dafffcc8c24382d7db616cd03?context=explore)                           |
| Foxglove bridge | -              | [foxglove-bridge:humble-0.7.4-20240320](https://hub.docker.com/layers/husarion/foxglove-bridge/humble-0.7.4-20240320/images/sha256-0ffb640b86f3ca4f641fdb5076673a2a3ad9c3c2c220808e0216df5e200c542c?context=explore) |

## ouster_luxonis

Panther with Ouster LiDAR and Luxonis camera visualized in Foxglove.

| Component type  | Hardware model    | Docker image                                                                                                                                                                                                   |
| --------------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LiDAR           | Ouster OS1 64     | [ouster:humble-0.10.2-20230831](https://hub.docker.com/layers/husarion/ouster/humble-0.10.2-20230831/images/sha256-ae0cd563c6e46676075e1a1ef9abb887f2c57d8a10d29fb8d18eef8ef20546f0?context=explore)           |
| Camera          | Luxonis OAK-1 PoE | [depthai:humble-2.7.4-20230830](https://hub.docker.com/layers/husarion/depthai/humble-2.7.4-20230830/images/sha256-e2f01a5c7fbecae0a8a1a0f5078e1d71dcf1499dce39f994b82ac9fc5aad28aa?context=explore)           |
| Foxglove        | -                 | [foxglove:1.84.0](https://hub.docker.com/layers/husarion/foxglove/1.84.0/images/sha256-ddd1041e3a8d884930dc595bb98673cb78e8263dafffcc8c24382d7db616cd03?context=explore)                                       |
| Foxglove bridge | -                 | [foxglove-bridge:humble-add-depthAI](https://hub.docker.com/layers/husarion/foxglove-bridge/humble-add-depthAI/images/sha256-b89941f0332e0b29049db0eb78ad732dfeadd7c42d94d5b0c7cbb87f3a24088d?context=explore) |

## How to use

### Configuration

1. Connect to the Panther's WiFi network, and open SSH on the NUC.
  
    ```bash
    ssh husarion@10.15.20.3
    ```

1. Clone this repository.

    ```bash
    git clone https://github.com/husarion/panther-demos.git
    ```

1. [OPTIONAL] Provide custom network configuration in the [net.env](../net.env) file.

### Running

1. Run demo.

   1. Go to the demo directory of your choice

        ```bash
        cd <demo_directory>
        ```

   1. Run demo with docker containers

        ```bash
        docker compose up
        ```

1. Open visualization.

   1. Using the open browser on your computer, connect to the address [`10.15.20.3:8080`](http://10.15.20.3:8080/).

   1. Click the plus sign next to the `Data source` in the left top corner, select `Open connection` and set the `WebSocket URL` to `ws://10.15.20.3:8765`, finally click `Open`.
