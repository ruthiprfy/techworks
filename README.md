# TechWorks

## Overview

TechWorks is a command-line tool designed to guide users through a step-by-step process for system recovery on Windows platforms. This program automates common recovery tasks, enabling users to restore their systems efficiently and effectively.

## Features

- Check system health using Windows System File Checker
- Restore system files with Deployment Imaging Service and Management Tool (DISM)
- Uninstall recent updates if they are causing issues
- Reset system settings to default
- Reboot the system to apply changes

## Getting Started

### Prerequisites

- A Windows operating system
- Python 3.x installed on your system

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/techworks.git
   ```
2. Navigate to the project directory:
   ```bash
   cd techworks
   ```

## Usage

Run the program using Python:

```bash
python techworks.py
```

Follow the on-screen instructions to perform each recovery step. You can choose to skip any step if you are not comfortable executing it.

## Notes

- Ensure you have administrative privileges to perform system recovery operations.
- For the `uninstall_recent_updates` step, replace `<KB_number>` with the actual KB number of the update you wish to uninstall.
- Use this tool with caution, as some operations might affect system stability.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for review.

## Authors

- [Your Name](https://github.com/yourusername)

## Acknowledgments

- Thanks to all the open-source contributors who helped make this tool possible.