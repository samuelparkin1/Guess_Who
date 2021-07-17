#!/bin/bash

# Checks to see if the user has Python 3 installed 
if ! [[ -x "$(command -v python3)" ]]
#If the user does NOT have python 3 installed it will display an error message 
#   and direct them to were they can install it.  
then
  echo 'Error: 
    This program runs on Python, but it looks like Python is not installed.
    To install Python, check out https://installpython3.com/' >&2
  exit 1
# if the user does have Python three 
else
  # Checks to see if the user has a programe files
  if [ ! -e "programe_files/guess_you.py" ]
  then
    echo "Unable to find files to start the programme. Please refer to help.txt documentation for troubleshooting." >&2
    exit 1
  else
    python3 programe_files/guess_you.py $1
  fi
fi

 