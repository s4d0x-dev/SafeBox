from cx_Freeze import setup, Executable

setup(
    name="SafeBox",
    version="1.1.1",
    description="Secure file locker by S4D0X",
    executables=[Executable("safebox.py")],
)
