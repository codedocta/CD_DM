# CD_DM: Directory Manager Package
CD is for Code Docta.


The `CD_DM` project houses the `Directory Manager` package, a comprehensive set of utilities designed for efficient file and directory management, ZIP operations, and more.

## Installation

To install the `Directory Manager` package, you can use pip:

```bash
pip install CD_DM
```

## Features

The `Directory Manager` package contains the following classes, each in its separate file:

### 1. FileManager

- **File**: `fm.py`
- **Description**: Handles various file operations like reading, writing, and managing different file formats such as JSON, CSV, HTML, and Pickle.

### 2. DirectoryManager

- **File**: `dm.py`
- **Description**: Manages directory-related operations like creating, deleting, listing files, and more.

### 3. PathManager

- **File**: `pm.py`
- **Description**: Provides utilities for handling and manipulating file paths in a cross-platform manner.

### 4. FileDialogs

- **File**: `tk_file_dialog.py`
- **Description**: Facilitates file dialog operations for TKinter.


- **File**: `ps_file_dialog.py`
- **Description**: Facilitates file dialog operations for PySide6.


- **File**: `pqt_file_dialog.py`
- **Description**: Facilitates file dialog operations for PyQt6.


### 5. ZipManager

- **File**: `zipper.py`
- **Description**: Manages ZIP-related operations, including zipping and unzipping files and directories.

## Usage

Each class provides static methods that can be used directly without instantiating the class. For detailed usage, refer to the docstrings within each class file.

Example:

```python
from DirectoryManager.fm import FileManager

data = FileManager.read_json("path_to_json_file.json")
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

