import argparse
import sys
from core.safebox_handler import SafeBox

class SafeBoxCLI:
    def __init__(self):
        self.safebox = SafeBox()
        self.args = self.parse_arguments()

    def parse_arguments(self):
        parser = argparse.ArgumentParser("SafeBox CLI")

        parser.add_argument("-e", "--encrypt", action="store_true", help="Encrypt a File")
        parser.add_argument("-d", "--decrypt", action="store_true", help="Decrypt a File")
        parser.add_argument("-f", "--file", help="Path to the File", required=True)
        parser.add_argument("-p", "--password", help="The Password", required=True)
        parser.add_argument("-o", "--out", help="Path to the output File, including the File name (Optional)")

        return parser.parse_args()

    def validate(self):
        if not self.args.encrypt and not self.args.decrypt:
            sys.exit("Select either '-e' or '-d'")
        
        if self.args.encrypt and self.args.decrypt:
            sys.exit("Select one mode only ('-e' or '-d')")

        if not self.args.file or not self.args.password:
            sys.exit("both, 'file' and 'password' are required")

    def run(self):
        self.validate()

        if self.args.encrypt:
            print(
                self.safebox.encrypt_file(
                    self.args.file,
                    self.args.password,
                    self.args.out
                )
            )
        elif self.args.decrypt:
            print(
                self.safebox.decrypt_file(
                    self.args.file,
                    self.args.password,
                    self.args.out
                )
            )


if __name__ == "__main__":
    cli = SafeBoxCLI()
    cli.run()