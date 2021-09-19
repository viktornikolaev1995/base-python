from time import time, sleep
from os import fork, getpid, wait
#
# pid = os.getpid()
#
# while True:
#     print(pid, time.time())
#     time.sleep(2)
#

#
# pid = fork()
# if pid == 0:
#     while True:
#         print("child:", getpid())
#         sleep(5)
# else:
#     print("parent:", getpid())
#     wait()










# foo = "bar"
# if os.fork() == 0:
#     foo = "baz"
#     print("child:", foo)
# else:
#     print("parent", foo)
#     os.wait()


from multiprocessing import Process

class PrintProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        print("hello", self.name)

p = PrintProcess("Viktor")
p.start()
p.join()