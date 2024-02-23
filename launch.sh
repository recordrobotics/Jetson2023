#!/bin/bash

# Set up env variables
export LIBGL_ALWAYS_INDIRECT=1
export DISPLAY=:0
export SDL_VIDEODRIVER='dummy'
export OPENBLAS_CORETYPE=ARMV8

# Jetson folder
cd /home/frunkus/Jetson2023/

# Run main.py
python3 main.py
