# owocryptor

This is a program that encrypts files within folders!

Name courtesy of https://github.com/jcollins17 :)

## Usage

```
usage: owocryptor.exe [-h] [--test] [--encryptpath ENCRYPTPATH] [--decryptpath DECRYPTPATH]

options:
  -h, --help            show this help message and exit
  --test
  --encryptpath ENCRYPTPATH
  --decryptpath DECRYPTPATH
```

## Running

### Test

This encrypts some test files in `~/encryption-test/sampledata`

    make run

### Screw up the entire C drive

Do NOT run this on your actual PC. You want to run this on a VM or something.

    poetry run python owocryptor.py --encryptpath C:/users/henry/encryption-test/sampledata

### Reverse it

    poetry run python owocryptor.py --decryptpath C:/users/henry/encryption-test/sampledata