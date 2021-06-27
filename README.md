# Repository-Cleaner

A python script for linux systems used to clean any directory and sort its files by type 
- photos
- videos
- documents
- folders
- archives
- others
- songs


## Requirements

1) Linux System
2) python package installed 

You can check whether python is installed in your system by typing : " python --version "
if it's not installed you can type sudo apt install python.

## How to use it

this script takes an array of directories' absolute paths as argument and it will clean these target directories
if not provided with a directory path, the script cleans the Desktop.

examples of running script : 

  - python sortDirectoryFiles.py // to clean desktop.
  - python sortDirectoryFiles.py /home/<username>/Donwloads /home<username>/Pictures /home/<username>/Desktop // to clean the mentioned directories.
  
## Possibility of improvment

- You can create an alias to facilitate the use of the script by adding the following line in the .bashrc file ( in ubuntu ).

  - alias cleanDesktop='python /home/<username>/sortDirectoryFiles.py'
 