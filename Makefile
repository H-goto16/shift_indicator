help:
	@echo "source env/bin/activate"
	@echo "deactivate"

setup:
	sudo apt install picocom python3.12-venv
	python3 -m venv env

chmod:
	sudo chmod 666 /dev/ttyACM0

send:
	ampy --port /dev/ttyACM0 put src /
	@echo "Leaving... Hard resetting via RTS pin..."

ls:
	ampy --port /dev/ttyACM0 ls

monitor:
	picocom /dev/ttyACM0 -b 115200

run: send monitor