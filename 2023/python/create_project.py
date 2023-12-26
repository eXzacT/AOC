import os
import shutil
import sys

day = sys.argv[1]

# Get path of this script and add the day argument
script_dir = os.path.dirname(os.path.realpath(__file__))
new_project_path = os.path.join(script_dir, day)

# Copy all the files from template to a newly created folder
template_dir = os.path.join(script_dir, 'daily-template')
shutil.copytree(template_dir, new_project_path)

# Replace placeolders in only these files(since others don't have them)
files_to_update = ['part1.py', 'part2.py']
for filename in files_to_update:
    file_path = os.path.join(new_project_path, 'src', filename)
    with open(file_path, 'r+') as file:
        file_contents = file.read()
        file_contents = file_contents.replace('{{day}}', day)
        file.seek(0)
        file.write(file_contents)
        file.truncate()

print(f'Project \'{day}\' created successfully from template \'src/template\'')
