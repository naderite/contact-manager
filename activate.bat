@echo off
REM Navigate to the Scripts directory of the virtual environment
cd /d venv\Scripts\

REM Start a new cmd window, activate the virtual environment, and navigate back to the initial directory
start cmd /k "activate && cd /d ..\.."



