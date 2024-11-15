@echo off
echo Running external.py at %date% %time% >> "log.txt"
pythonw.exe "external.py" >> "log.txt" 2>&1
echo Running scripts_and_registry.py at %date% %time% >> "log.txt"
pythonw.exe "scripts_and_registry.py" >> "log.txt" 2>&1
echo Running scan.py at %date% %time% >> "log.txt"
start "" pythonw.exe "scan.py" >> "log.txt" 2>&1
