<h1 align="center">pythread - Useful module for comfortable managing with threading.</h1>

<br>

<h1 align="center"> -How to use- </h1>

```python
import pythread as ptr

ptr.createThread('NameOfThread', func, 5) #NameOfThread - name of thread, func - function, 5 - delay of run function
ptr.stopThread('NameOfThread') #stop thread
t = ptr.getThreadByName('NameOfThread') #select thread by name
```