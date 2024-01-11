# pythread 🧵

A Python library providing a user-friendly interface for managing both synchronous and asynchronous threads.

## Description 📚

**pythread** is a dual-threading Python library crafted to streamline the creation and management of threads in Python applications. It offers two distinct managers: 

- **SyncThreadManager**: Handles classic synchronous threads for executing blocking operations.
- **AsyncThreadManager**: Manages asynchronous tasks to run coroutines in a non-blocking fashion.

With **pythread**, starting, stopping, and supervising the life cycle of threads and async tasks becomes effortless, enhancing the readability and resilience of your code.

## Features ✨

- Initiate and terminate threads/tasks by name or reference.
- Accommodates additional arguments for threads/tasks.
- Simple management of thread/task lifecycle.
- Suitable for both sync and async implementations.

## Installation 📥

To get started with **pythread**, run:

```sh
pip install pythread
```

## Use Cases 🔧

- Conducting background tasks like I/O operations, processing data, or scheduled tasks.
- Handling multiple network connections in parallel.
- Implementing producer-consumer patterns using thread-safe queues.
- Crafting a basic task scheduler for time-based task execution.

## Documentation 📄

### SyncThreadManager

Facilitates the creation of synchronous threads for running functions with specific delays.

```python
# Initialize the SyncThreadManager
manager = SyncThreadManager()

# Function to run in a separate thread
def print_message(message):
    print(f"Thread message: {message}")

# Start a new thread with a specific action and delay
thread = manager.start_thread(name='PrinterThread', func=print_message, delay=1, 
    message='Hello from SyncThread!'
)

# Stop the thread using its name
manager.stop_thread('PrinterThread')

# Stop the thread using the thread object
manager.stop_thread(thread)
```

### AsyncThreadManager

Enables the execution of async coroutines concurrently.

```python
import asyncio
from pythread import AsyncThreadManager

# Initialize the AsyncThreadManager
manager = AsyncThreadManager()

# Example coroutine function
async def async_print_message(message):
    print(f"Async message: {message}")

# Start and run an async task
loop = asyncio.get_event_loop()
task = loop.run_until_complete(manager.start_task(name='AsyncPrinter', coro_func=async_print_message, message='Hello from AsyncThread!'))

# Stop the task using its name
loop.run_until_complete(manager.stop_task('AsyncPrinter'))

# Stop the task using the task object
loop.run_until_complete(manager.stop_task(task))
```