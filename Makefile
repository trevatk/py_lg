
init:
	pip install -r requirements.txt

build:
	docker build -t trevatk/py_lg:latest .

lint:
	black src

test:
	python -m pytest