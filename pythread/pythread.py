from threading import current_thread as currentThread, enumerate as getThreads, Thread
from time import sleep


def init(func, delay, *args):
    t = currentThread()
    while getattr(t, "do_run", True):
        func(*args)
        sleep(delay)


def getThreadByName(name):
    for thread in getThreads():
        if thread.name == name:
            return thread


def createThread(name, func, *args):
    return Thread(target=init, args=(func, *args), name=name)


def stopThread(arg):
    if type(arg) == str:
        t = getThreadByName(arg)
    elif type(arg) == Thread:
        t = arg
    else:
        raise TypeError("Invalid type of argument!")
    t.do_run = False
    t.join()
