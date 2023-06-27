import shutil
import os
import sys
from cryptography.fernet import Fernet

'''
This program will copy "sampledata" to the "~/encryption-test/sampledata", recursively encrypt all files in the "sampledata" directory, and delete the original "sampledata" directory.
'''

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

ENC_FILE_EXT=".enc-henryfbp"

SAMPLE_DATA_DEST_PATH = os.path.expanduser("~/encryption-test/sampledata")

ENCRYPTION_KEY_RAW = b"acS7-XGrwdwu7Kfx1swNCsT6XMYvcv5BKAonky8MkEo="
FERNET = Fernet(ENCRYPTION_KEY_RAW)


def decrypt_file(
        file_path_enc: str,
        appender=lambda fh: None
) -> str:
    data_decrypted = None

    # read file contents, encrypt data in memory
    try:
        with open(file_path_enc, 'rb') as f:
            data_encrypted: bytes = f.read()

            data_decrypted = FERNET.decrypt(data_encrypted)
    except PermissionError as pe:
        print("READ PERMISSION ERROR: " + file_path_enc)
        return

    # write encrypted data to file
    try:
        with open(file_path_enc, 'wb') as f:
            f.write(data_decrypted)

            # append data to file if we want to
            appender(f)
    except PermissionError as pe:
        print("WRITE PERMISSION ERROR: " + file_path_enc)
        return

    # rename file
    file_path_regular: str = file_path_enc.replace(ENC_FILE_EXT, '')
    shutil.move(file_path_enc, file_path_regular)

    print("MV " + file_path_enc + " " + file_path_regular)

    return file_path_regular


def encrypt_file(
        file_path: str,
        appender=lambda fh: (None)
) -> str:
    data_encrypted = None

    # read file contents, encrypt data in memory
    try:
        with open(file_path, 'rb') as f:
            data: bytes = f.read()

            data_encrypted = FERNET.encrypt(data)
    except PermissionError as pe:
        print("READ PERMISSION ERROR: "+file_path)
        return

    # write encrypted data to file
    try:
        with open(file_path, 'wb') as f:
            f.write(data_encrypted)

            # append data to file if we want to
            appender(f)
    except PermissionError as pe:
        print("WRITE PERMISSION ERROR: "+file_path)
        return

    # rename file
    file_path_enc: str = file_path + ENC_FILE_EXT
    shutil.move(file_path, file_path_enc)

    print("MV " + file_path + " " + file_path_enc)

    return file_path_enc


def copy_sampledata_to_dest():
    shutil.copytree(os.path.abspath(THIS_DIR + "/sampledata"), SAMPLE_DATA_DEST_PATH)


def delete_sampledata_from_dest():
    shutil.rmtree(SAMPLE_DATA_DEST_PATH)

def decrypt_folder_recursively(folder_path) -> None:
    # walk tree recursively
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            if file_path.endswith(ENC_FILE_EXT):
                print("DECRYPT " + file_path)
                decrypt_file(file_path)
            else:
                # don't decrypt, it's already decrypted
                print("SKIP " + file_path)
                continue

def encrypt_folder_recursively(folder_path) -> None:
    # walk tree recursively
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            if file_path.endswith(ENC_FILE_EXT):
                # don't encrypt, it's already encrypted
                print("SKIP " + file_path)
                continue

            print("ENCRYPT " + file_path)
            encrypt_file(file_path)


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action='store_true')
    parser.add_argument("--encryptpath")
    parser.add_argument("--decryptpath")
    args = parser.parse_args()

    if args.test:
        if os.path.exists(SAMPLE_DATA_DEST_PATH):
            delete_sampledata_from_dest()

        if not os.path.exists(SAMPLE_DATA_DEST_PATH):
            copy_sampledata_to_dest()

        encrypt_folder_recursively(SAMPLE_DATA_DEST_PATH)
        exit(0)

    if args.encryptpath:
        encrypt_path = args.encryptpath
        encrypt_path = os.path.abspath(encrypt_path)

        print("Going to recursively encrypt "+encrypt_path)
        print("CTRL-C to cancel! (waiting 5 seconds)")
        import time
        time.sleep(5)

        encrypt_folder_recursively(encrypt_path)

    if args.decryptpath:
        decrypt_path = args.decryptpath
        decrypt_path = os.path.abspath(decrypt_path)

        print("Going to recursively decrypt "+decrypt_path)
        print("CTRL-C to cancel! (waiting 5 seconds)")
        import time
        time.sleep(5)

        decrypt_folder_recursively(decrypt_path)
