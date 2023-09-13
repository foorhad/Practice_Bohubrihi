import os

path = "../bohubrihi python course"
all_files = os.listdir(path)


# for i in all_files:
#     if os.path.isfile(os.path.join(path, i)):
#         print("{} is a file".format(i))

all_files = os.scandir(path)
for i in all_files:
    print(i)

import pathlib

path_object = pathlib.Path(path)

for i in path_object.iterdir():
    if i.is_file():
        print(i.name)