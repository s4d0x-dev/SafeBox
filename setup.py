from cx_Freeze import setup, Executable

setup(
    name="SafeBox",
    version="1.2.0",
    description="Secure file locker by S4D0X",
    executables=[Executable("safebox.py")],
)
