# Learn how to run terminal commands from python
# Use the subprocess library to automate calling terminal commands with python
# The check call function runs an executable in terminal and then waits for process to finish before continuing script
import subprocess
for i in range(0, 5):
    subprocess.check_call(['python3', 'dummy_program.py'])
