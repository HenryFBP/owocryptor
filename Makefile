all: test exebuild

setup:
	poetry install

exebuild:
	poetry run pyinstaller --onefile encrypt_desktop_files.py

run:
	poetry run python3 encrypt_desktop_files.py

test:
	poetry run python3 -m unittest