clean:
	find . -name "*.pyc" | xargs rm | true

py_req:
	pip install -r requirements.txt

py_env:
	pyenv install 3.5.1
	pyenv local 3.5.1

all: clean py_env py_req
