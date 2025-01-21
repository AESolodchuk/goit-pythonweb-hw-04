# File Sorting Script

This project is a Python script designed to sort files into different folders based on their file extensions. The script uses asynchronous operations to efficiently handle file I/O.

## Features

- Sorts files into folders based on their extensions.
- Supports a variety of file types including images, documents, and audio files.
- Uses asynchronous operations for efficient file handling.

## Requirements

- Python 3.7+
- `aiopath` library
- `aioshutil` library

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install aiopath aioshutil
    ```

## Usage

Run the script with the following command:
```sh
python main.py --in_folder <source-folder> --out_folder <output-folder>