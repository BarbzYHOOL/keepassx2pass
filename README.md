Script for importing password data XML from
[KeepassX](https://www.keepassx.org/) to
[password-store](http://zx2c4.com/projects/password-store/).

## Requirements

- pass
- python3

## Usage

1. Install `pass` from https://www.passwordstore.org/ ([tutorial](https://medium.com/@chasinglogic/the-definitive-guide-to-password-store-c337a8f023a1)) and install one of the client if needed.
1. In KeepassX, export your passwords to XML: `File --> Export to -->  XML Keepass file`.
1. Run the script directly:
    chmod +x keepassx2pass.py
    ./keepassx2pass.py my_passwords.xml
Or with python:
    python keepassx2pass.py my_passwords.xml

## Difference with official script

Imported folders and passwords retain their empty space.

## Links

Official and up-to-date version: https://git.zx2c4.com/password-store/tree/contrib/importers/keepassx2pass.py
