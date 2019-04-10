#!/bin/bash

pyinstaller -F $1 -p . -p RHframework --icon assets/favicon.ico rifleman.py