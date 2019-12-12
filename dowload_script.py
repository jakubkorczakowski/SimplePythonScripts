import os

system_name = str(os.uname())

with open('./stolen.txt', 'w') as f:
    f.write(system_name)

