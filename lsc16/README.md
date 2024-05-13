# lsc16

## How to use

### Configuration

1. Clone this repository on your computer.

      ```bash
    git clone https://github.com/husarion/panther-demos.git
    ```

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

1. Run demo.

    On the Panther robot:

    ```bash
    cd lsc16
    docker compose up
    ```

1. Open visualization.

    On your computer:

    ```bash
    cd lsc16
    docker compose -f compose.rviz.yaml up
    ```

    *Note: It's recommended to establish a wired connection between the computer and the Panther robot. Communication via WiFi may result in large packets dropping.*
