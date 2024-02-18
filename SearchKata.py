import os

kata_name = ''

for folders in os.getcwd():
    if f'{kata_name}.py' in folders:
        raise 'Have Kata'
