# lsc16

Panther with LSLIDAR C16 visualized in Rviz2.

## How to use

### Configuration

1. Connect to the Panther's WiFi network, and open an SSH session on the NUC.
  
    ```bash
    ssh husarion@10.15.20.3
    ```

1. Clone this repository on the Panther robot.

    ```bash
    git clone https://github.com/husarion/panther-demos.git
    ```

1. [OPTIONAL] Provide custom network configuration in the [net.env](../net.env) file.

### Running

**Important!** The below steps assume that [Husarion OS](https://husarion.com/software/os/) is installed on NUC. Otherwise, please follow the [installation](https://husarion.com/software/os/installation/) steps.

1. Share and access the NUC's remote desktop referring to [Remote Desktop](https://husarion.com/software/os/remote-desktop/) setup instructions.

1. Run demo.

    ```bash
    cd panther-demos/lsc16/
    docker compose up -d
    ```

    *Note: Compose file uses locally built docker image. The building is started, once `docker compose up` command is executed.*
