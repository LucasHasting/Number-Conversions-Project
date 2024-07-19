# Number Conversions Project

This program converts any base n number to a base m number where 1 ≤ n, m ≤ 36 and both n and m are integers. It uses logarithms to convert from base 10 to any base and it uses exponents to convert from any base to base 10.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Program-Overview](#program-overview)

## Installation

This project does not require any external pip packages. You only need [Python](https://www.python.org/downloads/) installed on your system.

### Option 1: using [git](https://git-scm.com/downloads)
1. Clone the repository:

    ```sh
    git clone https://github.com/LucasHasting/Number-Conversions-Project.git
    ```

2. Navigate to the project directory and execute the program:

    ```sh
    cd Number-Conversions-Project
    py base-converter.py
    ```
### Option 2: without git
1. Download the project as a zip file
2. [Extract the zip file](https://www.wikihow.com/Unzip-a-File)
3. In windows, the subnetting.py file can be clicked to execute

#### Run from the command line
1. Find the location of the files
2. Copy the path
3. go to the command line and run the following:
   ```sh
   cd /path/to/files
   py base-converter.py
   ```

## Usage

The program asks the user to enter an IP address and subnet mask in dotted decimal form, and will output the network address, usables range, and the broadcast address.

## Example

For an example of how to use the program, see the video here (to be posted in the future).

## Program-Overview

The [subnetting.py](https://github.com/LucasHasting/IP-Subnet-Calculator/blob/main/subnetting.py) file contains the main driver of the program and is what needs to be executed, the [functions_and_constants.py](https://github.com/LucasHasting/IP-Subnet-Calculator/blob/main/functions_and_constants.py) file contains the dictionaries used in the file. Finnaly, the file contains all the functions used in the driver.
