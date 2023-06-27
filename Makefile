all: setup tests

tests: test exebuild testexebuild

setup:
	poetry install

exebuild:
	poetry run pyinstaller owocryptor.spec

testexebuild:
	./dist/owocryptor --test

run:
	poetry run python3 owocryptor.py

test:
	poetry run python3 -m unittest
	poetry run python3 owocryptor.py --test
