# ouster_luxonis

## How to use

### Configuration

1. Connect to the Panther's WiFi network, and open an SSH session on the NUC.
  
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

    ```bash
    cd panther-demos/ouster_luxonis/
    docker compose up
    ```

1. Open visualization.

   1. Using the open browser on your computer, connect to the address [`10.15.20.3:8080`](http://10.15.20.3:8080/).

   1. Click the plus sign next to the `Data source` in the left top corner, select `Open connection` and set the `WebSocket URL` to `ws://10.15.20.3:8765`, finally click `Open`.
