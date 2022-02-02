#!/bin/bash

current_dir=$(pwd)
export PYTHONPATH=$PYTHONPATH:$current_dir


coverage run -m pytest tests --flakes -v