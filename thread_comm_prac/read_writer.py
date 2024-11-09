import threading
import time


class ReadersWriters:
    def __init__(self):
        self.lock = threading.Lock()
        self.readers = 0

    def reader(self, id):
        while True:
            with self.lock:
                self.readers += 1
                if self.readers == 1:
                    print(f"Reader {id} is reading")
            time.sleep(1)
            with self.lock:
                self.readers -= 1

    def writer(self, id):
        while True:
            with self.lock:
                print(f"Writer {id} is writing")
            time.sleep(1)


rw = ReadersWriters()
threading.Thread(target=rw.reader, args=(3,)).start()
threading.Thread(target=rw.writer, args=(1,)).start()
