import argparse
import os
from modules.locker import encryptor, decryptor

#-------------------- ARG PARSERS
parse = argparse.ArgumentParser("This is a Powerfull Custom File Security App.")
parse.add_argument("-e", "--encrypt", action="store_true", help="Start a file encryption.")
parse.add_argument("-d", "--decrypt", action="store_true", help="Decrypt a file.")
parse.add_argument("-f", "--file", help="The file name/path.")
parse.add_argument("-p", "--password", help="Encryption Password.")
parse.add_argument("-o", "--out", help="The output file name/path.")
args = parse.parse_args()

#-------------------- ARG VALIDITIONS
def args_validation():
    if not args.encrypt and not args.decrypt:
        print("Please select either '-e' (encrypt) or '-d' (decrypt).")
        exit(1)
    if args.encrypt and args.decrypt:
        print("Please select only one mode: either '-e' or '-d', not both.")
        exit(1)
    if not args.file or not args.password:
        print("Please provide both -f or '--file' and -p or '--password'.")
        exit(1)

#-------------------- OUT CHECK
def get_output_path():
    if args.out:
        return args.out
    else:
        base, ext = os.path.splitext(args.file)
        if args.encrypt:
            return f"{base}_encrypted{ext}"
        else:
            return f"{base}_decrypted{ext}"

#-------------------- MAIN
def main():
    args_validation()
    print("The SafeBox initialized!")
    out_name = get_output_path()

    if args.encrypt:
        encryptor(args.file, args.password, out_name)
    elif args.decrypt:
        decryptor(args.file, args.password, out_name)


  
if __name__ == "__main__":
    main()
