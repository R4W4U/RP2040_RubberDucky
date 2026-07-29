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

After CircuitPython has been installed, copy everything except the .uf2 files onto the RP2040 Rubber Ducky.

> **Note:** You may need to use the terminal when using linux.

### Run the Sample Payload

To test the device:
1. Plug in the USB with a texteditor open and selected. Wait for the Programm to run through one time, then you can upload your code. This works even if storage mode is not working.
2. Copy `payload.txt` to the root directory of the RP2040.
3. When saving the payload.txt file the USB will automaticly start the new programm so go back to the texteditor or pull out the USB.

> **Note:** payload.txt contains the BIOS setup for lenovo thinclients.

