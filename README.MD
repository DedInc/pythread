<h1 align="center">pythread - Useful module for comfortable managing with threading.</h1>

<br>

<h1 align="center"> -How to use- </h1>

```python
import pythread as pt

def func(a, b):
    print(a, b)

t = pt.createThread('NameOfThread', func, 5, 'a', 'b') #NameOfThread - name of thread, func - function, 5 - delay of run function, 'a', and 'b' arguments of function
t.start() #start the thread

pt.stopThread('NameOfThread') #stop thread by name
pt.stopThread(t) #stop thread by thread
t = ptr.getThreadByName('NameOfThread') #select thread by name
```