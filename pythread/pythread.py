from threading import currentThread, enumerate as getThreads, Thread
from time import sleep

def initer(func, delay):
    t = currentThread()
    while getattr(t, "do_run", True):
        func()
        sleep(delay)

def getThreadByName(name):
    for thread in getThreads():
        if thread.name == name:
            return thread

def createThread(name, func, delay=0):
    Thread(target=initer, args=(func, delay,), name=name).start()

def stopThread(name):
    t = getThreadByName(name)
    t.do_run = False
    t.join()