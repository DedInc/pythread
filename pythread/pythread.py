import threading
import asyncio
import time

class SyncThreadManager:
    def __init__(self):
        self.threads = []

    def start_thread(self, name, func, delay, **kwargs):
        def thread_target():
            while getattr(thread, 'do_run', True):
                func(**kwargs)
                time.sleep(delay)

        thread = threading.Thread(target=thread_target, name=name)
        thread.do_run = True
        thread.start()
        self.threads.append(thread)
        return thread

    def stop_thread(self, arg):
        thread = self.get_thread(arg)
        if thread:
            thread.do_run = False
            thread.join()

    def get_thread(self, arg):
        if isinstance(arg, threading.Thread):
            return arg
        elif isinstance(arg, str):
            for thread in self.threads:
                if thread.name == arg:
                    return thread
        return None

class AsyncThreadManager:
    def __init__(self):
        self.tasks = []

    async def start_task(self, name, coro_func, **kwargs):
        async def task_wrapper():
            await coro_func(**kwargs)
        
        task = asyncio.create_task(task_wrapper(), name=name)
        self.tasks.append(task)
        return task

    async def stop_task(self, arg):
        task = self.get_task(arg)
        if task:
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass

    def get_task(self, arg):
        if isinstance(arg, asyncio.Task):
            return arg
        elif isinstance(arg, str):
            for task in self.tasks:
                if task.get_name() == arg:
                    return task
        return None