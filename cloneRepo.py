#!/usr/bin/python
import os

destination_path  = "destination/path/where/project/to/be/cloned"
clone_command = "git clone https://github.com/KeligMartin/4-SRC.git" 

clone_with_path = clone_command  +" "+ destination_path
os.system(clone_with_path)