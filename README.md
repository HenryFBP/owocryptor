# Encryption Program

## Running

### Test

This encrypts some test files in `~/encryption-test/sampledata`

    make run

### Screw up the entire C drive

Do NOT run this on your actual PC. You want to run this on a VM or something.

    poetry run python owocryptor.py --encryptpath C:/users/henry/encryption-test/sampledata

### Reverse it

    poetry run python owocryptor.py --decryptpath C:/users/henry/encryption-test/sampledata