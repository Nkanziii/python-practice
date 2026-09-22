import time

class timer:
    def __enter__(self):
        self.start = time.time()
        return self.start

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start
        print(f"Elapsed: {elapsed:.2f} seconds")
        
with timer():
    time.sleep(1)