#!/bin/bash

for py_file in $(find ../agencias -name *.py)

do
    python3 $py_file

done 