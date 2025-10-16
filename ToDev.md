# Instructions to Devlover (a memo to myself) ;)
#### Here I layed some very usable and common instructions about this project to myself (or another devloper) to do not fail in any of steps.

## Setting Version in right way
###### Do all:
1. Edit `VERSION` variable in `gui.py`
2. Edit `filevers` and `prodvers` variable in `version.rc`
- note: as opensource-system versioning has 3 digits in ver and windows has 4 digits versioning system, I must add a zero(0) at the ending digit.
e.g. `1.2.0` to `1.2.0.0.` or in another example `1.2.7` to `1.2.7.0`

## pyInstaller
###### make GUI .exe in right way:
``` batch
pyinstaller --onefile --noconsole --add-data "modules;modules" --add-data "setup.py;." --add-data "safebox.py;." --version-file="version.rc" --icon "gui_icon.ico" --name SafeBox_GUI gui.py
```
<br>

###### Now the CLI .exe in right way:


``` batch
pyinstaller --onefile --add-data "modules;modules" --add-data "setup.py;." --icon "cli_icon.ico" --version-file="version.rc" --name safebox safebox.py
```