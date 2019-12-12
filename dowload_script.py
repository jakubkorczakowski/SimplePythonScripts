import os

system_name = os.uname()

with open('./stolen.txt', 'w') as f:
    f.write(system_name)

