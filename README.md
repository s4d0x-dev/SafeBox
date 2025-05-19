# SafeBox 🔒

![SafeBox Logo](icon2.ico)  
**A powerful, open-source file encryption/decryption tool with a user-friendly GUI.**

SafeBox is a secure, easy-to-use application that allows you to encrypt and decrypt files using AES encryption. Protect your sensitive data with a custom password and enjoy features like metadata preservation and a modern interface. Built by **S4D0X**, SafeBox is free, open-source, and designed for both casual users and security enthusiasts.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-1.1.0-blue)](https://github.com/s4d0x-dev/safebox/releases)
[![GitHub Issues](https://img.shields.io/github/issues/s4d0x-dev/safebox)](https://github.com/s4d0x-dev/safebox/issues)

## ✨ Features

- **Secure Encryption**: Encrypt files with AES (Advanced Encryption Standard) using a user-defined password.
- **Password Confirmation**: Confirm your encryption password to avoid typos, ensuring secure file access.
- **Show Password Option**: Toggle password visibility for easy verification during encryption.
- **Metadata Preservation**: Store and retrieve original filenames for seamless decryption.
- **User-Friendly GUI**: Intuitive interface with tabs for Encrypt, Decrypt, and About.
- **Color-Coded Feedback**: Status messages display in green for success (`[+]`) and red for errors (`[-]`).
- **Cross-Platform Source**: Run from source on Windows, macOS, or Linux (installer for Windows only).
- **Open-Source**: Free to use, modify, and distribute under the MIT License.

## 📋 Requirements

### For End-Users (Windows Installer)
- Windows 10 or 11 (64-bit).
- 100 MB free disk space for installation.
- No additional software required (all dependencies included).

### For Developers (Running from Source)
- Python 3.8 or later.
- Required Python packages:
  - `pyAesCrypt` (for encryption/decryption).
- Development tools (optional, for building installer):
  - PyInstaller (for bundling).
  - NSIS (for creating the Windows installer).

## 🚀 Installation

### For End-Users (Windows)
1. **Download the Installer**:
   - Visit the [Releases](https://github.com/s4d0x-dev/safebox/releases) page and download `SafeBoxInstaller.exe` (version 1.1.0).
2. **Run the Installer**:
   - Double-click `SafeBoxInstaller.exe`.
   - Follow the wizard to install SafeBox to `C:\Program Files\SafeBox` (or a custom directory).
   - Admin privileges may be required.
3. **Launch SafeBox**:
   - Open from Start Menu > SafeBox > SafeBox.
   - The app is ready to use with no additional setup.

### For Developers (Running from Source)
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/s4d0x-dev/safebox.git
   cd safebox
   ```
2. **Set Up a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   # or: source venv/bin/activate  # macOS/Linux
   ```
3. **Install Dependencies**:
   ```bash
   pip install pyAesCrypt
   ```
4. **Run the App**:
   ```bash
   python gui.py
   ```

## 🛠️ Usage

SafeBox provides a simple GUI with three tabs: Encrypt, Decrypt, and About.

### Encrypt Tab
1. **Select Input File**: Click “Browse” to choose a file to encrypt.
2. **Enter Password**: Type your encryption password.
3. **Confirm Password**: Re-enter the password to verify (prevents typos).
4. **Show Password**: Check to view passwords in plain text (optional).
5. **Specify Output File**: Click “Browse” to set the output (`.ssb` file).
6. **Encrypt**: Click the “Encrypt” button. Success shows as `[+] File Encrypted as: ...` (green).

### Decrypt Tab
1. **Select Input File**: Browse for a `.ssb` file (encrypted with SafeBox).
2. **Enter Password**: Type the decryption password.
3. **Output Options**:
   - Check “Use original filename from metadata” to save to the original filename in a chosen directory (defaults to input file’s directory).
   - Uncheck to specify a custom output file.
4. **Decrypt**: Click “Decrypt”. Success shows as `[+] Decrypted to: ...` (green).

### About Tab
- View SafeBox version (1.1.0), description, and author details.
- Contact S4D0X via:
  - GitHub: [github.com/s4d0x-dev/safebox](https://github.com/s4d0x-dev/safebox)
  - Email: faredba@outlook.com
  - Facebook: [facebook.com/fared.baktashabdaly.1](https://facebook.com/fared.baktashabdaly.1)

## 🖼️ Screenshots

*Coming soon! Check back for GUI screenshots showcasing the Encrypt and Decrypt tabs.*

## 🛡️ Security Notes
- **Password Safety**: Choose strong passwords and store them securely. SafeBox does not store or recover passwords.
- **File Integrity**: Ensure encrypted (`.ssb`) files are not modified, as this may prevent decryption.
- **Backup**: Always back up important files before encryption.

## 🧑‍💻 Contributing
We welcome contributions to SafeBox! To contribute:
1. Fork the repository: [github.com/s4d0x-dev/safebox](https://github.com/s4d0x-dev/safebox).
2. Create a branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Make changes and commit:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push and create a pull request:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request on GitHub.

Please follow the [Code of Conduct](CODE_OF_CONDUCT.md) and report issues via [GitHub Issues](https://github.com/s4d0x-dev/safebox/issues).

## 🔨 Building the Installer
To build the Windows installer from source:
1. **Install Build Tools**:
   ```bash
   pip install pyinstaller
   ```
   Download and install NSIS from [nsis.sourceforge.net](https://nsis.sourceforge.net).
2. **Bundle with PyInstaller**:
   ```bash
   pyinstaller --onedir --windowed --name SafeBox --add-data "modules;modules" --icon icon2.ico gui.py
   ```
3. **Create Installer with NSIS**:
   - Save `SafeBoxInstaller.nsi` (provided in the repository).
   - Compile:
     ```bash
     makensis SafeBoxInstaller.nsi
     ```
4. **Output**: `SafeBoxInstaller.exe` is ready for distribution.

## 📜 License
SafeBox is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it.

## 🙏 Acknowledgments
- Built with [Python](https://www.python.org/), [Tkinter](https://docs.python.org/3/library/tkinter.html), and [pyAesCrypt](https://pypi.org/project/pyAesCrypt/).
- Thanks to the open-source community for inspiration and tools.

## 📬 Contact
For questions, suggestions, or issues:
- **GitHub Issues**: [github.com/s4d0x-dev/safebox/issues](https://github.com/s4d0x-dev/safebox/issues)
- **Email**: faredba@outlook.com
- **Facebook**: [facebook.com/fared.baktashabdaly.1](https://facebook.com/fared.baktashabdaly.1)

---

*SafeBox: Protect your files with confidence. Built by S4D0X.*