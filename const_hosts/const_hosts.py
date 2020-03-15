#authut: edison Lai
#mail: edison@cstrail.com

import os
from threading import Timer

def read_file_as_str(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")

    all_the_text = open(file_path).read()
    open(file_path).close
    # print type(all_the_text)
    return all_the_text

def write_str_to_file(str, file_path):
    open(file_path, mode = 'w').write(str)
    open(file_path).close
    return

def task():
    global first_read
    str = read_file_as_str("/etc/hosts")
    if (str != first_read):
        write_str_to_file(first_read, "/etc/hosts")
        Timer(250, task, ()).start()
        print("reload original hosts")
    else:
        #write_str_to_file(first_read, "/home/edison/hosts")
        #print("equal")
        Timer(120, task, ()).start()
    return


def timedTask():
    '''
    第一个参数: 延迟多长时间执行任务(单位: 秒)
    第二个参数: 要执行的任务, 即函数
    第三个参数: 调用函数的参数(tuple)
    '''
    Timer(10, task, ()).start()


first_read = read_file_as_str("/etc/hosts")
timedTask()
