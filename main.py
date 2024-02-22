import shutil
import os
from info import info

path_in = "E:/teledown/"


def get_file_type(ext):
    # print(ext)
    for i in info:
        if ext in info[i]:
            return i
    return "Extras"


for i in os.listdir(path_in):
    extension = (i.rsplit('.', 1))[-1]
    file_type = get_file_type(extension.lower())
    if not os.path.exists(path_in+file_type):
        os.mkdir(path_in+file_type)

    shutil.move(path_in+i,path_in+file_type)


