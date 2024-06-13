#!/bin/bash

# Install dependencies
python -m pip install -r requirements.txt

# Run tests in parallel
pytest -n 2 test
