import file_lib
from threading import Timer
import sys
import pyinotify
import datetime

file = ['/etc/hosts']

def getRestSeconds():
    now = datetime.datetime.now()
    today_begin = datetime.datetime(now.year, now.month, now.day, 14, 0, 0)
    tomorrow_begin = datetime.datetime(now.year, now.month, now.day, 23, 0, 0)

    if (today_begin < now and tomorrow_begin > now):
        return (tomorrow_begin - now).seconds
    else:
        return 0

def timedTask(time, task, str, path):
    '''
    第一个参数: 延迟多长时间执行任务(单位: 秒)
    第二个参数: 要执行的任务, 即函数
    第三个参数: 调用函数的参数(tuple)
    '''
    Timer(time, task, (str, path)).start()

class MyEvent(pyinotify.ProcessEvent):
    def __init__(self, path, original_contents):
        self._path = path
        self._original_contents = original_contents
        self._count = 0

    def process_IN_MODIFY(self, event):
        if event.pathname in file:
            if (self._original_contents == file_lib.read_file_as_str("/etc/hosts")):
                return
            #else:
                #print ("\n\n\n",file_lib.read_file_as_str("/etc/hosts"))
                #print ("\n", self._original_contents)
            
            reset_time = getRestSeconds()
            print("/etc/hosts file has changed,file will be reset after", reset_time, "seconds\n")
            timedTask(reset_time, file_lib.write_str_to_file, self._original_contents, event.pathname)
            self._count = self._count + 1
            file_lib.write_str_to_file(str(self._count), "/home/edison/count.log")
        else:
            #print("/etc file has changed\n")
            pass
