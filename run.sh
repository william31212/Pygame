#!/bin/bash

if [[ ! "$1" == "" ]] && [[ ! "$2" == "" ]]; then
	python3 $1/$2.py
fi