import time
import subprocess
import os
import sys

day = sys.argv[1]
part = sys.argv[2]+'.py'

justfile_dir = os.path.dirname(os.path.realpath(__file__))
part_path = os.path.join(justfile_dir, day, 'src', part)

# Last change time
current_mod_time = os.stat(part_path).st_mtime

while True:
    # If there was a change run pytest
    if os.stat(part_path).st_mtime != current_mod_time:
        current_mod_time = os.stat(part_path).st_mtime
        # Change the current working directory because pytest runs from it
        os.chdir(os.path.join(justfile_dir, day))
        # Insert path of common.py file(same folder as justfile)
        # This is used for @time_execution custom decorator
        subprocess.run('cmd /C "set PYTHONPATH={} && pytest -s src/__tests__/test_{}"'.format(
            os.path.join(justfile_dir), part), shell=True)

    # Wait before checking again
    time.sleep(1)
