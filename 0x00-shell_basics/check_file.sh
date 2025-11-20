#!/usr/bin/env bash
filename="$1"
wc -l ${filename}  # prints the number of lines of the file
head -n 1 ${filename}  # prints the first line of the file to stdout (standard output)
