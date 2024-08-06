from time import sleep
import threading, queue
class Foo():
    def help(self):
        print('Running help')
        return 42


class MyThread(threading.Thread):

    def __init__(self, q_main, q_worker):
        self.queue_main = q_main
        self.queue_worker = q_worker
        threading.Thread.__init__(self)

    def run(self):
        while True:
            sleep(1)
            self.queue_main.put('run help')
            item = self.queue_worker.get()      # waits for item from main thread
            print('Received ', item)

queue_to_main, queue_to_worker = queue.Queue(), queue.Queue( )
my_work_thread = MyThread(queue_to_main, queue_to_worker)
my_work_thread.start()

while True:
    i = queue_to_main.get()
    print("que"+i)
    if i == "run help":
        rv = Foo().help()
        queue_to_worker.put(rv)
        print(rv)