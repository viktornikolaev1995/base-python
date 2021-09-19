import threading
def writer(x,event_for_wait, event_for_set):
    for i in range(10):
        event_for_wait.wa