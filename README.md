# Network Utilities using Python

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [MAC Address Changer](#mac-address-changer)
  - [Network Scanner](#network-scanner)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This repository contains two essential network utilities:

1. **MAC Address Changer**: A tool to change the MAC address of your network interfaces.
2. **Network Scanner**: A tool to scan your local network and identify connected devices.

## Features

- **MAC Address Changer**:
  - Change the MAC address of any network interface.
  - Restore the original MAC address.

- **Network Scanner**:
  - Scan the local network for active devices.
  - Display IP and MAC addresses of discovered devices.

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/angelinaturchyn/some_python.git
    cd some_python
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### MAC Address Changer

1. Run the MAC address changer script with the desired network interface:
    ```sh
    python mac_changer.py -i <interface> -m <new_mac_address>
    ```

    Example:
    ```sh
    python mac_changer.py -i eth0 -m 00:11:22:33:44:55
    ```

2. To restore the original MAC address:
    ```sh
    python mac_changer.py -i <interface> --restore
    ```

### Network Scanner

1. Run the network scanner script with the target IP range:
    ```sh
    python network_scanner.py -t <target_ip_range>
    ```

    Example:
    ```sh
    python network_scanner.py -t 192.168.1.0/24
    ```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

