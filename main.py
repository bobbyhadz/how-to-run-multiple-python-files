# Run multiple Python files concurrently 

import subprocess

# Create and start the processes
proc1 = subprocess.Popen(['python', 'a.py'])
proc2 = subprocess.Popen(['python', 'b.py'])
proc3 = subprocess.Popen(['python', 'c.py'])

# Wait for the processes to finish
proc1.wait()
proc2.wait()
proc3.wait()
