import os

system_name = str(os.uname())

with open('./tmp_hack/stolen.txt', 'w') as f:
    f.write(system_name)

