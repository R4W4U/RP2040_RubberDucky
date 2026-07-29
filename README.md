# RP2040 Rubber Ducky

## Getting Started

To upload the code and payload scripts to the RP2040 Rubber Ducky, the device must first be placed into **USB Storage Mode**.

### Enter USB Storage Mode

1. Press and hold both the **BOOT** and **RESET** buttons.
2. While holding the buttons, connect the device to your computer via USB.
3. Release the **BOOT** button first, then release the **RESET** button.
4. The device should appear as a removable USB storage drive.

### Install CircuitPython

Download and copy the CircuitPython UF2 file for the Raspberry Pi Pico to the device:

👉 https://circuitpython.org/board/raspberry_pi_pico/

> **Note:** The CircuitPython version used for this project is also included in the repository.

After CircuitPython has been installed, copy the contents of the ./code/ directory onto the RP2040 Rubber Ducky.

### Run the Sample Payload

To test the device:

1. Copy `sample/payloads/rickroll_macos.txt` to the root directory of the RP2040.
2. Rename the file to:

```text
payload.txt
