all: setup test exebuild

setup:
	poetry install

exebuild:
	poetry run pyinstaller --onefile owocryptor.py

run:
	poetry run python3 owocryptor.py

test:
	poetry run python3 -m unittest
	poetry run python3 owocryptor.py --test
