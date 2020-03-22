#authut: edison Lai
#mail: edison@cstrail.com

import os
import sys

def file_path_exist(path):
    # 判断路径文件存在
    if not os.path.isfile(path):
        return False
    else:
        return True

def read_file_as_str(path):
    all_the_text = open(path).read()
    open(path).close
    # print type(all_the_text)
    return all_the_text

def write_str_to_file(str, path):  
    #print("write str:\n", str, "\nto", path)
    open(path, mode = 'w+').write(str)
    open(path).close
    return