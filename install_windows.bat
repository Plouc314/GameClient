@echo off

set /p input=Do you have a python interpreter (version 3)? (y/n) 

if %input% == n (
    echo You will install the python interpreter in a few seconds...
    echo NOTE: You must add python to PATH !
    timeout 6
    python-3.7.7-amd64.exe
)
echo Installing pip...
python get-pip.py
echo Installing libraries...
pip install pygame
pip install requests
echo Setting up window size...
python set_size.py
