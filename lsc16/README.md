# lsc16

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

**Important!** The below steps assume that [Husarion OS](https://husarion.com/software/os/) is installed on NUC and a remote desktop is started. If no, please refer to the articles:

- [Installation](https://husarion.com/software/os/installation/)
- [Remote Desktop](https://husarion.com/software/os/remote-desktop/)

1. Run demo.

    ```bash
    cd lsc16
    xhost local:root
    docker compose up
    ```

    *Note: Compose file uses locally built docker image. The building is started, once `docker compose up` command is executed.*

2. Open visualization.

   1. Using the open browser on your computer, connect to the address [`10.15.20.3:8080`](http://10.15.20.3:8080/).
   2. Login to the session if the password is requested
   3. Rviz window with a default config will be displayed.
