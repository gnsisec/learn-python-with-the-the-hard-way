[![](http://image.prntscr.com/image/f07396d807c94bd48757a28060804d59.png)](https://learncodethehardway.org/python/)### Overview
A good stuff for newbie for learning programming. Learning basics of Python language based on Learn Python - The Hard Way course.

### Requirements
* Windows, Linux or Mac OS X
* Python 2.7
* Pip (Python Package Manager)

### Installing Python
* on Linux: Most of the Linux distributions should have installed Python by default
* on Windows: Download Python at: https://www.python.org/downloads/windows/ and run installer
* on Mac OS X: Download Python at: https://www.python.org/downloads/mac-osx/

### Executing Python scripts from terminal
* on Linux: Most of the Linux distributions should have enabled Python by default, so simply open terminal and type *python* to see if everything works.
* on Windows: add `/PythonXX` (e.g. `C:/Python27`) into `Path` environmental variable. Location of the Python directory depends on your configuration. Next, re-run terminal window and type `python`
* in order to check installed version of the Python, type: `python --version`
* in order to exit python console type `exit()`

### Pip
Pip is a Python Package Manager.

##### Installing Pip on Windows
1. Download: https://raw.github.com/pypa/pip/master/contrib/get-pip.py script
2. Execute: `python get-pip.py`
3. *pip.exe* and *easy_install.exe* files now should be located at: */PythonXX/Scripts* (e.g. *C:/Python27/Scripts*)
4. Add */PythonXX/Scripts* (e.g. *C:/Python27/Scripts*) directory into *Path* environmental variable.
5. Re-run terminal window
6. Type `pip`, to check if package manager works
7. You can type `pip --version`, in order to check version of the pip

##### Installing Pip on Linux
1. Open terminal
2. Type `sudo apt-get install python-pip`

##### Installing Pip on macOS
1. Open terminal
2. Type `brew install python3`

This command will install python and pip.

##### Pyhton code style guide
This document gives coding conventions for the Python code comprising the standard library in the main Python distribution.
https://www.python.org/dev/peps/pep-0008

##### Using Pip
* In order to install desired package just type `pip install desired_package` (e.g. `pip install Flask`)
* If you are working on Linux, type `sudo pip install desired_package` (e.g. `sudo pip install Flask`)
* Index of available packages can be found at: https://pypi.python.org/pypi/
* List of installed packages can be displayed with `pip freeze` command.
