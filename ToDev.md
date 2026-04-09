# Instructions to Devlover (a memo to myself) ;)
#### Here I layed some very usable and common instructions about this project to myself (or another devloper) to do not fail in any of steps.

## Setting Version in right way
###### Do all:
1. Edit `VERSION` variable in `gui.py`
2. Edit `filevers` and `prodvers` variable in `version.rc`
- note: as opensource-system versioning has 3 digits in ver and windows has 4 digits versioning system, I must add a zero(0) at the ending digit.
e.g. `1.2.0` to `1.2.0.0.` or in another example `1.2.7` to `1.2.7.0`

## pyInstaller
#### Making windows executable files: 
###### make GUI .exe in right way:
``` batch
pyinstaller --onefile --noconsole --add-data "modules;modules" --add-data "setup.py;." --add-data "safebox.py;." --version-file="version.rc" --icon "gui_icon.ico" --name SafeBox_GUI gui.py
```
<br>

###### Now the CLI .exe in right way:

``` batch
pyinstaller --onefile --add-data "modules;modules" --add-data "setup.py;." --icon "cli_icon.ico" --version-file="version.rc" --name safebox safebox.py
```
<br>

---

#### Making Linux executable files:
###### make GUI binary for linux in right way:
```bash
pyinstaller --onefile --noconsole --add-data="modules:modules" --add-data="setup.py:." --add-data="safebox.py:." --version-file="version.rc" --icon "gui_icon.ico" --name SafeBox_GUI gui.py
```
<br>

###### make CLI binary for linux in it's right way:
```bash
pyinstaller --onefile --add-data="modules:modules" --add-data="setup.py:." --icon "cli_icon.ico" --version-file="version.rc" --name safebox safebox.py
```
<br>

---

##### Packing .deb for debian based Linux-OS:
First make directory structure as bellow:
<pre>
safebox
├── DEBIAN
│   └── control
└── usr
    ├── bin
    │   ├── safebox
    │   └── safebox-gui
    └── share
        ├── applications
        │   └── safebox.desktop
        └── icons
            └── hicolor
                └── 48x48
                    └── apps
                        └── safebox.png

</pre>
Now `safebox/DEBIAN/control` file:
```
Package: safebox
Version: 1.2.0
Section: utils
Priority: optional
Architecture: amd64
Maintainer: S4D0X <faredba@outlook.com>
Description: SafeBox File Security Tool
 A powerful open-source file encryption and decryption tool with GUI.
```

time for `usr/share/applications/safebox.desktop` file:

```
[Desktop Entry]
Name=SafeBox-GUI
Type=Application
Exec=safebox-gui
Icon=safebox
GenericName=Safe File Encryption/Decryption App
Categories=GTK;Utility;Security;
Keywords=safebox;security;encrypt;decrypt;locker;crypto;ssb;s4d0x;sadox;
Comment=Encrypt and decrypt files securely.
StartupNotify=true
```
make sure the `safebox` (the cli file), `safebox-gui` (the gui version) copied to `safebox/usr/bin/` and all done as above tree.

###### packing .deb
```bash
sudo dpkg-deb --build safebox
```

it will deploy `safebox.deb` then we can share it or can install like `dpkg -i safebox.deb`

done for now.

