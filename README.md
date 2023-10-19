# Browsers Password Splitter


---

**Password Splitter** is a Python script that allows you to split a CSV file containing passwords exported from chrome/brave....etc into smaller parts, ensuring that each part is under a specified maximum size. This can be useful for importing passwords into various browsers or applications, especially when there are size limitations.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Splits a CSV file into smaller parts while ensuring each part stays below a specified maximum size (in bytes).
- Maintains the original header in each split file for better organization and import.

## Requirements

- Python 3.x installed on your system.
- A CSV file containing the passwords you want to split.

## Usage

1. Clone this repository to your local machine.

    ```bash
    git clone https://github.com/yourusername/password-splitter.git
    ```

2. Navigate to the project directory.

    ```bash
    cd password-splitter
    ```

3. Run the script.

    ```bash
    python password_splitter.py
    ```

4. Follow the prompts and provide the necessary information:
    - Enter the name of the CSV file containing passwords.
    - Specify the maximum size (in bytes) for each split file.

5. The script will create split files in the same directory as the input file.

6. Keep the split files organized as per your requirements for easy import into browsers or other applications.

## Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, please open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
