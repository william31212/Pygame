#!/bin/bash

if [[ ! "$1" == "" ]] && [[ ! "$2" == "" ]]; then
	pushd $1 > /dev/null
	python3 $2.py
	popd > /dev/null
fi