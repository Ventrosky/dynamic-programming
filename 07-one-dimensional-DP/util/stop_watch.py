import time

start_time = 0


def start_watch():
    global start_time
    start_time = time.time()


def stop_watch():
    global start_time
    return (time.time() - start_time)*1000000


def stop_watch_print(log):
    print(log.format(stop_watch()))
