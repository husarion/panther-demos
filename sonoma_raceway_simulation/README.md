# Sonoma Raceway Simulation

The demo, by simulating a real Sonoma raceway, allows you to test the operation of data fusion with GPS.

## How to use

### Configuration

1. Clone this repository on your PC.

    ```bash
    git clone https://github.com/husarion/panther-demos.git
    ```

2. [OPTIONAL] If your system does not have a GPU, modify the display configuration for the simulator by editing [compose.yaml](compose.yaml). Change the setting from `gpu-display` to `cpu-display` to ensure compatibility.

### Running

1. Run demo.

    ```bash
    cd panther-demos/panther_on_sonoma/
    xhost +local:docker
    docker compose up
    ```

    *Note: This demo shouldn't be launched on a real robot.*
