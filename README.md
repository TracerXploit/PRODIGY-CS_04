# Simple Keylogger

![Project Icon](icon.webp)

A basic Python-based keylogger that logs key presses and releases to a text file. Utilizes the `pynput` library to capture and record keyboard events.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [How It Works](#how-it-works)
- [Output Examples](#output-examples)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Key Logging**: Records all key presses and releases.
- **Timestamped Logs**: Each event is logged with a timestamp.
- **File Output**: Logs are stored in `key_log.txt`.
- **Stop Logging**: Press the `Esc` key to stop the keylogger.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/simple-keylogger.git
    cd simple-keylogger
    ```

2. **Install dependencies:**

    ```bash
    pip install pynput
    ```

## Usage

1. **Run the script:**

    ```bash
    python keylogger.py
    ```

2. **View the log file:**

   Logs will be saved to `key_log.txt` in the same directory. Press `Esc` to stop the keylogger.

## Example

```bash
$ python keylogger.py
```

## How It Works

The script captures keyboard events using the `pynput` library:

    Key Press: Logs the key pressed with a timestamp.
    Key Release: Logs the key released with a timestamp.
    Stop Logging: Press Esc to stop logging.

Logs are saved in `key_log.txt` within the directory of the script.

## Output Examples
### Key Press and Release Logs
#### Example Log Entries

``` plaintext
2024-07-27 14:35:22,345: Key pressed: a
2024-07-27 14:35:23,456: Key released: a
2024-07-27 14:35:24,567: Key pressed: b
2024-07-27 14:35:25,678: Key released: b
2024-07-27 14:35:26,789: Special key pressed: Key.esc
2024-07-27 14:35:27,890: Keylogger stopped.
```

## Contributing

Feel free to open issues or submit pull requests if you have suggestions for improvements or encounter any issues.

## License

This project is licensed under the MIT License.
