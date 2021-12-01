APP := "compytetive"
PYTHONPATH := "."
VENV := "venv"
BIN := VENV + "/bin"
PYTHON := BIN + "/python"

build_dir := "build/" + APP

default := 'check test'

check:
	PYTHONPATH={{PYTHONPATH}} {{BIN}}/mypy {{APP}}

test:
    PYTHONPATH={{PYTHONPATH}} {{BIN}}/pytest .

clean:
    rm -fr dist build \
    __pycache__ .mypy_cache .pytest_cache \
    .cache {{APP}}.egg-info \
    {{APP}}/.mypy_cache {{APP}}/__pycache__ \
    tests/.mypy_cache tests/__pycache__

venv:
    #!/usr/bin/env sh
    python -m venv venv
    . venv/bin/activate
    pip install --upgrade pip setuptools wheel build
    pip install -e '.[dev]'

build:
    {{PYTHON}} -m build --wheel

install:
    PIP_REQUIRE_VIRTUALENV=0 pip install -e .
